import datetime
import time
import requests

url = "https://yahoo-weather5.p.rapidapi.com/weather"

bot_token = "5126869787:AAFp65OYO2VW5FhVH6nTo_9l4p3ONqHAzUE"

chat_id = "952979574"


time_ref = 60 

def send_data():

 querystring = {"location":"Alger","format":"json","u":"c"}

 headers = {
     'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
     'x-rapidapi-key': "a23312faddmsh88e72ae5ff00486p112c5djsn83488f429f16"
     }

 response = requests.request("GET", url, headers=headers, params=querystring).json()
 
 while(True):
  
  for i in range(0 ,11):

     day = response['forecasts'][i]['day']
 
     low = response['forecasts'][i]['low']
 
     high = response['forecasts'][i]['high']
 
     description = response['forecasts'][i]['text']
 
     date = datetime.datetime.fromtimestamp(response['forecasts'][i]['date']).strftime("%d/%m/%Y")
  
     msg = f"date -->{day} {date} \ncountry --> Algeria\ncity --> Alger center \nlow-->{low}\nhigh-->{high}\n--{description}--"
  
     print(msg)
  
     send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
     requests.get(send_url)
  
  time.sleep(time_ref)

send_data()