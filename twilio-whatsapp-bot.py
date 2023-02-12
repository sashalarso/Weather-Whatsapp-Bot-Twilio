from twilio.rest import Client 
import os
import schedule
import requests
from dateutil.parser import parse

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_TOKEN')

client = Client(account_sid, auth_token) 
def send_message(city,hour):
    time,temp=weather(city,hour)

    time=str(time)
    temp=str(temp)

    get_date_obj = parse(time)
    hour=str(get_date_obj.hour)
    day=str(get_date_obj.day)
    month=str(get_date_obj.month)

    msg="A :"+city+" à "+hour+" h, le "+day+"/"+month+ " il fera :"+temp+" degrés Celcius"

    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body=msg,      
                                to='whatsapp:+33782142677'
                            ) 
    
def find_lat_long(city):
    response=requests.get("http://api.positionstack.com/v1/forward?access_key=36b6e9376680b1fa86c077a64139f062&query="+city).json()
    latitude=response["data"][0]["latitude"]
    longitude=response["data"][0]["longitude"]

    return latitude, longitude

def weather(city,hour):
    latitude,longitude=find_lat_long(city)
    latitude=str(latitude)
    longitude=str(longitude)
    response=requests.get("https://api.open-meteo.com/v1/forecast?latitude="+latitude+"&longitude="+longitude+"&hourly=temperature_2m").json()

    return response["hourly"]["time"][hour],response["hourly"]["temperature_2m"][hour]


send_message("Marseille",18)


