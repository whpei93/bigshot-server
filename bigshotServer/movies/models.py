from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.CharField(max_length=200)
    title    = models.CharField(max_length=200)