import requests
import json
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

city=input("Enter the city name:\n")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0b81d6002f95fc5f58e08fccf865166e"
r = requests.get(url)
# print(r.text)
dict1 = json.loads(r.text)
# print(dict1)
dict2 = dict1["main"]
x=f'Temperature of {city} is {dict2["temp"]}'
print(x)
speaker.Speak(x)
