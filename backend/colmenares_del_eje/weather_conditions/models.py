from django.db import models

# Create your models here.

class weather_conditions(models.Model):
    temperature = models.IntegerField()
    climate_description = models.CharField(max_length=30)
    humidity_indices = models.FloatField()
    wind_pressure = models.CharField(max_length=30)
    chance_of_rain = models.FloatField()