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

        # check for duplicates
        isDuplicate = False
        for i in VroomUser.objects.all():
            if username == i.user.username:
                isDuplicate = True

        # Create a new acccount
        if password == compPassword and not isDuplicate:
            userCreate = User.objects.create_user(username, "", password)
            userCreate.save()

            vroomUserCreate = VroomUser(user=userCreate)
            vroomUserCreate.save()

            login(request, userCreate)
            return HttpResponseRedirect("../profileInfo/")

    return render(request, "../design/createLogin/createLoginInfo/createLoginInfo.html")
# UNIQUE USER BLOCKER!


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
    all_rides = Ride.objects.all()

    return render(request, "../design/rider/rider.html", {'all_rides': all_rides})


# Rider Location (this is where the Ted Bundy-ing begins)
def riderLocation(request):
    if request.method == "POST":
        destination = request.POST["destination"]
        current = request.POST["current"]

        request.user.vroomuser.destination = destination
        request.user.vroomuser.current = current
        request.user.vroomuser.save()

        return HttpResponseRedirect("../riders/")

    return render(request, "../design/askInfo/riderLocation/riderLocation.html")


# Driver
def drivers(request):
    all_rides = Ride.objects.all()

    return render(request, "../design/driver/driverMain.html", {'all_rides': all_rides, 'user':request.user.vroomuser})


# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("../")


# Assign user to rider and return rider main to html
def assnRider(request):
    request.user.vroomuser.isDriver = False
    request.user.vroomuser.save()

    return HttpResponseRedirect("../riderLocation/")


# Assign user to driver and return driver main html
def assnDriver(request):
    request.user.vroomuser.isDriver = True
    request.user.vroomuser.save()

    return HttpResponseRedirect("../drivers/")

# createASchedule
def createASchedule(request):
    if request.method == "POST":
        time = request.POST["time"]
        destination = request.POST["destination"]
        current = request.POST["locationFrom"]

        ride_create = Ride(time=time, destination=destination, current=current, driver=request.user.vroomuser)
        ride_create.save()

        return HttpResponseRedirect("../drivers/")
    
    return render(request, "../design/driver/createSchedule/createSchedule.html")