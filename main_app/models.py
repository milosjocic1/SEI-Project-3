from nturl2path import url2pathname
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
RATINGS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)
# class User(models.Model)
class Destination(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    currency = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    keywords = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=30, default="")
    rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.created_at}"

    class Meta:
        ordering = ['-created_at']