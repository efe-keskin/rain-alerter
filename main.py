import requests
import datetime
from twilio.rest import Client

api_key = "YOUR_API_KEY"
latitude = "29.56"
longitude = "121.09"

account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

dt = datetime.datetime(2022, 7, 15).timestamp()
parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for _ in range(12):
    weather_id = weather_data["hourly"][_]["weather"][0]["id"]
    print(weather_id)
    if 200 <= weather_id <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bugün Yağmurlu Gözüküyor Efe, Şemsiye Almayı Unutma.☂️️️❤️",
        from_='YOUR_TWILIO_PHONE_NUMBER',
        to='RECIPIENT_PHONE_NUMBER'
    )
    print(message.status)
