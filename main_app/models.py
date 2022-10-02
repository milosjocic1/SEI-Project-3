from nturl2path import url2pathname
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

# class User(models.Model)
class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    keywords = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})
