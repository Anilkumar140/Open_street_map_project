from django.db import models

# Create your models here.

class my_cities(models.Model):
    city_name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.city_name
        
class my_latlong(models.Model):
    lattitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    city = models.ForeignKey(my_cities, on_delete=models.CASCADE)
