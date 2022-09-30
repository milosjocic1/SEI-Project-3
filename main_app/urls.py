from django.urls import path
from .import views


urlpatterns = [

    #  HOME AND ABOUT
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),

    # DESTINATIONS


    # REVIEWS

]
