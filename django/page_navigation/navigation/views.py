from django.shortcuts import render

# Create your views here.

def about(request):
    d = {'author': 'rahim', 'age': 20, 'sells':1000, 'courses': [
        {
            'id':1,
            'name': 'python',
            'fee':1500
        },
        {
            'id':2,
            'name': 'django',
            'fee':2000
        },
        {
            'id':3,
            'name': 'cpp',
            'fee':1000
        }
    ]}
    return render(request, 'navigation/about.html', d)
def contact(request):
    return render(request, 'navigation/contact.html')
