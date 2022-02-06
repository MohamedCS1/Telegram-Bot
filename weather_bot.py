import requests

url = "https://yahoo-weather5.p.rapidapi.com/weather"

bot_key = "5126869787:AAFp65OYO2VW5FhVH6nTo_9l4p3ONqHAzUE"

chat_id = "952979574"


time_ref = 60 * 60 * 24

def send_data():

 querystring = {"location":"Alger","format":"json","u":"c"}

 headers = {
     'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
     'x-rapidapi-key': "a23312faddmsh88e72ae5ff00486p112c5djsn83488f429f16"
     }

 response = requests.request("GET", url, headers=headers, params=querystring).json()
 
 t = response['city'][0]
 print(t)

send_data()