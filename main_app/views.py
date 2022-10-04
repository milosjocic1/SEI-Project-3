from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Destination, Rating, Review
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# PAGINATION
from django.core.paginator import Paginator

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
    # PAGINATION
    p = Paginator(Destination.objects.all(), 15)
    page = request.GET.get('page')
    dest = p.get_page(page)

    return render(request, 'destinations/index.html', {'dest': dest, 'destinations': destinations})


# DESTINATIONS DETAIL:
def destinations_detail(request, destination_id):
    # SELECT * FROM main_app_cat WHERE id = cat_id
    destination = Destination.objects.get(id = destination_id)
    review_form = ReviewForm()
    return render(request, 'destinations/detail.html', {'destination': destination, 'review_form': review_form})

def add_review(request, destination_id, user_id):
    print("add_review")
    form = ReviewForm(request.POST)

    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.destination_id = destination_id
        new_review.user_id = user_id
        new_review.save()
    return redirect('detail', destination_id = destination_id)

def add_rating(request, destination_id, user_id):
    print("add_rating")

    form = Rating(request.POST)
    if form.is_valid():
        new_rating = form.save(commit=False)
        new_rating.destination_id = destination_id
        new_rating.user_id = user_id
        new_rating.save()
    return redirect('detail', destination_id = destination_id)

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid signup - please try again later"

    # GET
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)