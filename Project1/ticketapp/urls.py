from django.urls import path
from . import views
urlpatterns = [
    path('', views.ticket, name='ticket_in'),
]
