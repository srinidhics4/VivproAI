import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Song
from .serializers import SongSerializer
# Create your tests here.
from .models import Song

client = Client()

class SongTest(TestCase):
    """ Test module for Song model """

    def setUp(self):
        Song.objects.create(
            id='abcdefghi', title='Sample Song')
        Song.objects.create(
            id='abcde12345', title='Another song', danceability=0.5, energy=0.75, key=1, loudness=0.34, mode=1, 
            acousticness=0.67, instrumentalness=0.89, liveness=0.54, valence=0.43, tempo=0.89, duration_ms=2839, 
            time_signature=4, num_bars=4, num_sections=2, num_segments=4, rating=5)

    def test_song_title(self):
        song_sample = Song.objects.get(title='Sample Song')
        song_another = Song.objects.get(title='Another song')
        self.assertEqual(
            song_sample.get_title(), "Song title is Sample Song")
        self.assertEqual(
            song_another.get_title(), "Song title is Another song")

class GetAllSongsTest(TestCase):
    """ Test module for GET all Songs API """

    def setUp(self):
        Song.objects.create(
            id='abcdefghi', title='Sample Song')
        Song.objects.create(
            id='abcde12345', title='Another song', danceability=0.5, energy=0.75, key=1, loudness=0.34, mode=1, 
            acousticness=0.67, instrumentalness=0.89, liveness=0.54, valence=0.43, tempo=0.89, duration_ms=2839, 
            time_signature=4, num_bars=4, num_sections=2, num_segments=4, rating=5)

    def test_get_all_songs(self):
        # get API response
        response = client.get(reverse('songs_list'))
        # get data from db
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        self.assertEqual(response.json()['count'], len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateSingleSongTest(TestCase):
    """ Test module for updating an existing Song record """

    def setUp(self):
        self.song1 = Song.objects.create(
            id='abcdefghi', title='Sample Song')
        self.song2 = Song.objects.create(
            id='abcde12345', title='Another song', danceability=0.5, energy=0.75, key=1, loudness=0.34, mode=1, 
            acousticness=0.67, instrumentalness=0.89, liveness=0.54, valence=0.43, tempo=0.89, duration_ms=2839, 
            time_signature=4, num_bars=4, num_sections=2, num_segments=4, rating=5)
        
        self.valid_payload = {
            'id': 'abcdefghi',
            'title': 'Sample Song',
            'rating': 4
        }
        self.invalid_payload = {
            'id': '12345',
            'title': '',
            'rating': 0
            }

    def test_valid_update_song(self):
        response = client.put(
            reverse('song_detail', kwargs={'lookup_param': 'id', 'value': self.song1.id}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_song(self):
        response = client.put(
            reverse('song_detail', kwargs={'lookup_param': 'id', 'value': self.song2.id}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)