api_key = "e91bec51ffc485e61ce6e21a076b7ae1"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
import requests
class WeatherData:
    def __init__(self, lat, lon):
        self.city = "Fes"
        self.PARAMETERS = {
            'lat': lat,
            'lon': lon,
            'appid': api_key

        }
        response = requests.get(OWM_endpoint, params=self.PARAMETERS)
        response.raise_for_status()
        self.weather_data = response.json()