from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .heat import heat

def home(request): 
    return render(request, 'input.html')

def result(request):
    heat()
    return render(request, 'output.html')
    
