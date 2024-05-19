from pyray import load_texture

from piper.state.common.weather_data_state import WeatherDataState
from piper.util.weather_util import WeatherType


class TextureConfig(object):
    def __init__(self):
        self.__tfl_icon_texture = None
        self.__weather_icons = {}

    @property
    def tfl_icon(self):
        if self.__tfl_icon_texture is None:
            self.__tfl_icon_texture = load_texture("resources/tfl.png")

        return self.__tfl_icon_texture

    def weather_icon(self, weather_type: WeatherType):
        if weather_type not in self.__weather_icons:
            condition_file_name = weather_type.name.lower()
            self.__weather_icons[weather_type] = load_texture(f"resources/{condition_file_name}.png")

        return self.__weather_icons[weather_type]

