from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms, models

# Create your views here.
@login_required
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()
    return render(request, './musician/add_musician.html', {'forms':musician_form})

@login_required
def edit_musician(request, id):
    post = models.Musician.objects.get(pk=id)
    edited_musician = forms.MusicianForm(instance=post)
    if request.method == 'POST':
        edited_musician = forms.MusicianForm(request.POST, instance=post)
        if edited_musician.is_valid():
            edited_musician.save()
            return redirect('home')
    return render(request, './musician/add_musician.html', {'forms':edited_musician})