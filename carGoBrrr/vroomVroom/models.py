from django.db import models
from django.contrib.auth.models import User

# Create your models here
class VroomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.default = None
    phone_number = models.JSONField()
    phone_number.default = list
    isActive = models.BooleanField()
    isActive.default = False
    destination = models.CharField(max_length=100)
    destination.default = ''
    current = models.CharField(max_length=100)
    current.default = ''

class Ride(models.Model):
    destination = models.CharField(max_length=100)
    current = models.CharField(max_length=100)
    time = models.DateTimeField()
    spots = models.PositiveSmallIntegerField()
