from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import VroomUser, Ride

from django.contrib.auth.models import User

# Create your views here
# Login page
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # process the data in form.cleaned_data as required
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("../info/")
        # Else: error message?
    return render(request, "../design/login/login.html")


# Session Info
def askInfo(request):
    return render(request, "../design/askInfo/askInfo.html")


# Create Account
def createAccount(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        compPassword = request.POST["compPassword"]

        if password == compPassword:
            userCreate = User.objects.create_user(username, '', password)
            userCreate.save()

            vroomUserCreate = VroomUser(user=userCreate)
            vroomUserCreate.save()
            
            login(request, userCreate)
            return HttpResponseRedirect("../profileInfo/")

    return render(request, "../design/createLogin/createLoginInfo/createLoginInfo.html")


# Define account info
def profileInfo(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]

        request.user.vroomuser.name = name
        request.user.vroomuser.phone_number = phone_number
        request.user.vroomuser.save()

        return HttpResponseRedirect("../info")

    return render(request, "../design/createLogin/profileInfo/profileInfo.html")


# Rider
def riders(request):
    return render(request, "../design/rider/rider.html")


# Driver
def drivers(request):
    return render(request, "../design/driver/driverMain.html")


# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../")
