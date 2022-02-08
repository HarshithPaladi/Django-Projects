from django.urls import path
from . import views

# URL Configs
urlpatterns = [path("", views.home, name="add_home"),
               path("add", views.add, name="add_num"),]