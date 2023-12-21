from datetime import datetime, timedelta

from src.util import HandlerTimer


def timed_handler(timer: HandlerTimer, seconds_pause: int):
    def decorator(function):
        def wrapper(*args, **kwargs):
            time_to_run = timer.last_run + timedelta(seconds=seconds_pause)

            if datetime.now() >= time_to_run:
                return function(*args, **kwargs)
        return wrapper
    return decorator
