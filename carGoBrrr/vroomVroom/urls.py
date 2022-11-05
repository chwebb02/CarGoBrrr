from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.index, name="index"),
    path("info/", views.askInfo, name="info"),
    path("createAccount/", views.createAccount, name="createAccount"),
    path("profileInfo/", views.profileInfo, name="profileInfo"),
    path("riders/", views.riders, name="riders"),
    path("drivers/", views.drivers, name="drivers"),
    path("logout/", views.logout, name="logout")
]
