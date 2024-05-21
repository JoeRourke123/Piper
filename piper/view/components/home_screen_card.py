from collections import deque

from kink import inject
from pyray import draw_rectangle_rounded, Rectangle, WHITE, draw_text_ex, Vector2, GREEN

from piper.util.font_config import FontConfig
from piper.util.texture_config import TextureConfig
from piper.view.components import Component, SwipableComponent
from piper.view.components.stocks_card_info import StocksCardInfo
from piper.view.components.tfl_card_info import TflCardInfo
from piper.view.components.weather_card_info import WeatherCardInfo


@inject
class HomeScreenCard(SwipableComponent):
    @property
    def collision_area(self) -> Rectangle:
        return Rectangle(200, 20, 260, 280)

    def __init__(self, font_config: FontConfig, texture_config: TextureConfig):
        super().__init__()
        self.font_config = font_config
        self.texture_config = texture_config
        self.card_queue = deque[Component]([
            *TflCardInfo.build(),
            *WeatherCardInfo.build(),
            *StocksCardInfo.build(),
            *YeelightCardInfo.build(),
        ])

    def draw_component(self):
        draw_rectangle_rounded(self.collision_area, 0.6, 60, WHITE)

        draw_current_card = self.card_queue[0]
        draw_current_card.draw()

    def on_swipe_left(self):
        self.card_queue.append(self.card_queue.popleft())

    def on_swipe_right(self):
        self.card_queue.insert(0, self.card_queue.pop())

    def draw_stocks_info(self):
        draw_text_ex(self.font_config.gogh, "STONKS", Vector2(240, 210), 40, 0, GREEN)

    @staticmethod
    def build() -> ['Component']:
        return [HomeScreenCard()]
