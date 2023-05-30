from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register("file", views.CSVDataUploadView, basename='file')
router.register("enrich", views.CSVDataEnrichView, basename='enrich')
urlpatterns = router.urls
