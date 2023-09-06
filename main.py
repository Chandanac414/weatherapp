import requests
import json
city=input("enter the city name")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0b81d6002f95fc5f58e08fccf865166e"
r = requests.get(url)
# print(r.text)
dict1 = json.loads(r.text)
# print(dict1)
dict2 = dict1["main"]
print("temperature of",city,"is ",dict2["temp"])
