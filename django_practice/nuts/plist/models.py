from django.db import models

class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
class plist(models.Model):
    nut = models.CharField(max_length=100)
    price_per_kilo = models.FloatField(default = 0)
    dry_fruit = models.CharField(max_length=100)
    price_per_kg = models.FloatField(default=0)
    
# Create your models here.
