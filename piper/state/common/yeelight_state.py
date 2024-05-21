from piper.state import State
from piper.util.yeelight_bulb import YeelightBulb


class YeelightState(State):
    bulbs: dict[str, YeelightBulb]
    request: YeelightBulb

    def __init__(self):
        self.bulbs = []

    def toggle_bulb_power(self, ip: str):
        for ip, bulb in self.bulbs.items():
            if bulb.ip == ip:
                bulb.is_on = not bulb.is_on
