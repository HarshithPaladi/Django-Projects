from django.urls import path,include
from . import views
from .admin import admin_site
urlpatterns = [
    path('', views.forms, name='login'),
    path('login/',include('django.contrib.auth.urls')),
    path('forms/', views.forms_data, name='forms'),
    path('myadmin/',admin_site.urls),
    path('logout/', admin_site.logout, name='logout'),
]
