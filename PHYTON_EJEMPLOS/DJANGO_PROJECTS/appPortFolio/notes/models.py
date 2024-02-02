from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    content2 = models.TextField(default="test")

    
    def __str__(self):
        return self.title