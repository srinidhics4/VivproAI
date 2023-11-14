from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from .models import Song
from .serializers import SongSerializer
# Create your views here.

def index(request):
    queryset = Song.objects.get(id='5vYA1mW9g2Coh1HUFUSmlb')
    return HttpResponse(f"Hello world, You're at the songs index {queryset}")

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    print(queryset)
    serializer_class = SongSerializer