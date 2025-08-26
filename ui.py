from tkinter import *
from weather import Weather
import datetime
from data import WeatherData





date = datetime.datetime.now()
date_now = datetime.date.today()
day = date_now.strftime("%A")
hour = date.hour

DAYS_OF_THE_WEEK = ["Monday", "Tuesday","Wednesday","Thursday", "Friday","Saturday", "Sunday"]


THEME_COLOR = '#a6dfd0'
WRITING_COLOR = "#871a24"
if (19 <= int(hour) < 24) or (0 <= int(hour) < 6):
    THEME_COLOR = '#292f47'# Dark theme for night
    WRITING_COLOR = "yellow"


class WeatherInterface:
    def __init__(self, weather: Weather):
        self.next_days_data = None
        self.today_btn = None
        self.day_buttons = None
        self.temperature = None
        self.image_label = None
        self.icon_img = None
        self.change_location_btn = None
        self.today_data = None
        self.lon_var = None
        self.lat_var = None
        self.lon_entry = None
        self.lat_entry = None
        self.lon_label = None
        self.lat_label = None
        self.city = None
        self.window = None
        self.weather = weather
        self.setup_ui()

    def setup_ui(self):

        self.window = Tk()
        self.window.title("Weather App")
        self.window.minsize(width=400, height=300)
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Configure column spacing
        for i in range(5):
            self.window.grid_columnconfigure(i, minsize=20)

        # City label
        self.city = Label(text=self.weather.weather_city_name, font=("Courier New", "24", "bold italic"),
                          fg="black", bg=THEME_COLOR)
        self.city.grid(row=0, column=2)

        # Change location UI elements
        self.setup_location_controls()

        # Weather display elements
        self.setup_weather_display()

        # Initialize day buttons
        self.setup_day_buttons()

        self.window.mainloop()

    def setup_location_controls(self):

        # Labels
        self.lat_label = Label(self.window, text='Latitude', font=('calibre', 8, 'italic'), bg=THEME_COLOR)
        self.lon_label = Label(self.window, text='Longitude', font=('calibre', 8, 'italic'), bg=THEME_COLOR)

        # Entries
        self.lat_var = StringVar()
        self.lon_var = StringVar()
        self.lat_entry = Entry(self.window, textvariable=self.lat_var, font=('calibre', 8, 'normal'))
        self.lon_entry = Entry(self.window, textvariable=self.lon_var, font=('calibre', 8, 'normal'))

        # Button
        self.change_location_btn = Button(text=f"Change\nlocation",
                                          font=("Courier New", "8", "bold italic"),
                                          fg=WRITING_COLOR, highlightthickness=0, bg=THEME_COLOR, padx=8,
                                          command=self.change_location)

        # Grid placement
        self.lat_entry.grid(row=4, column=4, pady=15)
        self.lon_entry.grid(row=5, column=4, pady=5)
        self.lat_label.grid(row=4, column=3)
        self.lon_label.grid(row=5, column=3)
        self.change_location_btn.grid(row=6, column=4, padx=5)

    def setup_weather_display(self):

        # Get initial data
        self.today_data = self.weather.get_today_data()

        # Weather icon for today
        self.icon_img = PhotoImage(file=self.today_data['icon'])
        self.image_label = Label(image=self.icon_img, bg=THEME_COLOR)
        self.image_label.grid(row=1, column=2)

        # Temperature for today
        self.temperature = Label(text=f"{self.today_data['temp']}°", font=("Courier New", "24", "bold italic"),
                                 fg="black", bg=THEME_COLOR)
        self.temperature.grid(row=2, column=2)

    def setup_day_buttons(self):

        self.day_buttons = []

        # Today button
        self.today_btn = Button(text=f"Today\n{self.weather.weather_temperature_max}°",
                                font=("Courier New", "12", "bold italic"),
                                fg=WRITING_COLOR, highlightthickness=0, bg=THEME_COLOR, padx=8, pady=8,
                                command=lambda: self.get_specific_data_ui(self.today_data['temp'],
                                                                          self.today_data['icon']))
        self.today_btn.grid(row=3, column=0, padx=5)
        self.day_buttons.append(self.today_btn)

        # Next days button
        self.next_days_data = self.weather.get_next_days_data()
        for i, day_data in enumerate(self.next_days_data, 1):
            day_btn = Button(text=f"{day_data['day_name']}\n{day_data['avg_temp']}°",
                             font=("Courier New", "12", "bold italic"),
                             fg=WRITING_COLOR, highlightthickness=0, bg=THEME_COLOR, padx=8, pady=8,
                             command=lambda d=day_data: self.get_specific_data_ui(d['avg_temp'], d['icon']))
            day_btn.grid(row=3, column=i, padx=5)
            self.day_buttons.append(day_btn)

    def get_specific_data_ui(self, temperature, image):

        self.temperature.config(text=f"{temperature}°")
        self.icon_img = PhotoImage(file=image)
        self.image_label.config(image=self.icon_img)
        self.image_label.image = self.icon_img  # Keep reference

    def update_ui(self):

        # Get fresh data
        self.today_data = self.weather.get_today_data()
        self.next_days_data = self.weather.get_next_days_data()

        # Update city name
        self.city.config(text=self.weather.weather_city_name)

        # Update today's weather display
        self.icon_img = PhotoImage(file=self.today_data['icon'])
        self.image_label.config(image=self.icon_img)
        self.image_label.image = self.icon_img
        self.temperature.config(text=f"{self.today_data['temp']}°")

        # Update today button
        self.today_btn.config(text=f"Today\n{self.weather.weather_temperature_max}°",
                              command=lambda: self.get_specific_data_ui(self.today_data['temp'],
                                                                        self.today_data['icon']))

        # Update next days buttons
        for i, day_data in enumerate(self.next_days_data, 1):
            if i < len(self.day_buttons):
                self.day_buttons[i].config(text=f"{day_data['day_name']}\n{day_data['avg_temp']}°",
                                           command=lambda d=day_data: self.get_specific_data_ui(d['avg_temp'],
                                                                                                d['icon']))

    def change_location(self):

        try:
            new_lat = self.lat_var.get()
            new_lon = self.lon_var.get()

            # Validate inputs (basic check)
            if not new_lat or not new_lon:
                return

            # Update the weather data with new location
            if self.weather.update_location(new_lat, new_lon):
                # If successful, update the UI
                self.update_ui()
        except Exception as e:

            print(f"Error updating location: {e}")