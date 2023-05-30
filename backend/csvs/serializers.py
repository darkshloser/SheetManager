from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CSVData


class CSVDataSerializer(serializers.Serializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=CSVData.objects.all())]
    )
    file = serializers.FileField()
    json_data = serializers.JSONField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = CSVData
        fields = ["name", "file", "json_data", "created_at"]


class CSVDataListAllSerializer(CSVDataSerializer):
    json_data = None

    class Meta:
        model = CSVData
        fields = ["name", "file", "created_at"]


class CSVDataEnrichSerializer(serializers.Serializer):
    """
    Custom serializer without model, only for
    validating requests for CSV enrichment.
    """

    name = serializers.CharField(
        required=True,
        allow_blank=False
    )
    additional_api_json = serializers.JSONField(
        required=True,
        allow_null=False
    )
    key_column_stored = serializers.CharField(
        required=True,
        allow_blank=False
    )
    key_column_api = serializers.CharField(
        required=True,
        allow_blank=False
    )
    second_src_key = serializers.CharField(
        required=False,
        allow_blank=True
    )
    second_api_key = serializers.CharField(
        required=False,
        allow_blank=True
    )