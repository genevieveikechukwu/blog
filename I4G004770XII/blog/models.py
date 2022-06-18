from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.CharField(max_length=200)
    created_date = models.DateTimeField
    published_date = models.DateTimeField