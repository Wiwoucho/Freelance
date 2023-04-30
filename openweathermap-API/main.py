import requests


API_KEY = "YourAPIKey"
            #API_KEY from the https://openweathermap.org/

city = input("Input your city: ")                       #Input the desired city

geocord_api_call_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"       #requests lon, lat
response_api_call_URL = requests.get(geocord_api_call_URL)                                            #from API

if response_api_call_URL.status_code == 200:                           #Checking if the status is 200
    data = response_api_call_URL.json()                                #converting the info from the API to JSON
    lon = (data[0]["lon"])                                             #Get the longitude
    lat = (data[0]["lat"])                                             #Get the latitude

else:
    print("Error occurred")

city_api_weather_call_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"      #requests city info from
response_city_call = requests.get(city_api_weather_call_URL)                                                            #the give lon, lat

city_weather_data = response_city_call.json()                                #converting the info from the API to JSON
#print(city_weather_data)          #<-- This line will print the whole information from the given request

current_temperature = round((city_weather_data["main"]["temp"]) - 273.15), "°C"              #extracting the temperature
max_temperature = round((city_weather_data["main"]["temp_max"]) - 273.15), "°C"              #from the JSON representation
min_temperature = round((city_weather_data["main"]["temp_min"]) - 273.15), "°C"
skies_description = city_weather_data["weather"][0]["description"]                           #Also extracting the skies

print(f"City: {city_weather_data['name']}")                                                                       #printing the desired info
print(f"Current temperature: {''.join(str(x) for x in current_temperature)}")
print(f"Max temperature for the day: {''.join(str(x) for x in max_temperature)}")
print(f"Min temperature for the day: {''.join(str(x) for x in min_temperature)}")
print(f"Current skies: {skies_description}")