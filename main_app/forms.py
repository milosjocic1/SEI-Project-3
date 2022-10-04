from django.forms import ModelForm
<<<<<<< HEAD
from django import forms
from django.contrib.auth.models import User
from .models import RATINGS, Review, Rating, Profile
=======

from .models import Review
>>>>>>> 08e8ce99ecaa182155765a5b37ec3da330a427a1

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

