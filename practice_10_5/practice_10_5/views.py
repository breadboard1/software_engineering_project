from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def context(request):
    dic = { 'author' : 'kuddus', 'lst' : [1, 3, 5], 'data' : ['java', 'cpp', 'python'], 's':'Math is fun. It speaks',
        'languages':[
            {'langId' : 'python', 'popularity' : 'high', 'used' : 'everywhere'},
            {'langId' : 'java', 'popularity' : 'android', 'used' : 'application'},
            {'langId' : 'kotlin', 'popularity' : 'app', 'used' : 'everywhere'},
            {'langId' : 'cpp', 'popularity' : 'VVI', 'used' : 'cp'},
            {'langId' : 'c', 'popularity' : 'preliminary', 'used' : 'basic'},
        ],
    }
    return render(request, 'context.html', dic)