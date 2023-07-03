from django.urls import path
from .views import MoviesList, MoviesDelete, MoviesUpdate, MoviesCreate

urlpatterns = [
    path('',MoviesList.as_view(), name='movielist'),
    path('delete/<int:pk>/',MoviesDelete.as_view(), name='moviedelete'),
    path('update/<int:pk>/',MoviesUpdate.as_view(), name='movieupdate'),
    path('create/',MoviesCreate.as_view(), name='moviecreate'),
]