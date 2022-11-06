from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.index, name="index"),
    path("info/", views.askInfo, name="info"),
    path("createAccount/", views.createAccount, name="createAccount"),
    path("profileInfo/", views.profileInfo, name="profileInfo"),
    path("riders/", views.riders, name="riders"),
    path("riderLocation/", views.riderLocation, name="rider_location"),
    path("drivers/", views.drivers, name="drivers"),
    path("logout/", views.logout_view, name="logout"),
    path("assnriders/", views.assnRider, name="assign_riders"),
    path("assndrivers/", views.assnDriver, name="assign_drivers"),
    path("createASchedule/", views.createASchedule, name="create_a_schedule"),
    path("", views.index, name="index")
]
