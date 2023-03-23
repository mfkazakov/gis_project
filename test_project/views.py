from .serializers import (
    PolygonSerializer,
    LineStringSerializer,
    PointSerializer,
    FileUploadSerializer
)
from rest_framework import viewsets, filters, status
from rest_framework_gis.filters import DistanceToPointFilter
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from django_filters.rest_framework import DjangoFilterBackend

from .models import Polygon, LineString, Point
from .myMixins import CreateListModelMixin
from .services.actions_with_gpx_file import PolygonItemFromFile, PointItemsFromFile, LineStringItemFromFile


class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', ]
    search_fields = ['name']


class PointViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', ]
    search_fields = ['name']


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    distance_filter_field = 'geometry'
    distance_filter_convert_meters = True

    filter_backends = [DistanceToPointFilter, DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', ]
    search_fields = ['name']


class FileUploadViewSet(CreateModelMixin, viewsets.ViewSet):
    serializer_class = FileUploadSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.data.get('name')
        geom_type = serializer.data.get('geom_type')
        file_uploaded = request.FILES.get('file_upload')

        if geom_type == 'Polygon':
            serializer = PolygonSerializer(data=PolygonItemFromFile(file_uploaded).get_geometry_item())
        elif geom_type == 'LineString':
            serializer = LineStringSerializer(data=LineStringItemFromFile(file_uploaded).get_geometry_item())
        elif geom_type == 'MultiPoint':
            serializer = PointSerializer(data=PointItemsFromFile(file_uploaded, name=name).get_geometry_item(),
                                         many=True)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

