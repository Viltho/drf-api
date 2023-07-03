from rest_framework import serializers
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields = ('id', 'title', 'name', 'description', 'created_at', 'updated_at')