import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' 
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def update_weather():
    city = city_entry.get()
    if city:
        weather_data = get_weather(api_key, city)
        if weather_data:
            display_weather(weather_data)
        else:
            messagebox.showerror("Error", f"Failed to fetch weather data for {city}.")
    else:
        messagebox.showerror("Error", "Please enter a city.")

def display_weather(data):
    temperature_label.config(text=f"Temperature: {data['main']['temp']}°C")
    weather_label.config(text=f"Weather: {data['weather'][0]['description']}")
    humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# OpenWeatherMap API key 
api_key = "9f7e01462f26823e7074f4b89dc429df"

# Create and configure GUI widgets
notebook = ttk.Notebook(app)

# Current Weather Tab
current_weather_frame = ttk.Frame(notebook)
notebook.add(current_weather_frame, text='Current Weather')

city_label = tk.Label(current_weather_frame, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(current_weather_frame)
city_entry.pack()

get_weather_button = tk.Button(current_weather_frame, text="Get Weather", command=update_weather)
get_weather_button.pack()

temperature_label = tk.Label(current_weather_frame, text="", font=("Helvetica", 16))
temperature_label.pack()

weather_label = tk.Label(current_weather_frame, text="", font=("Helvetica", 14))
weather_label.pack()

humidity_label = tk.Label(current_weather_frame, text="")
humidity_label.pack()

wind_speed_label = tk.Label(current_weather_frame, text="")
wind_speed_label.pack()

notebook.pack(expand=True, fill="both")

app.mainloop()
