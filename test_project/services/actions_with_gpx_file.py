import gpxpy.gpx
from dataclasses import dataclass
import abc
from rest_framework.serializers import ValidationError


@dataclass
class ParseResult:
    name: str
    points: list

    def __str__(self):
        return f'ParseResult(name - {self.name}, points - {self.points})'


class DefaultParserFile:
    """Cтандартный парсер gpx файла, точки находятся в points<-segments<-tracks"""
    def __init__(self, file):
        self.file = file

    def parse_file(self):

        try:
            gpx = gpxpy.parse(self.file)
        except Exception as e:
            raise ValidationError(str(e))

        name = ''
        points = []
        for track in gpx.tracks:
            name = track.name
            for segment in track.segments:
                for point in segment.points:
                    points.append([point.latitude, point.longitude])

        return ParseResult(
            name=name,
            points=points,
        )


class GeometryItemFromFile(abc.ABC):
    def __init__(self, file, name=None):
        self.parser = DefaultParserFile
        self.file = file
        if name is None:
            self.name = 'default_name_point'
        else:
            self.name = name

    @abc.abstractmethod
    def get_geometry_item(self):
        pass


class PolygonItemFromFile(GeometryItemFromFile):
    """Polygon из файла"""
    def get_geometry_item(self) -> dict:
        """Приведение Polygon из ParseResult в geojson"""
        data = self.parser(self.file).parse_file()
        format_data = {
            'name': data.name,
            'geometry': {
                'type': 'Polygon',
                'coordinates': [data.points, ]
            }
        }
        return format_data


class LineStringItemFromFile(GeometryItemFromFile):
    """LineString из файла"""
    def get_geometry_item(self) -> dict:
        """Приведение LineString из ParseResult в geojson"""
        data = self.parser(self.file).parse_file()
        format_data = {
            'name': data.name,
            'geometry': {
                'type': 'LineString',
                'coordinates': data.points
            }
        }
        return format_data


class PointItemsFromFile(GeometryItemFromFile):
    """Points из файла"""
    def get_geometry_item(self) -> list:
        """Приведение Points из ParseResult в geojson"""
        data = self.parser(self.file).parse_file()
        format_data = list()
        for i, point in enumerate(data.points):
            format_data.append({
                'name': self.name + str(i),
                'geometry': {
                    'type': 'Point',
                    'coordinates': point
                }
            })
        return format_data

