from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    number_of_pages = models.IntegerField()
    

    def __str__(self):
        return self.title
