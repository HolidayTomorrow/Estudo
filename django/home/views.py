from django.shortcuts import render

def home(request):
    print('home')
    
    context= {
        'title' : 'Página inicial - ',
        'h1' : 'Página inicial'
    }
    
    return render(
        request,
        'index.html',
        context,
    )
