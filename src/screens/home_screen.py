from raylib import Fade

from src.handlers.clock_handler import TimeHandler
from src.util import WEATHER_COLOUR_MAP, GREEN_ALT, BLUE_ALT
from src.util.store import Store
from src.screens import Screen

from pyray import *


class HomeScreen(Screen):
    time_handler = TimeHandler()
    tfl_texture: Texture
    play_texture: Texture
    skip_texture: Texture
    next_texture: Texture

    widget_index = 0
    widgets = []

    def __init__(self):
        self.tfl_texture = load_texture("src/resources/tfl.png")
        self.play_texture = load_texture("src/resources/play.png")
        self.pause_texture = load_texture("src/resources/pause.png")
        self.skip_texture = load_texture("src/resources/skip.png")
        self.next_texture = load_texture("src/resources/next.png")

        self.widgets = [self.draw_stock_carousel, self.draw_spotify_carousel, self.draw_monzo_carousel]

    def update(self, ctx: Store):
        self.time_handler.handle(ctx)

        next_btn = Rectangle(420, 60, 50, 170)
        is_clicking = check_collision_point_rec(get_mouse_position(), next_btn) and is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT)

        if is_clicking:
            self.widget_index = (self.widget_index + 1) % len(self.widgets)

    def build(self, ctx: Store):
        draw_text(ctx.get_formatted_hour(), 30, 30, 120, WHITE)
        draw_text(ctx.get_formatted_minute(), 30, 140, 120, WHITE)

        self.draw_tfl_and_weather(ctx)

        self.widgets[self.widget_index](ctx)

    def draw_monzo_carousel(self, ctx: Store):
        draw_rectangle_rounded(
            Rectangle(205, 35, 215, 220),
            0.25,
            0,
            Fade(DARKGRAY, 0.3)
        )
        draw_rectangle_rounded(
            Rectangle(235, 70, 220, 150),
                0.25,
            0,
            BLUE_ALT
        )
        draw_rectangle_rounded(
            Rectangle(200, 30, 220, 220),
            0.25,
            0,
            DARKBLUE
        )
        draw_texture_ex(self.next_texture, Vector2(424, 132), 0, 0.12, Fade(WHITE, 0.5))

        draw_text("Monzo", 225, 50, 18, Fade(WHITE, 0.75))
        draw_text("Spent Today", 225, 75, 24, WHITE)
        draw_text("£8000", 225, 105, 48, WHITE)

        draw_text("Last updated 1hr ago", 225, 200, 14, WHITE)


    def draw_stock_carousel(self, ctx: Store):
        draw_rectangle_rounded(
            Rectangle(205, 35, 215, 220),
            0.25,
            0,
            Fade(DARKGRAY, 0.3)
        )
        draw_rectangle_rounded(
            Rectangle(235, 70, 220, 150),
            0.25,
            0,
            DARKGRAY
        )
        draw_rectangle_rounded(
            Rectangle(200, 30, 220, 220),
            0.25,
            0,
            BLACK
        )
        draw_texture_ex(self.next_texture, Vector2(424, 132), 0, 0.12, GRAY)

        draw_text(ctx.stock_handler.stocks[0].ticker_name, 225, 50, 18, Fade(WHITE, 0.75))
        draw_text(f"${ str(ctx.stock_handler.stocks[0].current_value) }", 225, 81, 48, WHITE)
        draw_text(ctx.stock_handler.stocks[0].get_change_str(), 225, 132, 24, ctx.stock_handler.stocks[0].get_colour())
        draw_text(ctx.stock_handler.stocks[0].get_percentage_str(), 225, 160, 18, ctx.stock_handler.stocks[0].get_colour())

        draw_text(ctx.stock_handler.get_last_run_str(), 225, 200, 14, WHITE)

    def draw_spotify_carousel(self, ctx: Store):
        draw_rectangle_rounded(
            Rectangle(205, 35, 215, 220),
            0.25,
            0,
            Fade(DARKGRAY, 0.3)
        )
        draw_rectangle_rounded(
            Rectangle(235, 70, 220, 150),
                0.25,
            0,
            GREEN_ALT
        )
        draw_rectangle_rounded(
            Rectangle(200, 30, 220, 220),
            0.25,
            0,
            DARKGREEN
        )
        draw_texture_ex(self.next_texture, Vector2(424, 132), 0, 0.12, Fade(WHITE, 0.5))

        draw_text("Spotify", 225, 50, 18, Fade(WHITE, 0.75))
        draw_text(ctx.spotify_handler.get_track_name(), 225, 200, 14, WHITE)
        draw_text(ctx.spotify_handler.get_artist(), 225, 218, 14, LIGHTGRAY)

        draw_texture_ex(self.pause_texture if ctx.spotify_handler.is_playing else self.play_texture, Vector2(215, 82 ), 0, 0.5, WHITE)
        draw_texture_ex(self.skip_texture, Vector2(310, 84 ), 0, 0.5, WHITE)

    def draw_tfl_and_weather(self, ctx):
        if not ctx.tfl_handler.disabled:
            draw_texture_ex(self.tfl_texture, Vector2(30, 275), 0, 0.01, BLUE)
            draw_text(ctx.get_arrivals_string(), 70, 274, 25, WHITE)

        if not ctx.weather_handler.disabled:
            weather_text_width = measure_text(ctx.get_weather_string(), 25)
            draw_text(ctx.get_weather_string(), 450 - weather_text_width, 274, 25,
                      WEATHER_COLOUR_MAP(ctx.get_weather_type()))
