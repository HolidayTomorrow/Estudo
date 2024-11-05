from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('Home')
    return HttpResponse('Home')

# Create your views here.
