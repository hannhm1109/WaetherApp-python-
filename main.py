import tkinter as tk
import requests
import json
from config import api_key



# create a tkinter window
root = tk.Tk()
root.title("Simple Weather App")

# set window size and background color
root.geometry("500x400")
root.configure(bg="#e6e6fa")

# create a label widget for instructions
instructions_label = tk.Label(root, text="Enter the name of a city:", font=("Arial", 14), bg="#e6e6fa", fg="#3c3c3c")
instructions_label.pack()

# create an entry widget to get the city name from the user
city_entry = tk.Entry(root, font=("Arial", 14), bg="#f9f9f9", fg="#3c3c3c")
city_entry.pack()

# create a label widget to display the weather data
weather_label = tk.Label(root, text="", font=("Arial", 14), bg="#add8e6", fg="#3c3c3c")
weather_label.pack()

# define a function to get the weather data and display it in the label widget
def get_weather():
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        weather_label.config(text=f"The temperature in {city} is {temperature} degrees Celsius.\n"
                                   f"The weather is {description}.")
    except requests.exceptions.HTTPError as error:
        weather_label.config(text=f"HTTP Error: {error}")
    except requests.exceptions.RequestException as error:
        weather_label.config(text=f"An error occurred: {error}")

# create a button widget to get the weather data
get_weather_button = tk.Button(root, text="Get Weather", font=("Arial", 14), bg="#fff", fg="#3c3c3c", command=get_weather, bd=0, relief="flat", highlightthickness=0)
get_weather_button.pack()

# start the tkinter event loop
root.mainloop()
