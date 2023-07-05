from django.contrib import admin
from .models import Movies, Favorite

# Register your models here.
admin.site.register(Movies)
admin.site.register(Favorite)
