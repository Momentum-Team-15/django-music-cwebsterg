from django.shortcuts import render

# Create your views here.
def index(request):
    RETURN render(request, 'mymusic/index.html')

# TODO: determine what is on index.html
# TODO: search page 

def album_list(request):
    pass
# album_list RETURNs a list of albums based on the 
# search parameters passed from index.html, a landing page
# with a search form

def album_detail(request):
    pass
# when album is selected from the album_list, RETURN
# the album_detail page which includes the title, genre,
# artist, release date, and how many likes (that's insane)

def album_create(request):
    pass
# CREATE new albums with title, artist, release date req.
# specific abiilty to cancel the add and RETURN to the list?
# ability to clear the contents/start over (redundant?)
# on SAVE, RETURN album detail template w/method below
# TODO: create forms for adding & editing 
# add icon on HTML page to add album

def album_edit(request):
    pass
# RETURN existing album with pk DISPLAY and on SAVE RETURN 
# to album detail template
# else RETURN the edit form
#  add icon on HTML page to EDIT album

# TODO: create forms for adding artist bio/detail page
# TODO: where/how to incorporate songs (and why)