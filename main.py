import requests
from ui import WeatherInterface
from weather import Weather
import datetime




api_key = "e91bec51ffc485e61ce6e21a076b7ae1"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather = Weather()

weather_app = WeatherInterface(weather)





