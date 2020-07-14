from django import forms
from .models import Simulation

class SimulationForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ['cover']
        
class thresh(forms.Form):
    li = forms.FloatField(label='Lowest Temp  :')
    hi = forms.FloatField(label='Highest Temp :')
    temp = forms.FloatField(label='thresh Temp  :')