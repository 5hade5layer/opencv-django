from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .heat import heat

def home(request): 
    return render(request, 'input.html')

def result(request):
    heat()
    f = open(r"C:\Users\bharathambika\Desktop\opencv-django\mysite\simulation\static\data.txt","r")
    ID=f.readline()
    age=f.readline()
    f.close()
    return render(request, 'output.html',{'id': ID,'age':age})
    
