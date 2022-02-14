from django.urls import path
from . import views

urlpatterns = [
    path("num/", views.num, name="num"),
    path("list/", views.fibo_archive, name="fibo_archive"),
]
