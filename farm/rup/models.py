from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    lat = models.TextField(null=True)
    lng = models.TextField(null=True)
    company_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

class Pesticide(models.Model):
    registrant_name = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=200)
    epa_number = models.CharField(max_length=50)
    active_ingredient = models.CharField(max_length=100, blank=True)
    rui = models.TextField()
    rei = models.DateTimeField(null=True, blank=True)
    use = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.product_name

class Formulation(models.Model):
    pesticide = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    rate = models.FloatField(null=True)

    def __str__(self):
        return self.pesticide.product_name

class Name(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    license_no = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name

class Location(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    polyname = models.CharField(max_length=200, null=True)
    rectBounds = models.TextField(null=True)
    polyList = models.TextField(null=True)
    rectBounds = models.TextField(null=True)
    newLat = models.CharField(max_length=50, null=True)
    newLng = models.CharField(max_length=50, null=True)
    areaRect = models.CharField(max_length=50, null=True)
    areaPoly = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.polyname

    def is_restricted(self):
        now = timezone.now()
        if self.locationpesticide_set.filter(start__lte=now, end__gte=now).exists():
            return True
        return False

class Center(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '( ' + str(self.lat) + ', ' + str(self.lng) + ' )'


class LocationPesticide(models.Model):
    """Many locations or pesticides, one LocationPesticide event"""
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    formulation = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    rate = models.CharField(null=True, max_length=50)
    target = models.CharField(null=True, max_length=50)
    applicator = models.CharField(null=True, max_length=50)


    def __str__(self):
        return self.location.name + ' ' + self.pesticide.product_name
