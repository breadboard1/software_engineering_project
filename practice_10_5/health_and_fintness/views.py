from django.shortcuts import render

# Create your views here.

def index(request):
    data = [
        {'id' : 1, 'weight': 50, 'height': 130,},
        {'id' : 2, 'weight': 60, 'height': 150,},
        {'id' : 3, 'weight': 70, 'height': 190,},
        {'id' : 4, 'weight': 80, 'height': 120,},
        {'id' : 5, 'weight': 90, 'height': 110,},
    ]
    return render(request, 'health_and_fintness/index.html', {'data' : data})