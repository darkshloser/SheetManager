from django.conf import settings
from django.core.cache import cache
from .models import CSVData
from .tasks import (
    save_csv_items_in_redis_task,
    delete_csv_from_redis_task,
    remove_local_csv_file_task,
    convert_csv_to_json_task,
)

# if there is no 'CACHE_ALL_CSVS_KEY' specified it will NOT cache 
# the list with all csv items (it will always retrieve data from the database)
CACHE_ALL_CSVS_KEY = getattr(settings, 'CACHE_ALL_CSVS_KEY', None)


def get_selected_csv(csv_name):
    if csv_name in cache:
        csv_item = cache.get(csv_name)
    else:
        csv_item = CSVData.objects.filter(name=csv_name)
        if csv_item:
            save_csv_items_in_redis_task.apply_async(
                [csv_name],
                ignore_result=True
            )
    return csv_item


def get_all_csvs():
    if not CACHE_ALL_CSVS_KEY:
        all_items = CSVData.objects.all()
    elif CACHE_ALL_CSVS_KEY in cache:
        all_items = cache.get(CACHE_ALL_CSVS_KEY)
    else:
        all_items = CSVData.objects.all()
        save_csv_items_in_redis_task.apply_async(
            [CACHE_ALL_CSVS_KEY],
            ignore_result=True
        )
    return all_items


def del_csv_from_redis(csv_name):
    delete_csv_from_redis_task.apply_async(
        [csv_name],
        ignore_result=True
    )


def remove_local_csv_file(filepath):
    remove_local_csv_file_task.apply_async(
        [filepath],
        ignore_result=True
    )


def convert_to_json_field(csv_name):
    convert_csv_to_json_task.apply_async(
        [csv_name],
        ignore_result=True
    )


def update_csv_in_cache(csv_name):
    save_csv_items_in_redis_task.apply_async(
        [csv_name],
        ignore_result=True
    )