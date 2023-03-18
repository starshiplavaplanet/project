import requests

# Prompt user to enter the preferred city
city = input("Please enter the city: ")

# Set up the API URL and parameters using the user's input for the city
url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": city, "appid": "2f209a89043105a7763a733831a1bf7a", "units": "metric"}

# Make the API request
response = requests.get(url, params=params)
weather_data = response.json()

# Extract the relevant information from the response
description = weather_data["weather"][0]["description"]
temperature = weather_data["main"]["temp"]
humidity = weather_data["main"]["humidity"]
wind_speed = weather_data["wind"]["speed"]

# Print the weather information
print(f"Current weather in {city}: {description.capitalize()}")
print(f"Temperature: {temperature} °C")
print(f"Humidity: {humidity}%")
print(f"Wind speed: {wind_speed} m/s")

