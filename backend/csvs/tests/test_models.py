import os
import pytz
import datetime
from unittest import mock
from django.conf import settings
from django.db import transaction, IntegrityError
from django.test import TestCase
from csvs.models import CSVData
from .factories import CsvFactory


class CSVDataTest(TestCase):

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
    
    def test_create_csv(self):
        csv = CsvFactory()
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)

    def test_no_name_field(self):
        try:
            with transaction.atomic():
                csv = CsvFactory(name=None)
        except:
            pass
        count = CSVData.objects.all().count()
        self.assertEqual(count, 0)

    def test_name_field_exeed_max_length(self):
        name = 'a' * 256
        try:
            with transaction.atomic():
                csv = CsvFactory(name=name)
        except:
            pass
        count = CSVData.objects.all().count()
        self.assertEqual(count, 0)

    def test_no_unique_name_field(self):
        csv = CsvFactory()
        try:
            with transaction.atomic():
                csv_same_name = CsvFactory(name=csv.name)
        except:
            pass
        count = CSVData.objects.all().count()
        self.assertEqual(count, 1)

    def test_correct_file_location(self):
        csv = CsvFactory()
        self.assertIn(settings.CSV_DIR, csv.file.name)

    def test_meta_ordering(self):
        csv = CsvFactory()
        ordering = csv._meta.ordering
        self.assertEqual(ordering[0], 'created_at')

    def test_str_representation(self):
        csv = CsvFactory()
        self.assertEqual(str(csv), csv.name)

    def test_no_json_field(self):
        try:
            with transaction.atomic():
                csv = CsvFactory(json_data=None)
        except IntegrityError:
            pass
        count = CSVData.objects.all().count()
        self.assertEqual(count, 0)

    def test_json_field_type(self):
        csv = CsvFactory()
        self.assertIn(type(csv.json_data).__name__, 'dict/list')
        
    def test_created_at_type(self):
        csv = CsvFactory()
        self.assertEqual(type(csv.created_at).__name__, 'datetime')

    def test_created_at_time(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            csv = CsvFactory()
            self.assertEqual(csv.created_at, mocked)


