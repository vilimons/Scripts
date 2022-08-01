import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "92d3f2af2a91ad77a08c95dc2ee89fd2"
account_sid = "AC6c1a2a8154d32e6a30b078ee9c7e53f5"
auth_token = "5b2e1560d6ccccac7ebbbedb9d3f1626"

weather_params = {
    "lat": -23.550520,
    "lon": -46.633308,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella.",
            from_= "+17372657099",
            to="+5511989100623"
        )

print(message.status)