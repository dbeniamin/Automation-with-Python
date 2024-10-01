import requests
import json
import os

url = "https://api.upcitemdb.com/prod/trial/lookup"

parameters = {
    "upc": "025000044908"
}

response = requests.get(url, params=parameters)
print(response.url)

# extract title and brand of the product
info = json.loads(response.text)
item = info["items"][0]
title = item["title"]
brand = item["brand"]
print(f"title: {title}\nbrand: {brand}")


# -------> api keys <-------

api_key = os.getenv("api_key")

weather_url = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "q": "Bucharest,RO",
    "appid": api_key
}

weather_response = requests.get(weather_url, params=weather_params)
print(weather_response.text)