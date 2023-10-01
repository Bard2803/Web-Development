from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.AutoField(primary_key=True)

class Exercises(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)