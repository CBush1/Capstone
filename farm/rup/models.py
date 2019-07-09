from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Pesticide(models.Model):
    product_name = models.CharField(max_length=200)
    epa_number = models.CharField(max_length=50)
    rui = models.TextField()
    rei = models.DateTimeField(null=True, blank=True)
    use = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.product_name

class Name(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_no = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name

class Location(models.Model):
    name = models.CharField(max_length=200)
    verticies = models.TextField()

    def __str__(self):
        return self.name

    def is_restricted(self):
        now = timezone.now()
        if self.locationpesticide_set.filter(start__lte=now, end__gte=now).exists():
            return True
        return False

class UserLocation(models.Model):
    polyname = models.CharField(max_length=200)
    rectBounds = models.TextField()
    polyList = models.TextField()
    rectBounds = models.TextField()
    newLat = models.CharField(max_length=50)
    newLng = models.CharField(max_length=50)
    areaRect = models.CharField(max_length=50)
    areaPoly = models.CharField(max_length=50)

    def __str__(self):
        return self.polyname

class Center(models.Model):
    timestamp = models.DateTimeField(null=True, blank=True)
    lat = models.TextField(null=True)
    lng = models.TextField(null=True)

    def __str__(self):
        return self.timestamp


class LocationPesticide(models.Model):
    """Many locations or pesticides, one LocationPesticide event"""
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pesticide = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.CharField(null=True, max_length=50)
    target = models.CharField(null=True, max_length=50)
    applicator = models.CharField(null=True, max_length=50)


    def __str__(self):
        return self.location.name + ' ' + self.pesticide.product_name
