from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 
from .forms import *
from .models import Simulation
from .heat import heat
import os 
from os import path

class home(CreateView): 
    model = Simulation
    form_class = SimulationForm
    template_name = 'input.html'
    success_url = reverse_lazy('trange')

def trange(request):
    basepath = os.getcwd()
    inputPath = "\\".join([basepath,"simulation\static\data.txt"])
    f = open(inputPath,"r")
    ID=f.readline()
    age=f.readline()
    f.close()
    if 'analyse' in request.POST: #get time and redirect to next page
        tval = trangef(request.POST)
        if tval.is_valid():
            li=tval.cleaned_data['li']
            hi=tval.cleaned_data['hi']
            print('===========================================')
            print(li)
            print('===========================================')
            request.session['li']=li
            request.session['hi']=hi
            return HttpResponseRedirect('/result')
    return render(request, 'first.html',{'forms':trangef(),'id': ID,'age':age,'out':False})  

def result(request): 
    basepath = os.getcwd()
    inputPath = "\\".join([basepath,"simulation\static\data.txt"])
    f = open(inputPath,"r")
    ID=f.readline()
    age=f.readline()
    f.close()
    li=request.session['li']
    hi=request.session['hi']
    if 'analyse' in request.POST: #get time and redirect to next page
        tval = thresh(request.POST)
        if tval.is_valid():
            temp=tval.cleaned_data['temp']
            heat(hi,li,temp)
            return render(request, 'output.html',{'forms':thresh(),'id': ID,'age':age,'out':True,'temp':temp})
    return render(request, 'output.html',{'forms':thresh(),'id': ID,'age':age,'out':False})

