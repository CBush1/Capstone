from django.db import models
from django.contrib.auth.models import User


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

    def is_restricted(self):
        import datetime
        now = datetime.now()
        if LocationPesticide.start < now.strftime("%Y-%m-%d %I:%M") and LocationPesticide.end > now.strftime("%Y-%m-%d %I:%M"):
            return "Restriced"
        # check if there exists a locationpesticide that the current date files within
        else:
            return "Unrestricted"
        pass

    def __str__(self):
        return self.name

class LocationPesticide(models.Model):
    name = models.ManyToManyField(Location)
    pesticide_id = models.ForeignKey(Pesticide, on_delete=models.CASCADE)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
