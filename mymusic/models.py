from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length=25, default='Last Name')
    first_name = models.CharField(max_length=25, default='First Name')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    album_cover = models.ImageField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Artist(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Song(models.Model):
    song = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='songs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song} by {Artist.objects.artist}"


class Playlist(models.Model):
    playlist = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.playlist}"

