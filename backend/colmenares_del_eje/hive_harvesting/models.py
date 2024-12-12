from django.db import models
from users.models import User
from hive_management.models import Beehive

# Create your models here.

class harvesting(models.Model):
    harvest_date = models.DateField()
    honey_production = models.FloatField()
    pollen_production = models.FloatField()
    hive_id = models.ForeignKey(Beehive, on_delete=models.CASCADE)
    beekeeper = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'beekeeper'})