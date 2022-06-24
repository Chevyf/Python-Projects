import requests
import math
import cred


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
d = u'\N{DEGREE SIGN}'

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={cred.API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temprature = round(1.8 * (data["main"]["temp"] - 273.15) + 32, 2) 

    print("Weather: "+ weather)
    print(f"Temprature: {temprature}{d}")

else:
    print("An error occurred.")
