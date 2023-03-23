from .views import *
from rest_framework import routers


router = routers.SimpleRouter()

router.register('linestring', LineStringViewSet, basename='linestring')
router.register('point', PointViewSet, basename='point')
router.register('polygon', PolygonViewSet, basename='polygon')

router.register('upload', FileUploadViewSet, basename='upload')

urlpatterns = router.urls

