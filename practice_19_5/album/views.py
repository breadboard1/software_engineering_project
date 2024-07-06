from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.
@login_required
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, './album/add_album.html', {'forms':album_form})

@login_required
def edit_album(request, id):
    post = models.Album.objects.get(pk=id)
    edited_album = forms.AlbumForm(instance=post)
    if request.method == 'POST':
        edited_album = forms.AlbumForm(request.POST, instance=post)
        if edited_album.is_valid():
            edited_album.save()
            return redirect('home')
    return render(request, './album/add_album.html', {'forms':edited_album})

@login_required
def delete_album(request, id):
    post = models.Album.objects.get(pk = id)
    post.delete()
    return redirect('home')