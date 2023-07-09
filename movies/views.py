from django.shortcuts import render
from rest_framework import generics
from .models import Movies, Favorite
from .serializers import MovieSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Create your views here.

# ListAPIView
class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    
# class MoviesDelete(generics.DestroyAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer
#     permission_classes = [IsOwnerOrReadOnly]
    
class MoviesUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
# class MoviesCreate(generics.CreateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer
#     permission_classes = [IsAuthenticated]
    
class FavoriteList(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrReadOnly]

