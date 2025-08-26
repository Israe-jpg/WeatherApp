import requests
import datetime
from collections import Counter
from data import WeatherData

datetime_now = datetime.datetime.now()
hour = datetime_now.hour


cloudy_img = "images/cloudyimg.png"
rainy_img = "images/rainyimg.png"
sunny_img = "images/sunnyimg.png"
night_img = "images/night (2).png"

#get ahold of the data
# weather_data =WeatherData('34.0372','-4.9998').weather_data

# Define days of the week for reference
DAYS_OF_THE_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class Weather:
    def __init__(self, lat='34.0372', lon='-4.9998'):
        self.next_days_forecast = None
        self.weather_temperature_max = None
        self.weather_temperature = None
        self.weather_city_name = None
        self.weather_description = None
        self.weather_code = None
        self.daily_data = None
        self.weather_data = None
        self.lat = lat
        self.lon = lon
        self.update_weather_data()

    def update_weather_data(self):

        self.weather_data = WeatherData(self.lat, self.lon).weather_data
        self.daily_data = {}
        self.weather_code = self.weather_data['list'][0]['weather'][0]['id']
        self.weather_description = self.weather_data['list'][0]['weather'][0]['main']
        self.weather_city_name = self.weather_data["city"]['name']
        self.weather_temperature = int((self.weather_data['list'][0]['main']['temp']) - 273.15)
        self.weather_temperature_max = int((self.weather_data['list'][0]['main']['temp_max']) - 273.15)
        self.next_days_forecast = self._process_next_days()

    def update_location(self, lat, lon):

        self.lat = lat
        self.lon = lon
        self.update_weather_data()
        return True

    def weather_state(self):
        if self.weather_code <= 700:
            return rainy_img
        elif 6 < int(hour) < 19:
            if self.weather_code == 800:
                return sunny_img
            elif self.weather_code > 800:
                return cloudy_img
        else:
            return night_img

    def _process_next_days(self):

        # Current day to exclude from results
        current_day = datetime_now.strftime('%Y-%m-%d')

        # Iterate through the 3-hour forecasts
        for item in self.weather_data['list']:
            # Convert timestamp to datetime
            timestamp = item['dt']
            date = datetime.datetime.fromtimestamp(timestamp)
            day_key = date.strftime('%Y-%m-%d')

            # Skip current day
            if day_key == current_day:
                continue

            # Extract temperature and weather data
            temp_kelvin = item['main']['temp_max']
            temp_celsius = temp_kelvin - 273.15
            weather_condition = item['weather'][0]['main']
            weather_id = item['weather'][0]['id']

            # Add or append to the daily data
            if day_key not in self.daily_data:
                self.daily_data[day_key] = {
                    'temp': [temp_celsius],
                    'temp_count': 1,
                    'weather_conditions': [weather_condition],
                    'weather_ids': [weather_id],
                    'day_name': date.strftime('%A')
                }
            else:
                self.daily_data[day_key]['temp'].append(temp_celsius)
                self.daily_data[day_key]['temp_count'] += 1
                self.daily_data[day_key]['weather_conditions'].append(weather_condition)
                self.daily_data[day_key]['weather_ids'].append(weather_id)

        # Calculate averages and determine most common weather condition for each day
        daily_summary = []
        for day, data in self.daily_data.items():
            high_temp = max(data['temp'])

            # Find most common weather condition
            weather_counter = Counter(data['weather_conditions'])
            most_common_weather = weather_counter.most_common(1)[0][0]

            # Find most common weather ID
            id_counter = Counter(data['weather_ids'])
            most_common_id = id_counter.most_common(1)[0][0]

            daily_summary.append({
                'date': day,
                'day_name': data['day_name'],
                'avg_temp': round(high_temp),  # Round to integer
                'weather': most_common_weather,
                'weather_id': most_common_id
            })

            # Only keep the next 4 days
            if len(daily_summary) >= 4:
                break

        return daily_summary

    def get_weather_icon(self, weather_id):

        if weather_id <= 700:
            return rainy_img
        elif 6 < int(hour) < 19:
            if weather_id == 800:
                return sunny_img
            elif weather_id != 800 and weather_id > 700:
                return cloudy_img
        else:
            return night_img

    def get_today_data(self):

        return {
            'day_name': 'Today',
            'temp': self.weather_temperature,
            'weather': self.weather_description,
            'icon': self.weather_state()
        }

    def get_next_days_data(self):

        forecast_with_icons = []
        for day_data in self.next_days_forecast:
            day_data['icon'] = self.get_weather_icon(day_data['weather_id'])
            forecast_with_icons.append(day_data)
        return forecast_with_icons

