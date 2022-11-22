import requests
from pprint import pprint

API_Key = "882d490eeae157bc259a7e1bda0035bf"

location = "Saskatoon"  # input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()

print("------------")
pprint(weather_data)


# call 5 day 3 hour forcast
lat = weather_data['coord']['lat']
lon = weather_data['coord']['lon']

forcast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_Key}"
weather_forcast = requests.get(final_url).json()
print("------------")
pprint(weather_forcast)