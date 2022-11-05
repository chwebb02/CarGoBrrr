from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# Login
def login(request):
    return HttpResponse("This is the login page.  It will be replaced with a render.  Someone change this in carGoBrrr/vroomVroom/views.py")

# Session Info
def askInfo(request):
    return HttpResponse("This is the askInfo page.  It will be replaced with a render.  Some change this in carGoBrrr/vroomVroom/views.py")

# Create Account
def createAccount(request):
    return HttpResponse("This is the createAccount page.  It will be replaced with a render.  Some change this in carGoBrrr/vroomVroom/views.py")

# Define account info
def profileInfo(request):
    return HttpResponse("This is the profileInfo page.  It will be replaced with a render.  Some change this in carGoBrrr/vroomVroom/views.py")

# Rider
def riders(request):
    return HttpResponse("This is the riders page.  It will be replaced with a render.  Some change this in carGoBrrr/vroomVroom/views.py")

# Driver
def driver(request):
    return HttpResponse("This is the driver page.  It will be replaced with a render.  Some change this in carGoBrrr/vroomVroom/views.py")

