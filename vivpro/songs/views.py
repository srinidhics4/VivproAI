from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Song
from .serializers import SongSerializer
# Create your views here.

def index(request):
    return HttpResponse(f"Hello world, You're at the songs index")

class SongList(APIView):
    """
    List all songs, or create a new song.
    """
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        """
        Gets all objects in the Song Model class
        """
        songs = Song.objects.all()

        paginator = self.pagination_class()
        results = paginator.paginate_queryset(songs, request, view=self)
        serializer = SongSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """
        Creates a new Song object and saves data in database table
        """
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SongDetail(APIView):
    """
    Retrieve, update or delete a song instance.
    """

    def get_object(self, lookup_param, value):
        """
        Get a single Song instance filtered by id or title of Song

        Returns Song instance
        """
        try:
            if lookup_param == 'title':
                return Song.objects.get(title=value)
            elif lookup_param == 'id':
                return Song.objects.get(id=value)
            else:
                raise Http404
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, lookup_param, value, format=None):
        """
        Get a single Song instance filtered by id or title of Song

        Returns Response with serialized data
        """
        song = self.get_object(lookup_param=lookup_param, value=value)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, lookup_param, value, format=None):
        """
        Updates values of Song instance filtered by id or title

        Returns Response with serialized data or error if any
        """
        song = self.get_object(lookup_param, value)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lookup_param, value, format=None):
        """
        Deletes a Song instance from database

        Returns Response with status message
        """
        song = self.get_object(lookup_param, value)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)