from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

class stud_record(models.Model):
    name = models.CharField(max_length=100)
    register_no = models.IntegerField()
    mark_1 = models.IntegerField()
    grade_1 = models.CharField(max_length=1)
    mark_2 = models.IntegerField()
    grade_2 = models.CharField(max_length=1)
    mark_3 = models.IntegerField()
    grade_3 = models.CharField(max_length=1)