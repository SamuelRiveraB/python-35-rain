import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("API_KEY")
print(API_KEY)

weather_params = {
    "lat": 6.2518,
    "lon": -75.5636,
    "appid": API_KEY,
    "cnt": 4,
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_='whatsapp:+14155238886',
                                  body='Bring an umbrella! ☂️',
                                  to=f'whatsapp:{os.environ.get("NUM")}'
                              )
    print(message.status)