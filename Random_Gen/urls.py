from django.urls import path
from Random_Gen.views import RandomApp
from . import views

urlpatterns = [path('', RandomApp.as_view(), name='rand_init'),
               path('csv/', views.Random_csv, name='rand_csv'),]