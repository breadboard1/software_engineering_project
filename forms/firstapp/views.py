from django.shortcuts import render
from . forms import contactForm, studentForm

# Create your views here.
def index(request):
    return render(request, './firstapp/index.html')

def home(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './firstapp/home.html', {'name':name, 'email':email, 'select':select})
    return render(request, './firstapp/home.html')

def form(request):
    return render(request, './firstapp/form.html')

def djangoForm(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./firstapp/uploads/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = studentForm()
    return render(request, './firstapp/django_forms.html', {'form':form})