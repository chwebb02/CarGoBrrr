from django.db import models
from django.contrib.auth.models import User

# Create your models here
class VroomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user.default = None
    name = models.CharField(max_length=64)
    name.default = ''
    phone_number = models.JSONField()
    phone_number.default = list
    isActive = models.BooleanField()
    isActive.default = False
    destination = models.CharField(max_length=100)
    destination.default = ''
    current = models.CharField(max_length=100)
    current.default = ''
    isDriver = models.BooleanField()
    isDriver.default = False

class Ride(models.Model):
    destination = models.CharField(max_length=100)
    current = models.CharField(max_length=100)
    time = models.FloatField()
    hour = models.FloatField()
    hour.default = 0
    minute = models.FloatField()
    minute.default = 1
    day = models.FloatField()
    day.default = 1
    month = models.FloatField()
    month.default = 1
    year = models.FloatField()
    year.default = 1970
    driver = models.ForeignKey(VroomUser, on_delete=models.CASCADE)
    driver.default = None