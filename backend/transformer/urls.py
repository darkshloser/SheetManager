from django.urls import include, path
from django.http import HttpResponse
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view


def healthcheck(request):
    from django.db import connection
    from .celery import app
    import json

    status = {}
    try:
        tables = connection.introspection.table_names()
        status["DB"] = f"ok, tables: {', '.join(tables)}"
    except Exception as e:
        status["DB"] = f"error, {e}"

    try:
        celery_status = app.control.broadcast('ping', reply=True, limit=1)
        tasks = list(app.control.inspect().registered_tasks().values())[0]
        status["CELERY"] = f"ok, tasks: {', '.join(tasks)}" if celery_status else "error"
    except Exception as e:
        status["CELERY"] = f"error, {e}"

    return HttpResponse(json.dumps(status), content_type='application/json')


urlpatterns = [
    path(settings.API_VERSION, include("csvs.urls")),
    path("admin/", admin.site.urls),
    path(
        "schema/",
        get_schema_view(
            title=settings.API_DOC_TITLE,
            description=settings.API_DOC_DESCRIPTION
        ),
        name="openapi-schema",
    ),
    path('healthcheck/', healthcheck),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)