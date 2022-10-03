from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination
from .forms import ReviewForm

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

# QUIZ PAGE
def quiz(request):
    return render(request, 'quiz.html')

# DESTINATIONS INDEX
def destinations_index(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations/index.html', {'destinations': destinations})


# DESTINATIONS DETAIL:
def destinations_detail(request, destination_id):
    # SELECT * FROM main_app_cat WHERE id = cat_id
    destination = Destination.objects.get(id = destination_id)
    review_form = ReviewForm()
    return render(request, 'destinations/detail.html', {'destination': destination, 'review_form': review_form})

def add_review(request, destination_id):
    print("add_review")
    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.destination_id = destination_id
        new_review.save()
    return redirect('detail', destination_id = destination_id)