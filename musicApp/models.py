from django.db import models
from django.core.urlresolvers import reverse


class Genre(models.Model):
    artist_genre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.id) + '. ' + self.artist_genre

    def get_absolute_url(self):
        return reverse('genre')


class Artist(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    artist_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.id) + '. ' + self.artist_name

    # def get_absolute_url(self):
    #     return reverse('genre')

    def get_absolute_url(self):
        return reverse('artist', kwargs={'pk': self.pk})


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    album_title = models.CharField(max_length=200, unique=True)
    album_logo = models.FileField(max_length=1000)
    album_released = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + '. ' + self.album_title

    def get_absolute_url(self):
        return reverse('genre')


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200, unique=True)
    file_type = models.CharField(max_length=20)
    song_url = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.id) + '. ' + self.song_title

    def get_absolute_url(self):
        return reverse('genre')