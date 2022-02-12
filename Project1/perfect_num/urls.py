from django.urls import path
from . import views
urlpatterns = [
    path('', views.choose, name='choose'),
    path('divisors/', views.perfect_num, name='perfect_num'),
    path('num_stats/', views.num_stats, name='num_stats'),
]
