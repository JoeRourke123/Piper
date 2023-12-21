from datetime import datetime

from src.handlers.base_handler import BaseHandler
from src.handlers.timed_handler import TimedHandler

from src.screens.alarm_screen import AlarmScreen
from src.util import compare_times


class AlarmHandler(TimedHandler):
    alarm_cache = []

    @property
    def seconds_pause(self) -> int:
        return 600

    active_alarm = datetime(1970, 1, 1)

    def handle(self, ctx):
        if super().handle(ctx):
            print("Refreshing alarm cache...")
            self.alarm_cache = ctx.db.alarms

        current_time: datetime = ctx.current_time

        if compare_times(current_time, self.active_alarm):
            if ctx.db.is_active_alarm(current_time, self.alarm_cache):
                self.active_alarm = current_time
                ctx.push_screen(AlarmScreen())