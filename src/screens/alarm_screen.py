import os

from src.screens import Screen

from pyray import *

from src.util import TRANSLUCENT


class AlarmScreen(Screen):
    alarm_sound = load_music_stream("alarm.mp3")
    alarm_sound.looping = True

    def update(self, ctx):
        if is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT):
            stop_music_stream(self.alarm_sound)
            ctx.pop_screen()

    def build(self, ctx):
        if not is_music_stream_playing(self.alarm_sound):
            play_music_stream(self.alarm_sound)

        draw_rectangle_gradient_h(0, 0, 480, 320, YELLOW, ORANGE)

        formatted_time = f"{ctx.get_formatted_hour()}:{ctx.get_formatted_minute()}"
        stop_text = "Tap anywhere to stop"

        time_width = measure_text(formatted_time, 120)
        stop_width = measure_text(stop_text, 20)

        draw_text(formatted_time, 440 - time_width, (320 - 120) // 2, 120, WHITE)
        draw_text(stop_text, (480 - stop_width) // 2, 280, 20, TRANSLUCENT)

