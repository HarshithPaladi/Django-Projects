from django.urls import path
from . import views

urlpatterns = [
    path("bookticket", views.bookticket, name="bookticket"),
]
