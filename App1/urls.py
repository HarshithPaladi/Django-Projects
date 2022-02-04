import imp
from tkinter import image_names
from django.urls import path
from . import views

# URL Configs
urlpatterns = [
    path("hello/",views.say_hello)
    ]