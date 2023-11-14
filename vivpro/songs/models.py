from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.CharField(primary_key=True)
    title = models.CharField()
    danceability = models.FloatField(null=True)
    energy = models.FloatField(null=True)
    key = models.IntegerField(null=True)
    loudness = models.FloatField(null=True)
    mode = models.IntegerField(null=True)
    acousticness = models.FloatField(null=True)
    instrumentalness = models.FloatField(null=True)
    liveness = models.FloatField(null=True)
    valence = models.FloatField(null=True)
    tempo = models.FloatField(null=True)
    duration_ms = models.IntegerField(null=True)
    time_signature = models.IntegerField(null=True)
    num_bars = models.IntegerField(null=True)
    num_sections = models.IntegerField(null=True)
    num_segments = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'songs'

    def get_title(self):
        return 'Song title is ' + self.title

    def __repr__(self):
        return self.title + ' is added.'
