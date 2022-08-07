from rest_framework import serializers
from .models import Moviedata

class MovieSerializers(serializers.ModelSerializer):
    class meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating']