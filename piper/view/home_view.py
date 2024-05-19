from kink import inject
from pyray import draw_rectangle_gradient_h, ORANGE, PINK, WHITE, draw_text_ex, Vector2, draw_rectangle_rounded, \
    Rectangle

from piper.state.home_state import HomeState
from piper.util.font_config import FontConfig
from piper.view import View
from piper.view.components.dimmed_home_component import DimmedHomeComponent
from piper.view.components.home_screen_card import HomeScreenCard


@inject
class HomeView(View):
    def __init__(self, home_state: HomeState, font_config: FontConfig):
        self.home_state = home_state
        self.font_config = font_config
        self.font = None

        self.home_screen_card = HomeScreenCard()
        self.dimmed_home_component = DimmedHomeComponent()

    def draw(self):
        if self.font is None:
            self.font = self.font_config.gogh
        if self.home_state.is_dimmed:
            self.dimmed_home_component.draw()
            return

        self.draw_background()
        self.draw_clock(self.home_state.hour, self.home_state.minute)
        self.draw_card()

    def draw_clock(self, hour, minute):
        draw_text_ex(self.font, hour, Vector2(30, 40), 150, 0, WHITE)
        draw_text_ex(self.font, minute, Vector2(30, 130), 150, 0, WHITE)

    @staticmethod
    def draw_background():
        draw_rectangle_gradient_h(0, 0, 480, 320, ORANGE, PINK)

    def draw_card(self):
        self.home_screen_card.draw()
