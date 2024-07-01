from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def app(request):
    if request.method == 'POST':
        example_form = forms.ExampleModelForm(request.POST)
        if example_form.is_valid():
            example_form.save()
            return redirect('app')
    else:
        example_form = forms.ExampleModelForm()
    return render(request, './application/app.html', {'forms':example_form})