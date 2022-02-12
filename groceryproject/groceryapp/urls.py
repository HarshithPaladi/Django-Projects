from django.urls import path
from . import views

urlpatterns = [
    path("buy/", views.buy),
    path("records/", views.records),
]
