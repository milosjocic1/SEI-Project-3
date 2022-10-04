from django.forms import ModelForm

from .models import RATINGS, Review, Rating

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        ratings = Rating

