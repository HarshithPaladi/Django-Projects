from django.db import models

class Dept(models.Model):
    name = models.CharField(max_length=120) 
    code =  models.CharField(max_length=4)

class Student(models.Model):
    name = models.CharField(max_length=120)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length=200) 
    code = models.CharField(max_length=7)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)

class Teacher(models.Model):
    name = models.CharField(max_length=120)
    dept =  models.ForeignKey(Dept, on_delete=models.CASCADE)

class course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    