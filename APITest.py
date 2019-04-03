# Python code to set LED colors of DB1 based on current weather in Boulder, CO.
# Hot weather (100F) will set the LEDs red. Cold weather (0F) will set the LEDs blue.
# Weather in between will set the color ranging from green to yellow.
# Weather API from: https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

import requests, json 
from db1 import Db1
from db1 import RgbMode
import time

if __name__ == "__main__":
	print("DB1 Python Weather API Demo!")

	DB1 = Db1()

	# Enter your API key here 
	# Please don't use this for anything besides this example!
	api_key = "886705b4c1182eb1c69f28eb8c520e20"
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	city_name = "Boulder"
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url) 

	x = response.json() 
	if x["cod"] != "404": 
		y = x["main"] 
		t_k = y["temp"] 

		# convert to F
		t_f = clamp((t_k - 273.15) * (9/5) + 32, 0, 100)

		#100 degrees F = red (0) , 0 degrees F = blue (200)
		h = int(200 - (2*t_f))
		print("Temp (F): " + str(t_f) + " Hue: " + str(h))
		DB1.set_rgb_mode(RgbMode.Static)
		DB1.set_hsv_no_eeprom(h, 100, 50)

		print("Done!")

	else:
		print("API error! Are you rate-limited?")