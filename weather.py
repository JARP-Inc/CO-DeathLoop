import requests
import random

def weather():
    response = requests.get("http://api.weatherapi.com/v1/current.json?key=2398b81c3dc04c8299e175655231802&q="+str(random.randint(0,50))+","+str(random.randint(0,50)))

    if response.json()['current']['wind_kph'] == response.json()['current']['wind_degree']:
        return True
    return False
