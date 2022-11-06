from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import VroomUser, Ride

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
   # /*userCreate = User.objects.create_user('fsmith7','','testpass')
   # userCreate.save()
   # vroomUserCreate = VroomUser(user=userCreate, destination='ThisIsADestination')
   # vroomUserCreate.save()
   # userGet = User.objects.get(username='fsmith7')
   ## destination = userGet.vroomuser.destination
    #print(destination)#
def askInfo(request):
    #if request.method =="POST":
       # driver=request.POST["driver"]
      #  print(rider)
       # print(driver)
      #  print("^driver here^")
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

def assnRider(request):
    return HttpResponseRedirect("/vroomvroom/riders/")

def assnDriver(request):
    return HttpResponseRedirect("/vroomvroom/drivers/")