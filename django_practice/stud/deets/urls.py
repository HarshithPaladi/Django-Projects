from distutils.log import error
import re
from unittest import result
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index , name= "index"),
    path('grade', views.results, name="results" )
    
]