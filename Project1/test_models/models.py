from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)
    def __str__(self):
        return self.name
    

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class User(models.Model):
    # first name, last name, email
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique=True)
    
    def __str__(self):
        return self.first_name

class NewModel(models.Model):
    name = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=264,unique=True)
    text = models.CharField(max_length=264)
    def __str__(self):
        return self.name
