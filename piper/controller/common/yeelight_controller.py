from datetime import timedelta

from kink import inject
from yeelight import Bulb, discover_bulbs

from piper.controller import PeriodicController
from piper.state.common.yeelight_state import YeelightState
from piper.util.yeelight_bulb import YeelightBulb


@inject
class YeelightController(PeriodicController):
    def __init__(self, yeelight_state: YeelightState):
        super().__init__()
        self.yeelight_state = yeelight_state

    def periodic_update(self):
        if self.yeelight_state.request:
            bulb_ip = self.yeelight_state.request.ip
            bulb = Bulb(bulb_ip)
            bulb.toggle()
            self.yeelight_state.toggle_bulb_power(bulb_ip)
        else:
            self.yeelight_state.bulbs = [YeelightBulb(b) for b in discover_bulbs()]

    @property
    def update_every(self) -> timedelta:
        return timedelta(seconds=5)
