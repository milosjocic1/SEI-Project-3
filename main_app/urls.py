from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about'),
    path('destinations/', views.destinations_index, name = 'index'),
    path('destinations/<int:destination_id>', views.destinations_detail, name = 'detail'),
    path('destinations/<int:destination_id><int:user_id>/add_review', views.add_review, name='add_review'),
    # Quiz
    path('quiz/', views.quiz, name='quiz'),
    path('accounts/signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('users/profile/', views.profile, name='users_profile'),
    path('users/profile_update/', views.profile, name='users_profile_update')
=======
    path('users/profile/', views.profile, name='users-profile'),
    path('search/', views.search, name="search")
>>>>>>> dcdd4992e09c4a6e14f6eb0ac6e34781d0753d70
]
 