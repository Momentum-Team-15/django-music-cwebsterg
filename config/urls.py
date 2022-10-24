"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mymusic import views

urlpatterns = [
    # set up url pattern to handle admin site paths
    path('admin/', admin.site.urls),
    # to handle any accounts view/site paths
    path('accounts/', include('registration.backends.simple.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.list_albums, name='home'),
    path('album/<int:pk>/', views.detail_album, name='detail_album'),
    path('album/new/', views.create_album, name='create_album'),
    path('album/<int:pk>/edit', views.edit_album, name='edit_album'),
]
