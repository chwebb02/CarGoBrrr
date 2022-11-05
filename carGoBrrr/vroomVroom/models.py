from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here
class VroomUser(AbstractBaseUser):
    uname = models.CharField(max_length=64)
    phone_number = models.JSONField()
    isActive = models.BooleanField()
    destination = models.CharField(max_length=100)
    current = models.CharField(max_length=100)

class Ride(models.Model):
    destination = models.CharField(max_length=100)
    current = models.CharField(max_length=100)
    time = models.DateTimeField()
    spots = models.PositiveSmallIntegerField()
