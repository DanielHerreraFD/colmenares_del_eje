from django.db import models
from weather_conditions.models import weather_conditions

# Create your models here.

class Beehive(models.Model):
    registration_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30)
    open_brood_frames = models.IntegerField()
    capped_brood_frames = models.IntegerField()
    queen_presence = models.BooleanField()
    queen_color = models.CharField(max_length=15)
    origin = models.CharField(max_length=20)
    food_frames = models.IntegerField()
    observations = models.CharField(max_length=90)
    qr_code = models.CharField(max_length=200)
    id_weather_conditions = models.ForeignKey(weather_conditions, on_delete=models.CASCADE)
    status = models.CharField(max_length=30)
