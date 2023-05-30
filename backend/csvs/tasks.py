import os
import csv
import json
from time import sleep
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.core.mail import send_mail
from celery import shared_task
from .models import CSVData


CACHE_LIST_CSVS_TTL = getattr(settings, 'CACHE_LIST_CSVS_TTL', DEFAULT_TIMEOUT)
CACHE_SINGLE_CSV_TTL = getattr(settings, 'CACHE_SINGLE_CSV_TTL', DEFAULT_TIMEOUT)
CACHE_ALL_CSVS_KEY = getattr(settings, 'CACHE_ALL_CSVS_KEY', None)


@shared_task()
def save_csv_items_in_redis_task(name):
    """Save single or all CSVs into Redis"""
    if name == CACHE_ALL_CSVS_KEY:
        value = CSVData.objects.all()
        cache.set(name, value, timeout=CACHE_LIST_CSVS_TTL)
    else:
        value = CSVData.objects.filter(name=name)
        if value.first():
            cache.set(name, value, timeout=CACHE_SINGLE_CSV_TTL)
            # Update cache which lists all csv items
            if CACHE_ALL_CSVS_KEY in cache and len(value) > 0:
                all_csvs = list(cache.get(CACHE_ALL_CSVS_KEY))
                is_existing = any(item.name == name for item in all_csvs)
                if not is_existing:
                    all_csvs.extend(value)
                else:
                    for idx, item in enumerate(all_csvs):
                        if item.name == name:
                            all_csvs[idx]=value[0]
                            break
                cache.set(
                    CACHE_ALL_CSVS_KEY,
                    all_csvs, 
                    timeout=CACHE_LIST_CSVS_TTL
                )


@shared_task()
def delete_csv_from_redis_task(name):
    """Remove specified csv from Redis"""
    cache.delete(name)
    # Update cache which lists all csv items
    if CACHE_ALL_CSVS_KEY in cache:
        all_csvs = cache.get(CACHE_ALL_CSVS_KEY)
        new_csvs = [item for item in all_csvs if item.name != name]
        cache.set(
            CACHE_ALL_CSVS_KEY, 
            new_csvs, 
            timeout=CACHE_LIST_CSVS_TTL
        )


@shared_task()
def remove_local_csv_file_task(filepath):
    """Remove the locally stored copy of the uploaded *.csv file"""
    try:
        os.remove(filepath)
    except OSError:
        pass


@shared_task()
def convert_csv_to_json_task(name):
    """Select csv object by 'name', convert stored 
    csv file into a JSON format and update the object 
    in database and Redis.
    """
    csv_object = CSVData.objects.get(name=name)
    file = csv_object.file
    json_data = dict()
    # Read the CSV file and convert it to a JSON object
    csv_data = csv.DictReader(file.read().decode("utf-8").splitlines())
    json_data = json.dumps([row for row in csv_data])
    # Validate the JSON object
    _ = json.loads(json_data)
    csv_object.json_data = json_data
    csv_object.save()
    cache.set(csv_object.name, [csv_object], timeout=CACHE_SINGLE_CSV_TTL)
    # Update cache which lists all csv items
    if CACHE_ALL_CSVS_KEY in cache:
        all_csvs = list(cache.get(CACHE_ALL_CSVS_KEY))
        is_existing = any(item.name == name for item in all_csvs)
        if not is_existing:
            all_csvs.append(csv_object)
            cache.set(
                CACHE_ALL_CSVS_KEY,
                all_csvs, 
                timeout=CACHE_LIST_CSVS_TTL
            )
