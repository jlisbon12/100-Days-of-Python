import requests
import os
from twilio.rest import Client

api_key = "f8a32fa0b9543f2acb6f93eb8c87c2f4"
account_sid = "ACef5d0855247b9cb19a69adbf43254c3f"
auth_token = "b03a5bccd144c033d8aead6d073711e9"
### EASY VIEWING ###
#   jsonviewer.stack.hu


parameters = {
    "lat": "35.467560",
    "lon": "-97.516426",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()
next_12 = [weather_data['hourly'][i]['weather'] for i in range(0,11)]

will_rain = False
for data in next_12:
    if data[0]['id'] < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's gonna rain today. Make sure to bring an ☔",
        from_='+13254408012',
        to='+14045108390'
    )
    print(message.status)