from django.urls import path
from . import views
urlpatterns = [
    path('', views.forms, name='form1_in'),
    path('data/', views.forms_data, name='form1_out'),
]
