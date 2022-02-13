from django.db import models

# Create your models here.
class Grocery(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=[('oil', 'oil'), ('grains', "Grains"),('Cosmetics', 'Cosmetics')],default='oil')
    quantity = models.IntegerField()
    price_peritem = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name