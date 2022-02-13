from django.db import models

ch = [("Vegetable", "Vegetable"), ("Fruit", "Fruit"), ("Nuts", "Nuts")]
# Create your models here.
class fooditem(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=ch, default="Vegetable")
    VitaminPresent = models.CharField(max_length=100)

    def __str__(self):
        return self.name
