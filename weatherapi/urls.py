from .views import get_weather
from django.urls import path

urlpatterns = [
    path('weather/', get_weather, name='get_weather')
]
