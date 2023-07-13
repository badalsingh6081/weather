from django import forms
from .models import City,Coordinate


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields= ['name']
        widgets={
            'name': forms.TextInput(attrs={'class':'input','placeholder':'City Names'})
        }

class CoordinateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields= ['lat','long']
        widgets={
            'lat': forms.TextInput(attrs={'class':'input','placeholder':'Lattitude'}),
            'long': forms.TextInput(attrs={'class':'input','placeholder':'Longitude'})
        }

