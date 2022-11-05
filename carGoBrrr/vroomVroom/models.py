from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here
class VroomUser(AbstractBaseUser):
    phone_number = models.JSONField()
    isActive = models.BooleanField()
    destination = models.charField(max_length=100)
    current = models.charField(max_length=100)

class Rides(models.Model):
    destination = models.charField(max_length=100)
    current = models.charField(max_length=100)
    time = models.DateTimeField()
    spots = models.PositiveSmallIntegerField()
