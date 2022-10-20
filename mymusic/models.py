from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    last_name = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    released = models.DateField(null=True, blank=True)
    # ForeignKey representsa 1:many relationship (O2M)
    # the one is the field and the many are from the class
    # it is defined on
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Artist(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Song(models.Model):
    song = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='songs')
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song} by {Artist.objects.artist}"


class Playlist(models.Model):
    playlist = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.playlist}"

