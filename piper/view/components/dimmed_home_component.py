from kink import inject
from pyray import Rectangle, draw_rectangle_rec, BLACK, draw_text_ex, WHITE, Vector2

from piper.state.home_state import HomeState
from piper.util.font_config import FontConfig
from piper.view.components import ClickableComponent


@inject
class DimmedHomeComponent(ClickableComponent):
    def __init__(self, home_state: HomeState, font_config: FontConfig):
        self.home_state = home_state
        self.font_config = font_config

    @property
    def collision_area(self) -> Rectangle:
        return Rectangle(0, 0, 480, 320)

    def on_click(self):
        self.home_state.is_dimmed = False

    def draw_component(self):
        draw_rectangle_rec(self.collision_area, BLACK)

        font = self.font_config.gogh
        draw_text_ex(font, self.home_state.hour, Vector2(30, 40), 150, 0, WHITE)
        draw_text_ex(font, self.home_state.minute, Vector2(30, 130), 150, 0, WHITE)

    @staticmethod
    def build():
        return [DimmedHomeComponent()]