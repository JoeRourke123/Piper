from kink import inject
from pyray import set_text_line_spacing, draw_text_ex, draw_texture_ex, Vector2, BLUE, DARKGRAY

from piper.state.common.tfl_data_state import TflDataState
from piper.util.font_config import FontConfig
from piper.util.texture_config import TextureConfig
from piper.view.components import Component


@inject
class TflCardInfo(Component):
    def __init__(self, font_config: FontConfig, tfl_data: TflDataState, texture_config: TextureConfig):
        self.font_config = font_config
        self.tfl_data = tfl_data
        self.texture_config = texture_config

        self.arrivals_string = "No services"
        self.arrivals_position = Vector2(240, 210)

    @staticmethod
    def build() -> ['Component']:
        return [TflCardInfo()]

    def draw_component(self):
        tfl_texture = self.texture_config.tfl_icon

        set_text_line_spacing(30)

        draw_text_ex(self.font_config.gogh, self.arrivals_string, self.arrivals_position, 40, 0, DARKGRAY)
        draw_texture_ex(tfl_texture, Vector2(380, 60), 0, 0.015, BLUE)

    def update(self):
        if not self.tfl_data.arrivals:
            self.arrivals_string = "No services"
            self.arrivals_position = Vector2(240, 210)
        else:
            self.arrivals_string = f"In\n{self.tfl_data.arrivals_minutes_string} mins"
            arrivals_line_count = len(self.tfl_data.arrivals) + 1
            self.arrivals_position = Vector2(240, 240 - (arrivals_line_count * 30))
