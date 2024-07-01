from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, './tasks/add_task.html', {'forms':task_form})

def edit_task(request, id):
    task = models.Task.objects.get(pk = id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request, './tasks/add_task.html', {'forms':task_form})

def delete_task(request, id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('home')