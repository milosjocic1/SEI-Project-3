from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('destinations/', views.destinations_index, name = 'index'),
    path('destinations/<int:destination_id>', views.destinations_detail, name = 'detail'),
    path('destinations/<int:destination_id><int:user_id>/add_review', views.add_review, name='add_review'),
    # Quiz
    path('quiz/', views.quiz, name='quiz')
]
