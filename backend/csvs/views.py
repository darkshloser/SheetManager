import os
import uuid
import pandas as pd
from datetime import datetime
from .models import CSVData
from django.conf import settings
from django.core.files import File
from rest_framework import viewsets, status
from rest_framework.response import Response
from .exceptions import (
    MissingCSVFileError,
    CSVMergeError,
    CSVNotSavedError,
)
from .serializers import (
    CSVDataSerializer,
    CSVDataEnrichSerializer,
    CSVDataListAllSerializer,
)
from .services import (
    get_selected_csv,
    get_all_csvs,
    del_csv_from_redis,
    remove_local_csv_file,
    convert_to_json_field,
    update_csv_in_cache,
)



class CSVDataUploadView(viewsets.ModelViewSet):

    queryset = CSVData.objects.all()
    serializer_class = CSVDataSerializer

    http_method_names = ['get', 'post', 'put', 'delete']

    def __csv_file(self, request):
        csv_object = request.FILES.get("file")
        csv_data = pd.read_csv(csv_object.file)
        if not csv_object:
            raise MissingCSVFileError()
        return csv_object

    def create(self, request):
        serializer = CSVDataSerializer(data=request.data)
        if serializer.is_valid():
            try:
                csv_file = self.__csv_file(request)
                new_csvdata_obj = CSVData.objects.create(
                    name=request.data.get("name"), 
                    file=csv_file
                )
                convert_to_json_field(request.data.get("name"))
                serializer = CSVDataSerializer(new_csvdata_obj)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED)
            except MissingCSVFileError as err:
                return Response(
                    {"details": "{err.msg}"},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            except Exception as err:
                return Response(
                    {"details": "Unexpected error"},
                    status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            name = request.query_params.get("name")
            csv_object = get_selected_csv(name)[0]
            del_csv_from_redis(name)
            file_path = csv_object.file.path
            csv_object.delete()
            remove_local_csv_file(file_path)
        except IndexError:
            return Response(
                {"details": f"Specified CSV object {name} does not exist."},
                status=status.HTTP_410_GONE)
        except Exception as err:
            return Response(
                {"details": f"Removal can not be completed for {name}."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(
            {"details": "CSV data deleted successfully."},
            status=status.HTTP_204_NO_CONTENT)

    def put(self, request):
        new_json = request.data.get("json_data")
        name = request.query_params.get("name")
        if not name or not new_json:
            return Response(
                {"details": "Incomplete request"},
                status=status.HTTP_400_BAD_REQUEST)
        try:
            upd_object = get_selected_csv(name)[0]
            f_path = upd_object.file.path
            df = pd.read_json(new_json)
        except:
            return Response(
                {"details": "Unexpected error"}, status=status.HTTP_406_NOT_ACCEPTABLE
            )
        # Save the updated CSV file
        df.to_csv(f_path, index=False)
        upd_object.json_data = new_json
        upd_object.save()
        update_csv_in_cache(name)
        serializer = CSVDataSerializer(upd_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        name = request.query_params.get("name")
        if name:
            queryset = get_selected_csv(name)
            serializer = CSVDataSerializer(queryset, many=True)
        else:
            queryset = get_all_csvs()
            serializer = CSVDataListAllSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CSVDataEnrichView(CSVDataUploadView):

    http_method_names = ["post"]

    def __generate_unique_name(self, name):
        now = datetime.now()
        new_name = name + now.strftime("_%d_%m_%Y-%H_%M_%S")
        new_obj_exists = CSVData.objects.filter(name=new_name)
        if new_obj_exists:
            return str(uuid.uuid4())
        return new_name

    def __merge_jsons_by_key(
        self,
        stored_json,
        api_json,
        stored_key,
        api_key,
        sec_src_key,
        sec_api_key
    ):
        src_keys = []
        api_keys = []
        try:
            src_keys.append(stored_key)
            api_keys.append(api_key)
            if sec_src_key: src_keys.append(sec_src_key)
            if sec_api_key: api_keys.append(sec_api_key)
            df_stored = pd.read_json(stored_json)
            df_api = pd.read_json(api_json)
            df_merged = pd.merge(
                df_stored, df_api, how='left', left_on=src_keys, right_on=api_keys
            )
        except Exception:
            raise CSVMergeError()
        return df_merged

    def __store_csv(self, data_frame, file_path):
        try:
            data_frame.to_csv(file_path, index=False)
        except:
            if os.path.isfile(file_path):
                os.remove(file_path)
            raise CSVNotSavedError()

    def create(self, request):
        serializer = CSVDataEnrichSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get("name")
            api_json = request.data.get("additional_api_json")
            key_col_stored = request.data.get("key_column_stored")
            key_col_api = request.data.get("key_column_api")
            second_src_key = request.data.get("second_src_key")
            second_api_key = request.data.get("second_api_key")
            try:
                csv_object = CSVData.objects.get(name=name)
                new_name = self.__generate_unique_name(name=name)
                df_merged = self.__merge_jsons_by_key(
                    stored_json=csv_object.json_data,
                    api_json=api_json,
                    stored_key=key_col_stored,
                    api_key=key_col_api,
                    sec_src_key=second_src_key,
                    sec_api_key=second_api_key
                )
                new_json = df_merged.to_json(orient="records")
                # Save the merged CSV file
                file_path = os.path.join(settings.CSV_DIR, new_name + ".csv")
                self.__store_csv(data_frame=df_merged, file_path=file_path)
                new_csvdata_obj = CSVData.objects.create(
                    name=new_name, json_data=new_json
                )
                new_csvdata_obj.file.name = file_path
                new_csvdata_obj.save()
                update_csv_in_cache(new_name)
                serializer = CSVDataSerializer(new_csvdata_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except CSVData.DoesNotExist:
                return Response(
                    {"details": "Specified CSV object {name} does not exist."},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
            except (CSVMergeError, CSVNotSavedError) as err:
                pass
            except Exception:
                return Response(
                    {"details": "Error during *.csv "},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)