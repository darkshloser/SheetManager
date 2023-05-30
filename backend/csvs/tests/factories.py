import json
import factory
from django.utils import timezone
from csvs.models import CSVData
from csvs import models
from faker import Faker

fake = Faker()

f_json_content = open('csvs/tests/files/base_test_file.json')
json_content = json.load(f_json_content)

class CsvFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CSVData

    name = fake.file_name(extension='csv')
    file = factory.django.FileField(filename='./files/base_test_file.csv')
    json_data = json_content
    created_at = timezone.now()

