from django import forms
from .models import my_cities
    

class CityForm(forms.Form):
    City = forms.ModelChoiceField(queryset=my_cities.objects.all())
 
class addressForm(forms.Form):
    lat = forms.CharField(max_length=15)
    lon = forms.CharField(max_length=15)
    location = forms.CharField(max_length=150)

