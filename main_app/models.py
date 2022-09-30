from nturl2path import url2pathname
from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})
