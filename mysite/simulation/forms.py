from django import forms

class thresh(forms.Form):
    li = forms.FloatField(label='Lowest Temp  :')
    hi = forms.FloatField(label='Highest Temp :')
    temp = forms.FloatField(label='thresh Temp  :')