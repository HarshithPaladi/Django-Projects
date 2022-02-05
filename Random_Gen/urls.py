from django.urls import path
from . import views

urlpatterns = [path('', views.Random_gen, name='rand_init'),
               path('csv/', views.Random_csv, name='rand_csv'),]