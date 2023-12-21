import json
from datetime import datetime
from functools import cached_property

from src.handlers.alarm_handler import AlarmHandler
from src.handlers.config_handler import ConfigHandler
from src.handlers.spotify_handler import SpotifyHandler
from src.handlers.stock_handler import StockHandler
from src.handlers.tfl_handler import TflHandler
from src.handlers.weather_handler import WeatherHandler
from src.screens import Screen

import redis

from src.util.notion import PiperDB


class Store(object):
    r = redis.Redis(host='localhost', port=6379, db=0)
    db = PiperDB()

    configs = {}

    current_time: datetime

    global_handlers = {
        "alarms": AlarmHandler(),
        "configs": ConfigHandler(),
        "tfl": TflHandler(),
        "weather": WeatherHandler(),
        "stocks": StockHandler(),
        "spotify": SpotifyHandler(),
    }

    page_stack: [Screen] = []

    def update(self):
        [h.handle(self) for h in self.handlers_list]

    def get_formatted_hour(self) -> str:
        return str(self.current_time.hour)

    def get_formatted_minute(self) -> str:
        return str(self.current_time.minute).rjust(2, "0")

    def get_arrivals_string(self) -> str:
        if not self.tfl_handler.arrivals:
            return "No services"

        return "In " + ", ".join(list(map(lambda a: str(a.mins_to_arrival), sorted( self.tfl_handler.arrivals, key=lambda ar: ar.mins_to_arrival)))[:3]) + " mins"

    def get_weather_string(self) -> str:
        return f"{ self.weather_handler.weather.temp } °C"

    def get_weather_type(self) -> str:
        return self.weather_handler.weather.type

    def push_screen(self, page: Screen):
        self.page_stack.append(page)

    def pop_screen(self):
        self.page_stack.pop()

    def peek_screen(self) -> Screen:
        return self.page_stack[len(self.page_stack) - 1]

    def get_config(self, key: str, type=str):
        return type(self.configs[key])

    @cached_property
    def tfl_handler(self) -> TflHandler:
        return self.global_handlers["tfl"]

    @cached_property
    def weather_handler(self) -> WeatherHandler:
        return self.global_handlers["weather"]

    @cached_property
    def stock_handler(self) -> StockHandler:
        return self.global_handlers["stocks"]

    @cached_property
    def spotify_handler(self) -> SpotifyHandler:
        return self.global_handlers["spotify"]

    @cached_property
    def handlers_list(self) -> []:
        return list(self.global_handlers.values())
