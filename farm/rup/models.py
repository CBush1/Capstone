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

    def __str__(self):
        return self.first_name

class Applicator(models.Model):
    applicator_name = models.ForeignKey(Name, on_delete=models.CASCADE)
    date_applied = models.DateTimeField()
    location_applied = models.TextField()

    def __str__(self):
        return self.applicator_name


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

class LocationPesticide(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pesticide = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location.name + ' ' + self.pesticide.product_name
