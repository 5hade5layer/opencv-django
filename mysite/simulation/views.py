from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 
from .forms import SimulationForm 
from .models import Simulation
from .heat import heat

class home(CreateView): 
    model = Simulation
    form_class = SimulationForm
    template_name = 'input.html'
    success_url = reverse_lazy('result')

def result(request):
    heat()
    return render(request, 'output.html')
    
