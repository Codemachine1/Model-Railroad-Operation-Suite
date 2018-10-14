from __future__ import unicode_literals

from django.db import models

# Create your models here.
class station(models.Model):
    milePost=models.IntegerField()
    name=models.CharField(max_length=300)

class siding(models.Model):
    station=models.ForeignKey(station,
    on_delete=models.CASCADE)
    milePost=models.IntegerField()
    name=models.CharField(max_length=300)

class yard(models.Model):
    station=models.ForeignKey(station,
    on_delete=models.CASCADE)
    milePost=models.IntegerField()
    name=models.CharField(max_length=300)
