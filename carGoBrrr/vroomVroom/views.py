from django.shortcuts import render
from django.http import HttpResponse


from .models import VroomUser, Ride

# Create your views here
# Login page
def index(request):
    return render(request, '../design/login/login.html')

# Session Info
def askInfo(request):
    return render(request, '../design/askInfo/askInfo.html')

# Create Account
def createAccount(request):
    return render(request, '../design/createLogin/createLoginInfo/createLoginInfo.html')

# Define account info
def profileInfo(request):
    return render(request, '../design/createLogin/profileInfo/profileInfo.html')

# Rider
def riders(request):
    return render(request, '../design/rider/rider.html')

# Driver
def drivers(request):
    return render(request, '../design/driver/driverMain.html')