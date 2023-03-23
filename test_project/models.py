from django.contrib.gis.db import models


class Point(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    geometry = models.PointField(verbose_name='Поле геометрии')

    def __str__(self):
        return self.name


class Polygon(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    geometry = models.PolygonField(verbose_name='Поле геометрии')
    points = models.ManyToManyField(Point, verbose_name='Точки', blank=True)

    def __str__(self):
        return self.name


class LineString(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    geometry = models.LineStringField(verbose_name='Поле геометрии')

    def __str__(self):
        return self.name

