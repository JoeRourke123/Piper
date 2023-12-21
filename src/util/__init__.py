from datetime import datetime

from pyray import Color, WHITE

DARK_BG = Color(20, 20, 20, 255)

TRANSLUCENT = Color(20, 20, 20, 60)

GREEN_ALT = Color(0, 102, 0, 255)
BLUE_ALT = Color(0, 51, 102, 255)

TIME_FORMAT_STR = "%I:%M%p on %B %d, %Y"

WEATHER_COLOUR_MAP = lambda weather: {
    "clouds": Color(180, 180, 180, 255),
    "rain": Color(134, 219, 255, 255),
    "drizzle": Color(204, 255, 255, 255),
    "clear": Color(238, 158, 54, 255),
    "thunderstorm": Color(255, 255, 204, 255)
}.get(weather, WHITE)

class HandlerTimer:
    last_run: datetime

    def update(self):
        self.last_run = datetime.now()


def compare_times(current_time, active_alarm_time):
    return active_alarm_time.strftime(TIME_FORMAT_STR) != current_time.strftime(TIME_FORMAT_STR)