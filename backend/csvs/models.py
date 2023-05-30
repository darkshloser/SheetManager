from django.db import models
from django.conf import settings


class CSVData(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True, 
        blank=False,
        null=False
    )
    file = models.FileField(
        upload_to=settings.CSV_DIR,
        blank=False,
        null=False
    )
    json_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = "CSV Data"