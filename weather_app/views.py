from django.shortcuts import render
import requests
from decouple import config, Csv
from .forms import LocationForm

def get_weather(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            api_key = config('API_KEY')
            api_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude},{longitude}"
            response = requests.get(api_url)
            weather_data = response.json()
            return render(request, 'weather_results.html', {'form': form, 'weather': weather_data})
    else:
        form = LocationForm()

    return render(request, 'weather_form.html', {'form': form})

def weather(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        api_key = config('API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
        response = requests.get(url)
        weather_data = response.json()
        return render(request, 'weather.html', {'weather_data': weather_data})
    else:
        return render(request, 'weather.html')

def home(request):
        return render(request, 'home.html',{"name":"home"})




