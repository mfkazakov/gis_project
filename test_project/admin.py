from django.contrib import admin
from .models import Polygon, LineString, Point


admin.site.register(Polygon)
admin.site.register(LineString)
admin.site.register(Point)
