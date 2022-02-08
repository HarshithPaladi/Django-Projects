from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = [('-timestamp'),]
    def __str__(self):
        return self.title + ', ' + self.body + ', ' + str(self.timestamp)
