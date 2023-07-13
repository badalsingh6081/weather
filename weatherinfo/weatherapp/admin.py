from django.contrib import admin
from .models import City,Coordinate
# Register your models here.

@admin.register(City)
class CityAmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Coordinate)
class CoordinateAmin(admin.ModelAdmin):
    list_display=['id','lat','long']