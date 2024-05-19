from piper.state import State
from piper.util.weather_util import WeatherType


class WeatherDataState(State):
    conditions: WeatherType
    temperature: int

    def __init__(self):
        self.conditions = WeatherType.CLEAR
        self.temperature = 0
