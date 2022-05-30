from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)

class AreaCode(models.Model):
    code = models.IntegerField(primary_key=True)
    location = models.ForeignKey(Location, models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    location = models.ForeignKey(Location, models.CASCADE)
