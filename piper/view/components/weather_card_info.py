from kink import inject
from pyray import draw_text_ex, ORANGE, Vector2, draw_texture_ex, DARKGRAY

from piper.state.common.weather_data_state import WeatherDataState
from piper.util.font_config import FontConfig
from piper.util.texture_config import TextureConfig
from piper.view.components import Component


@inject
class WeatherCardInfo(Component):
    def __init__(
        self,
        weather_data: WeatherDataState,
        font_config: FontConfig,
        texture_config: TextureConfig
    ):
        self.weather_data = weather_data
        self.font_config = font_config
        self.texture_config = texture_config

    def draw_component(self):
        weather_conditions_texture = self.texture_config.weather_icon(self.weather_data.conditions)

        draw_texture_ex(weather_conditions_texture, Vector2(235, 90), 0, 1, ORANGE)
        draw_text_ex(self.font_config.gogh, self.temperature, Vector2(240, 190), 40, 0, ORANGE)
        draw_text_ex(self.font_config.gogh, self.min_max_temperature, Vector2(245, 235), 24, 0, DARKGRAY)

    @property
    def temperature(self):
        return f"{self.weather_data.temperature} degrees"

    @property
    def min_max_temperature(self):
        return f"l:{self.weather_data.min_temperature} h:{self.weather_data.max_temperature}"

    def update(self):
        pass
