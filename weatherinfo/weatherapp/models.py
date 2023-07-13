from django.db import models

# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=50)

class Coordinate(models.Model):
    lat=models.TextField()
    long=models.TextField()
