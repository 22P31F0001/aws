from django.db import models

# Create your models here.
class Bikeorders(models.Model):
        Bike_name = models.CharField(max_length=200 )
        color = models.CharField(max_length=200 )
        cus_name = models.CharField(max_length=200 )
        email=models.EmailField(primary_key=True)
        phone=models.CharField(max_length=50, default='SOME STRING')