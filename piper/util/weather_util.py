from enum import Enum


class WeatherType(Enum):
    CLEAR = 0
    LIGHT_CLOUDS = 1
    LIGHT_RAIN = 2
    RAIN = 3
    SNOW = 4
    SHOWERS = 5
    STORM = 6


class WeatherResponseUtil(object):
    def __init__(self, response):
        self.response = response

    @property
    def temperature(self) -> int:
        return round(self.response["current"]["temperature_2m"])

    @property
    def weather_type(self) -> WeatherType:
        weather_code_max_values = [0, 3, 48, 57, 67, 77, 86, 99]
        weather_code = self.response["current"]["weather_code"]

        for category_index, weather_code_category in enumerate(weather_code_max_values):
            if weather_code <= weather_code_category:
                return WeatherType(weather_code)

        return WeatherType.CLEAR
