import os
import json
import pytz
import pytest
import datetime
from unittest import mock
from django.test import override_settings
from django.conf import settings
from django.core.cache import cache
from django.core.files.base import File
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from csvs.models import CSVData
from .factories import CsvFactory


class CSVDataUploadViewTest(APITestCase):

    @classmethod
    def tearDownClass(cls):
        # specify the directory path
        directory = './csv_files/'

        # Remove all files and get directories
        dir_list = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                dir_list.append(os.path.join(root, name))

        for dir_path in dir_list:
            os.rmdir(dir_path)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_create_csv_data(self):
        url = reverse("file-list")
        f_csv = open('csvs/tests/files/base_test_file.csv')
        f_json_content = open('csvs/tests/files/base_test_file.json')
        json_content = json.load(f_json_content)
        csv_name = 'test_csv_1'
        data = {
            'name': csv_name,
            'file': File(f_csv)
        }
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            response = self.client.post(url, data=data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(CSVData.objects.count(), 1)
            resultant_csv = CSVData.objects.get()
            self.assertEqual(resultant_csv.name, csv_name)
            filename = os.path.basename(f_csv.name)[:-4]
            expected_file_beginning = os.path.join(settings.CSV_DIR, filename)
            resultant_file = resultant_csv.file.name
            self.assertTrue(
                resultant_file.startswith(expected_file_beginning)
            )
            self.assertEqual(
                json.loads(resultant_csv.json_data),
                json_content
            )
            self.assertEqual(
                resultant_csv.created_at.strftime('%Y-%m-%dT%H:%M:%SZ'),
                mocked.strftime('%Y-%m-%dT%H:%M:%SZ')
            )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_delete_csv(self):
        csv = CsvFactory()
        url = reverse('file-list')
        response = self.client.delete(f'{url}?name={csv.name}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CSVData.objects.count(), 0)
        self.assertEqual(
            response.data,
            {'details': 'CSV data deleted successfully.'}
        )

    def test_delete_non_existent_csv(self):
        csv_name = 'non_existent'
        url = reverse('file-list')
        response = self.client.delete(f'{url}?name={csv_name}')
        self.assertEqual(response.status_code, status.HTTP_410_GONE)
        self.assertEqual(
            response.data,
            {"details": f"Specified CSV object {csv_name} does not exist."}
        )

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_update_csv(self):
        url = reverse("file-list")
        f_csv = open('csvs/tests/files/base_test_file.csv')
        expected_csv = open('csvs/tests/files/updated_test_file.csv')
        csv_name = 'test_csv_1'
        data = {
            'name': csv_name,
            'file': File(f_csv)
        }
        new_json = {'json_data': '[{"col1": "val1", "col2": "val2"}]'}
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            resp_new_csv = self.client.post(url, data=data)
            resp_upd_csv = self.client.put(
                f'{url}?name={csv_name}', data=new_json
            )
            csv_obj = CSVData.objects.get(name=csv_name)
            filepath = os.path.join(settings.MEDIA_URL, csv_obj.file.name)
            expected_response_data = {
                'name': csv_name,
                'file': filepath,
                'json_data': '[{"col1": "val1", "col2": "val2"}]',
                'created_at': mocked.strftime('%Y-%m-%dT%H:%M:%SZ')
            }
            self.assertEqual(resp_upd_csv.data, expected_response_data)
            updated_csv = open(csv_obj.file.name)
            self.assertEqual(
                expected_csv.readlines(),
                updated_csv.readlines()
            )

    def test_update_without_name_or_json_data(self):
        name = 'test_csv'
        data = {'json_data': '[{"col1": "val1", "col2": "val2"}]'}
        csv = CsvFactory(name=name)
        url = reverse("file-list")
        response = self.client.put(f'{url}?name=', data)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        response = self.client.put(f'{url}?name={name}')
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEqual(
            {"details": "Incomplete request"},
            response.data
        )
    
    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_list_csvs(self):
        csv_1 = CsvFactory(name='csv_1')
        csv_2 = CsvFactory(name='csv_2')
        cache.delete(settings.CACHE_ALL_CSVS_KEY)
        self.assertEqual(CSVData.objects.count(), 2)
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(
            set(response.data[0].keys()),
            set(['name', 'file', 'created_at']),
        )


class CSVDataEnrichViewTest(APITestCase):

    @classmethod
    def tearDownClass(cls):
        # specify the directory path
        directory = './csv_files/'

        # Remove all files and get directories
        dir_list = []
        for root, dirs, files in os.walk(directory):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                dir_list.append(os.path.join(root, name))

        for dir_path in dir_list:
            os.rmdir(dir_path)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_enrich_csvs(self):
        url = reverse("file-list")
        f_csv = open('csvs/tests/files/base_enrich.csv')
        f_api_json_content = open('csvs/tests/files/api_enrich.json')
        api_json_content = f_api_json_content.read()
        f_expected_json_content = open('csvs/tests/files/expected_enrich.json')
        expected_json_content = f_expected_json_content.read()
        csv_name = 'test_csv_enrich_1'
        data = {
            'name': csv_name,
            'file': File(f_csv)
        }
        response = self.client.post(url, data=data)
        self.assertEqual(CSVData.objects.count(), 1)
        url = reverse('enrich-list')
        data_to_enrich = {
            'name': csv_name,
            'additional_api_json': f'{api_json_content}',
            'key_column_stored': 'posting_user_id',
            'key_column_api': 'id'
        }
        response = self.client.post(url, data=data_to_enrich)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CSVData.objects.count(), 2)
        self.assertNotEqual(response.data.get('name'), csv_name)
        self.assertEqual(
            '/media/csv_files',
            os.path.dirname(response.data.get('file'))
        )
        self.assertEqual(
            json.loads(response.data.get('json_data')),
            json.loads(expected_json_content)
        )










