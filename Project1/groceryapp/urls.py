from django.urls import path
from . import views
urlpatterns = [
    path('', views.grocery, name='grocery'),
    path('view/', views.view, name='groceries'),
]
