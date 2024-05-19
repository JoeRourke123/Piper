from datetime import datetime
from enum import Enum

from dateutil.parser import parse


class WeatherType(Enum):
    CLEAR = 0
    FOG = 1
    LIGHT_CLOUDS = 2
    LIGHT_RAIN = 3
    RAIN = 4
    SNOW = 5
    SHOWERS = 6
    STORM = 7
    CLOUD = 8
    CLEAR_NIGHT = 9


class WeatherResponseUtil(object):
    def __init__(self, response):
        self.response = response

    @property
    def temperature(self) -> int:
        return round(self.response["current"]["temperature_2m"])

    @property
    def sunset(self) -> datetime:
        return parse(self.response["daily"]["sunset"][0])

    @property
    def max_temperature(self) -> int:
        return round(self.response["daily"]["temperature_2m_max"][0])

    @property
    def min_temperature(self) -> int:
        return round(self.response["daily"]["temperature_2m_min"][0])

    @property
    def weather_type(self) -> WeatherType:
        weather_code_max_values = [0, 3, 48, 57, 67, 77, 86, 99]
        weather_code = self.response["current"]["weather_code"]

        for category_index, weather_code_category in enumerate(weather_code_max_values):
            if weather_code <= weather_code_category:
                weather_type = WeatherType(category_index)

                if self.sunset < datetime.now() and weather_type == WeatherType.CLEAR:
                    return WeatherType.CLEAR_NIGHT

                return weather_type

        return WeatherType.CLOUD
