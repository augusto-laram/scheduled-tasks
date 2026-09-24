import requests

API_KEY = "fca620e0614bbfc90d388e39d6c36a0e"
MY_LAT = 18.8480278 # Your latitude
MY_LONG = -97.0806111 # Your longitude
WD_ENDPOINT = f"https://api.openweathermap.org/data/2.5/forecast?"

BOT_TOKEN = "8970180675:AAF4CEVxZXQIoTQsDBj24f94U8BPpMy-ODs"
CHAT_ID = "6797881320"

response = requests.get(WD_ENDPOINT, params={
    "lat":MY_LAT,
    "lon":MY_LONG,
    "cnt":4,
    "appid":API_KEY,
})
response.raise_for_status()
weather_data = response.json()
for time_data in weather_data["list"]:
    if time_data["weather"][0]['id'] < 700:
        print(type(time_data["weather"][0]['id']))
        # message = "🌧️ Rain is expected today! Bring an umbrella!"
        # url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        # parameters = {
        #     "chat_id": CHAT_ID,
        #     "text": message
        # }
        # response = requests.get(url, params=parameters)
        # break



