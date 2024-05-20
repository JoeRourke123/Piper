from piper.state import State
from piper.util.weather_util import WeatherType


class WeatherDataState(State):
    conditions: WeatherType
    temperature: int
    min_temperature: int
    max_temperature: int

    def __init__(self):
        self.conditions = WeatherType.CLEAR
        self.temperature = 0
        self.min_temperature = 0
        self.max_temperature = 0
