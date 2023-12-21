from datetime import datetime, timedelta

from src.handlers.base_handler import BaseHandler
from abc import abstractmethod


class TimedHandler(BaseHandler):
    last_run = datetime(1970, 1, 1)

    @property
    @abstractmethod
    def seconds_pause(self) -> int:
        pass

    def handle(self, ctx):
        current_time = datetime.now()

        if self.last_run + timedelta(seconds=self.seconds_pause) >= current_time or self.disabled:
            return False

        self.last_run = current_time
        return True

    def get_last_run_str(self) -> str:
        current_time = datetime.now()
        time_diff = (current_time - self.last_run).total_seconds()
        min_diff = round(time_diff // 60)

        if min_diff > 0:
            return f"Last updated { min_diff } min ago"
        else:
            return "Last updated now"