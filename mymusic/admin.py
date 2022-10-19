from django.contrib import admin
from .models import User, Album

# Register your models here.
# So you can see them in the admin
admin.site.register(User)
admin.site.register(Album)
