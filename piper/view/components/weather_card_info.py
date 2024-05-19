from kink import inject
from pyray import draw_text_ex, ORANGE, Vector2, draw_texture_ex

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

        draw_texture_ex(weather_conditions_texture, Vector2(235, 100), 0, 1, ORANGE)
        draw_text_ex(self.font_config.gogh, self.temperature(), Vector2(240, 210), 40, 0, ORANGE)

    def temperature(self):
        return f"{self.weather_data.temperature} degrees"

    def update(self):
        pass
