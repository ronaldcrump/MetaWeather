# Ronald Crump III - 8/18/21
from threading import Thread
import requests
import datetime
import numpy as np


def getWeather(woeid):
    base_url = "https://www.metaweather.com/api/"
    # complete url address
    complete_url = base_url + f"location/{woeid}/"
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    json_data = response.json()
    # Ref dictionary Weather
    weather = json_data['consolidated_weather']
    # Get the city
    title = json_data['title']
    # Create a list of the max temp for each day
    max_temps=[day['max_temp'] for day in weather]
    # Print Average Max Temp and round 2 second decimal
    print (f"{title} Average Max Temp: {round(np.average(max_temps),2)} ℃")

if __name__ == '__main__':
    threads=[]
    # woeids of Los Angeles, Salt Lake City,Boise Average
    woeids=[2487610,2442047,2366355]
    for woeid in woeids:
        # Create thread for each city
        t=Thread(target=getWeather,args=(woeid,))
        threads.append(t)
        # Start Threads
        t.start()


