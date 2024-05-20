from piper.state import State
from piper.util.yeelight_bulb import YeelightBulb


class YeelightState(State):
    bulbs: [YeelightBulb]

    def __init__(self):
        self.bulbs = []

    def toggle_bulb_power(self, name: str):
        for bulb in self.bulbs:
            if bulb.name == name:
                bulb.is_on = not bulb.is_on
