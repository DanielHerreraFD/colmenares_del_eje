from django.db import models
from users.models import User
from hive_management.models import Beehive

# Create your models here.
class Monitoring(models.Model):
    monitoring_date = models.DateTimeField()
    queen_observations = models.CharField(max_length=50)
    food_observations = models.CharField(max_length=50)
    general_observations = models.CharField(max_length=90)
    beekeeper = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'beekeeper'})
    hive_id = models.ForeignKey(Beehive, on_delete=models.CASCADE)