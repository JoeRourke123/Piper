from src.screens import Screen

from pyray import draw_text, WHITE


class TimerScreen(Screen):
    def update(self, ctx):
        pass

    def build(self, ctx):
        draw_text("TIMER", 20, 20, 100, WHITE)