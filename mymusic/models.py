from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    released = models.DateField(null=True, blank=True)
    # ForeignKey representsa 1:many relationship (O2M)
    # the one is the field and the many are from the class
    # it is defined on
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"
