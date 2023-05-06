import requests
import os
from django.http import JsonResponse

def get_weather(request):
    api_key = os.environ.get('API_KEY')
    city = request.GET.get('Austin')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url).json()
    return JsonResponse(response)