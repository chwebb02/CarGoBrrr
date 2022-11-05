from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.askInfo, name='info'),
    path('', views.createAccount, name='createAccount'),
    path('', views.profileInfo, name='profileInfo'),
    path('', views.riders, name='riders'),
    path('', views.drivers, name='drivers'),
]