from nturl2path import url2pathname
# from tkinter import Widget
from unittest.util import _MAX_LENGTH
from django.db import models
from django import forms
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.db.models import Avg, Count

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
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name

        class Meta:
            verbose_name_plural = 'cities'

    # AVERAGE REVIEWS AND COUNT:
    def averageReview(self):
        reviews = Review.objects.filter(destination=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = int(reviews['average'])
        return avg

    def countReview(self):
        reviews = Review.objects.filter(destination=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count
    # END OF AVERAGE REVIEWS AND COUNT

    # START OF WEATHER API

    # END OF WEATHER API

    def get_absolute_url(self):
        return reverse('destinations_detail', kwargs={'pk': self.id})



class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=30, default="")
    rating = models.FloatField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} on {self.created_at}"

    class Meta:
        ordering = ['-created_at']


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


