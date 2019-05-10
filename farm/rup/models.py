from django.db import models

# Create your models here.
# class Name(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.first_name



class Pesticide(models.Model):
    product_name = models.CharField(max_length=200)
    epa_number = models.CharField(max_length=50)
    rui = models.TextField()
    rei = models.DateTimeField(null=True, blank=True)
    use = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.product_name

class Name(models.Model):
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
