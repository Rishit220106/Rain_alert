import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("api_key")
params={
    "lat":19.075983,
    "lon":72.877655,
    "cnt":4,
    "appid":api_key
}
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=params)
response.raise_for_status()
data=response.json()
print(data['cod'])
print(data['list'])
list_=data['list']

for dict_ in list_:
    if dict_['weather'][0]['id']<700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Bring your umbrella.",
            from_="+14323004751",
            to="+918149923565",
        )
        print(message.status)
        break
