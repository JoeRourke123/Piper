from datetime import timedelta

import requests
from kink import inject

from piper.controller import PeriodicController
from piper.state.common.notion_config_state import NotionConfigState
from piper.state.common.weather_data_state import WeatherDataState


@inject
class WeatherDataController(PeriodicController):
    def __init__(self, weather_data: WeatherDataState, notion_config: NotionConfigState):
        super().__init__()
        self.weather_data = weather_data
        self.notion_config = notion_config

    def periodic_update(self):
        weather_endpoint = self.notion_config.get_config("weather_endpoint_url")

        weather_response = requests.get(weather_endpoint).json()

        self.weather_data.temperature = round(weather_response["current"]["temperature_2m"])
        self.weather_data.conditions = "clear"

    @property
    def update_every(self) -> timedelta:
        return timedelta(minutes=15)
