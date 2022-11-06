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
    hour = models.IntegerField()
    hour.default = 0
    minute = models.IntegerField()
    minute.default = 1
    day = models.IntegerField()
    day.default = 1
    month = models.IntegerField()
    month.default = 1
    year = models.IntegerField()
    year.default = 1970
    driver = models.ForeignKey(VroomUser, on_delete=models.CASCADE)
    driver.default = None