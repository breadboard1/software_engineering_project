from django.shortcuts import render, redirect
from . import models
from . forms import StudentForm

# Create your views here.
# def home(request):
#     student = models.Student.objects.all()
#     print(student)
#     return render(request, './firstapp/home.html/', {'data':student})

# def delete_student(request, roll):
#     models.Student.objects.get(pk = roll).delete()
#     return redirect('home')

def newhome(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'firstapp/newhome.html', {'forms': form})