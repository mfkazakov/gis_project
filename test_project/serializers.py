from rest_framework.serializers import SlugRelatedField, Serializer, FileField, CharField, ValidationError, StringRelatedField
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeoModelSerializer
from .models import Polygon, LineString, Point


class LineStringSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = LineString
        geo_field = "geometry"
        id_field = False
        fields = ['geometry', 'id', 'name']


class PointSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Point
        geo_field = 'geometry'
        id_field = False
        fields = ['geometry', 'id', 'name']


class PointListSerializer(GeoModelSerializer):

    class Meta:
        model = Point
        geo_field = 'geometry'
        # id_field = False
        fields = ['name', 'geometry',]


class PolygonSerializer(GeoFeatureModelSerializer):

    points = StringRelatedField(
        many=True,
    )

    class Meta:
        model = Polygon
        geo_field = "geometry"
        id_field = False
        fields = ['geometry', 'id', 'name', 'points']


class PolygonListSerializer(GeoModelSerializer):

    points = StringRelatedField(
        many=True,
    )

    class Meta:
        model = Polygon
        geo_field = "geometry"
        id_field = False
        fields = ['geometry', 'id', 'name', 'points']


class FileUploadSerializer(Serializer):
    name = CharField(allow_null=True)
    geom_type = CharField()
    file_upload = FileField()

    def validate(self, data):
        if str(data['file_upload'])[-4:] != '.gpx':
            raise ValidationError("Wrong file format")

        if data['geom_type'] not in ('Polygon', 'LineString', 'MultiPoint'):
            raise ValidationError("Wrong geom_type")
        return data

    class Meta:
        fields = ['name', 'geom_type', 'file_upload']

