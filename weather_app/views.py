from django.shortcuts import render
import requests
from decouple import config, Csv

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

