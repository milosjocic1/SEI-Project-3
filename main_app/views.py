from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import User, Destination
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView
# from .forms import FeedingForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# HOME PAGE
def home(request):
    return render(request, 'home.html')

# ABOUT PAGE
def about(request):
    return render(request, 'about.html')