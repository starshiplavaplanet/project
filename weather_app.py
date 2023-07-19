import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": "YOUR API KEY", "units": "metric"}

    response = requests.get(url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        result_text.set(f"Current weather in {city}: {description.capitalize()}\n"
                        f"Temperature: {temperature} °C\n"
                        f"Humidity: {humidity}%\n"
                        f"Wind speed: {wind_speed} m/s")
    else:
        result_text.set("City not found or an error occurred. Please try again.")

# Create the main GUI window
root = tk.Tk()
root.title("Weather Checker")
root.geometry("1200x720")

# Customize colors
bg_color = "#f0f0f0"  # Light gray background
text_color = "#333333"  # Dark gray text color
button_color = "#4CAF50"  # Green button color

# Set the background color
root.configure(bg=bg_color)

# Create and configure the input elements
city_label = tk.Label(root, text="Please enter the city:", bg=bg_color, fg=text_color, font=("Arial", 14))
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg=button_color, fg="white", font=("Arial", 14))
get_weather_button.pack(pady=10)

# Create and configure the output element
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, bg=bg_color, fg=text_color, font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI event loop
root.mainloop()
