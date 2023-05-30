import os
import json
from django.test import TestCase
from csvs.models import CSVData
from django.core.files.base import File

from ..serializers import (
    CSVDataSerializer,
    CSVDataListAllSerializer,
    CSVDataEnrichSerializer
)
from .factories import CsvFactory

f_csv = open('csvs/tests/files/base_test_file.csv')
f_json_content = open('csvs/tests/files/base_test_file.json')
json_content = json.load(f_json_content)


class CSVDataSerializerTest(TestCase):

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
    
    def test_contains_expected_fields(self):
        csv = CsvFactory()
        serializer = CSVDataSerializer(instance=csv)

        # Check that the serialized data has the expected keys
        expected_keys = ['name', 'file', 'json_data', 'created_at']
        self.assertEqual(list(serializer.data.keys()), expected_keys)

    def test_contains_expected_values(self):
        csv = CsvFactory()
        serializer = CSVDataSerializer(instance=csv)

        # Check that the serialized data has the expected values
        file_value = '/media/csv_files/files/' \
            + os.path.basename(csv.file.name)
        created_value = \
            csv.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        expected_values = [
            csv.name, 
            file_value,
            json_content,
            created_value
        ]
        self.assertCountEqual(
            serializer.data.values(),
            expected_values,
        )

    def test_correct_content(self):
        csv_data = {
            'name': 'CorrectCsv',
            'file': File(f_csv)
        }
        serializer = CSVDataSerializer(data=csv_data)
        self.assertEqual(serializer.is_valid(), True)

    def test_no_file_field(self):
        csv_missing_file = {
            'name': 'NoFileCsv',
            'file': None
        }
        wrong_serializer = CSVDataSerializer(data=csv_missing_file)
        self.assertEqual(wrong_serializer.is_valid(), False)

    def test_wrong_file_field(self):
        csv_missing_file = {
            'name': 'NoFileCsv',
            'file': 'wrong content'
        }
        wrong_serializer = CSVDataSerializer(data=csv_missing_file)
        self.assertEqual(wrong_serializer.is_valid(), False)

    def test_duplicated_csv_name(self):
        # Check if 'name' field is non-unique
        stored_csv = CsvFactory()
        serializer = CSVDataSerializer(instance=stored_csv)
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)
        csv_data = {
            'name': stored_csv.name,
            'file': File(f_csv)
        }
        serializer = CSVDataSerializer(data=csv_data)
        self.assertEqual(serializer.is_valid(), False)


class CSVDataListAllSerializerTest(TestCase):

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
    
    def test_validate_returned_fields(self):
        # Check if serializer requires 'name' field
        stored_csv = CsvFactory()
        serializer = CSVDataListAllSerializer(instance=stored_csv)
        self.assertCountEqual(
            set(serializer.data.keys()),
            set(['name', 'file', 'created_at']),
        )
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)
    
    def test_validate_returned_values(self):
        # Check if serializer requires 'name' field
        stored_csv = CsvFactory()
        serializer = CSVDataListAllSerializer(instance=stored_csv)
        file_value = '/media/csv_files/files/' \
            + os.path.basename(stored_csv.file.name)
        created_value = \
            stored_csv.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        self.assertCountEqual(
            set(serializer.data.values()),
            set([stored_csv.name, file_value, created_value]),
        )

    def test_duplicated_csv_name(self):
        # Check if 'name' field is non-unique
        stored_csv = CsvFactory()
        serializer = CSVDataSerializer(instance=stored_csv)
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)
        csv_data = {
            'name': stored_csv.name,
            'file': File(f_csv)
        }
        serializer = CSVDataListAllSerializer(data=csv_data)
        self.assertEqual(serializer.is_valid(), False)


class CSVDataEnrichSerializerTest(TestCase):

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
    
    def setUp(self):
        self.enrich_csv = {
            'name': 'EnrichedCsv',
            'additional_api_json': json_content,
            'key_column_stored': 'id',
            'key_column_api': 'id_api'
        }
        self.serializer = CSVDataEnrichSerializer(instance=self.enrich_csv)

    def test_contains_expected_fields(self):
        # Check that the serialized data has the expected fields
        self.assertCountEqual(
            set(self.serializer.data.keys()),
            set(['name', 'additional_api_json', 'key_column_stored', 
            'key_column_api']),
        )

    def test_name_field_types(self):
        # Check if the serializer produces the expected data types

        expected_field_types = ['str', 'dict/list', 'str', 'str']
        for i, field_key in enumerate(self.serializer.data.keys()):
            if type(self.serializer.data[field_key]).__name__ not in expected_field_types[i]:
                self.fail(f'Key type of "{field_key}" does not match expected type <{expected_field_types[i]}>')

    def test_name_field_not_exist(self):
        # Check if serializer requires 'name' field
        wrong_enrich_csv = self.enrich_csv
        wrong_enrich_csv['name'] = ''
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)

    def test_name_existing(self):
        # Check if the name of the file for enrichment is present
        stored_csv = CsvFactory()
        serializer = CSVDataSerializer(instance=stored_csv)
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)
        wrong_enrich_csv = self.enrich_csv
        wrong_enrich_csv['name'] = stored_csv.name
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), True)

    def test_additional_json_field_not_exist(self):
        # Check if serializer requires 'additional_api_json' field
        wrong_enrich_csv = self.enrich_csv
        wrong_enrich_csv['additional_api_json'] = None
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)

    def test_key_column_stored_field_not_exist(self):
        # Check if serializer requires 'key_column_stored' field
        wrong_enrich_csv = self.enrich_csv
        wrong_enrich_csv['key_column_stored'] = ''
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)
        wrong_enrich_csv['key_column_stored'] = None
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)

    def test_key_column_api_field_not_exist(self):
        # Check if serializer requires 'key_column_api' field
        wrong_enrich_csv = self.enrich_csv
        wrong_enrich_csv['key_column_api'] = ''
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)
        wrong_enrich_csv['key_column_api'] = None
        wrong_serializer = CSVDataEnrichSerializer(data=wrong_enrich_csv)
        self.assertEqual(wrong_serializer.is_valid(), False)
        
