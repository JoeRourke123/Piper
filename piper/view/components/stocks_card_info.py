from kink import inject
from pyray import draw_text_ex, Vector2, GREEN

from piper.util.font_config import FontConfig
from piper.util.texture_config import TextureConfig
from piper.view.components import Component


@inject
class StocksCardInfo(Component):
    def __init__(self, font_config: FontConfig, texture_config: TextureConfig):
        self.font_config = font_config
        self.texture_config = texture_config

    def draw_component(self):
        draw_text_ex(self.font_config.gogh, "STOCKS", Vector2(240, 210), 40, 0, GREEN)

    def update(self):
        pass
