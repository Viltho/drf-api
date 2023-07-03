from django.shortcuts import render
from rest_framework import generics
from .models import Movies 
from .serializers import MovieSerializer

# Create your views here.

# ListAPIView
class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class MoviesDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    
class MoviesUpdate(generics.RetrieveUpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    
class MoviesCreate(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
