from datetime import datetime

import requests

from src.handlers.timed_handler import TimedHandler


class Weather(object):
    type: str
    temp: int

    def __init__(self, weather_response):
        self.temp = round(weather_response["current"]["temperature_2m"])
        self.type = "clear"


class WeatherHandler(TimedHandler):
    weather: Weather

    @property
    def seconds_pause(self) -> int:
        return 3600

    def handle(self, ctx):
        if super().handle(ctx):
            weather_endpoint = ctx.get_config("weather_endpoint_url")

            weather_response = requests.get(weather_endpoint).json()

            self.weather = Weather(weather_response)
