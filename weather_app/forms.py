from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Latitude'}))
    longitude = forms.FloatField(label='Longitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Longitude'}))
