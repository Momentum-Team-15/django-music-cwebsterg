from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Album
from .forms import AlbumForm


# Create your views here.
# def index(request):
#     return render(request, 'mymusic/index.html')

# TODO: welcome and search page

def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'mymusic/list_albums.html', {'albums': albums})

def detail_album(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'mymusic/detail_album.html', {'album': album})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        form = AlbumForm()
    return render (request, 'mymusic/create_album.html', {'form': form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect("detail_album")
