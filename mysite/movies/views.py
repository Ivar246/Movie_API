from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializers
from .models import Moviedata
# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializers
    

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='action')
    serializer_class = MovieSerializers
    

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(genre='comedy')
    serializer_class = MovieSerializers