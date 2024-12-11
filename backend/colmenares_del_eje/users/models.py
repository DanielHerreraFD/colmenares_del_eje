from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    assignment_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(max_length=10)
    state = models.CharField(max_length=30)
    emergency_contact = models.CharField(max_length=10)
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('beekeeper', 'Apicultor'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='beekeeper')

class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_login = models.DateTimeField(auto_now_add=True)
    id_User = models.ForeignKey(User, on_delete=models.CASCADE)
