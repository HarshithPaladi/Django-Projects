from django.db import models

# Create your models here.
class Fibonacci(models.Model):
    numstr = models.IntegerField()
    terms = models.CharField(max_length=1000)

    def __str__(self):
        return "The First {} terms of Fibonacci are: {}".format(self.numstr, self.terms)
