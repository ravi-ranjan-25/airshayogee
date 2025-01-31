"""sih2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from airline import views
from rest_framework import routers
from .views import findFlights
# from .views import ListView


urlpatterns = [
# path('/user', , name = "userConsumptionN"),
    path('addairline',views.addAirline , name = "addairline"),
    path('addprice',views.addPrice , name = "addprice"),
    path('findflights',views.findFlights , name = "addprie"),
    path('booking',views.orderCallBack , name = "booking"),
    path('show',views.showorders , name = "booking"),

]
