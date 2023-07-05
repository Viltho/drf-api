from django.urls import path
from .views import MoviesList, MoviesUpdate, FavoriteList, FavoriteDetail

urlpatterns = [
    path('',MoviesList.as_view(), name='movielist'),
    path('update/<int:pk>/',MoviesUpdate.as_view(), name='movieupdate'),
    path('favorites/',FavoriteList.as_view(), name='favoritelist'),
    path('favorites/<int:pk>',FavoriteDetail.as_view(), name='favoritelist'),
]