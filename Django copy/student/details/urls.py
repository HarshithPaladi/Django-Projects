from distutils.log import error
import re
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name= "index")
]