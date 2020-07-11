from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .heat import heat
from .forms import *

def home(request): 
    f = open(r"C:\Users\bharathambika\Desktop\opencv-django\mysite\simulation\static\data.txt","r")
    ID=f.readline()
    age=f.readline()
    f.close()
    if 'analyse' in request.POST: #get time and redirect to next page
        tval = thresh(request.POST)
        if tval.is_valid():
            li=tval.cleaned_data['li']
            hi=tval.cleaned_data['hi']
            temp=tval.cleaned_data['temp']
            heat(hi,li,temp)
            return render(request, 'input.html',{'forms':thresh(),'id': ID,'age':age,'out':True})
    return render(request, 'input.html',{'forms':thresh(),'id': ID,'age':age,'out':False})

