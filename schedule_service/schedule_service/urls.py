"""
URL configuration for schedule_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from schedule.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AirportInsertandGettingall/',AirportInsertandGettingall.as_view(),name="AirportInsertandGettingall"),
    path('updateAndDeleteAndRetraiveByID/<int:pk>/',updateAndDeleteAndRetraiveByID.as_view(),name="updateAndDeleteAndRetraiveByID"),
    path('FlightInsertandGettingall/',FlightInsertandGettingall.as_view(),name="FlightInsertandGettingall"),
    path('FlightupdateAndDeleteAndRetraiveByID/<int:pk>/',FlightupdateAndDeleteAndRetraiveByID.as_view(),name="FlightupdateAndDeleteAndRetraiveByID"),
    path('inserting/', inserting,name='inserting'),
    path('gettingData/', gettingData,name='gettingData'),
    path('getById/<int:id>/', getById,name='getById'),
    path('updateSchedule/<int:id>/',updateSchedule ,name='updateSchedule'),
    path('deleteSchedule/<int:id>/', deleteSchedule,name='deleteSchedule'),

]
