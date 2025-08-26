# 🌤️ WeatherApp

A modern Python desktop weather application with a beautiful GUI that provides current weather and 4-day forecasts for any location worldwide.

## ✨ Features

- **Real-time Weather Data** - Current temperature, conditions, and weather icons
- **4-Day Forecast** - Extended weather predictions with daily temperatures
- **Location Flexibility** - Change location using latitude/longitude coordinates
- **Dynamic Theming** - Automatic day/night theme switching
- **Interactive UI** - Click on any day to view detailed weather information
- **Weather Icons** - Visual representations for sunny, cloudy, rainy, and night conditions

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- tkinter (usually comes with Python)
- Internet connection for API calls

### Installation

1. **Clone/Download** the project
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python main.py
   ```

### Default Location

- **Fes, Morocco** (34.0372°N, 4.9998°W)
- Change location using the latitude/longitude inputs in the app

## 🎯 How to Use

1. **View Current Weather** - Main display shows today's temperature and conditions
2. **Check Forecast** - Click any day button to see that day's weather
3. **Change Location** - Enter new latitude/longitude and click "Change location"
4. **Theme** - App automatically switches to dark theme during night hours (7PM-6AM)

## 🛠️ Technical Stack

- **GUI Framework:** tkinter
- **Weather API:** OpenWeatherMap 5-day forecast API
- **HTTP Requests:** requests library
- **Image Handling:** PIL/Pillow
- **Data Processing:** Python collections.Counter

## 📁 Project Structure

```
WeatherApp/
├── main.py          # Entry point
├── weather.py       # Weather data processing logic
├── ui.py           # GUI interface and user interactions
├── data.py         # API communication layer
├── requirements.txt # Python dependencies
└── images/         # Weather condition icons
    ├── sunnyimg.png
    ├── cloudyimg.png
    ├── rainyimg.png
    └── night.png
```

## 🌡️ Weather Conditions

The app categorizes weather into:

- **☀️ Sunny** - Clear skies (daytime)
- **☁️ Cloudy** - Overcast conditions
- **🌧️ Rainy** - Precipitation (rain, snow, storms)
- **🌙 Night** - Dark theme with night icon

## 🔧 Configuration

- **API Key:** OpenWeatherMap API key included
- **Default Coordinates:** Fes, Morocco
- **Theme Colors:** Light green (day) / Dark blue (night)
- **Temperature Unit:** Celsius

## 📱 Screenshots

The app features a clean, minimalist design with:

- City name at the top
- Large weather icon and temperature
- Row of clickable day buttons
- Location change controls on the right

---

**Built with ❤️ using Python & tkinter**
