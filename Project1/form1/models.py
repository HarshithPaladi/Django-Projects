from django.db import models
from django.core import validators
# Create your models here.
class Form1(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True,validators=[validators.validate_email])
    age = models.IntegerField(validators=[validators.MaxValueValidator(150),validators.MinValueValidator(0)])

    def __str__(self) -> str:
        return self.name