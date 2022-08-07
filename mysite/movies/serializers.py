from rest_framework import serializers
from .models import Moviedata

class MovieSerializers(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'genre', 'images'] 