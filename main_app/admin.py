from django.contrib import admin
from .models import Review, Destination, Profile

# Register your models here.
admin.site.register(Review)
admin.site.register(Destination)
admin.site.register(Profile)