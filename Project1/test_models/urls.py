from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_models, name='test_models'),
    path("users/", views.test_users, name="test_users"),
    path("forms/", views.test_forms, name="test_forms"),
]
