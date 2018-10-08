from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cars(models.Model):
    road_name=models.CharField(max_length=20)
    cartype=models.CharField(max_length=10)
    roadNumber=models.CharField(max_length=25)

class Locomotives(models.Model):
    road_name=models.CharField(max_length=20)
    cartype=models.CharField(max_length=10)
    roadNumber=models.CharField(max_length=25)