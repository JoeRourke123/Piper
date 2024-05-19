from piper.state import State
from piper.util.tfl_arrival import TflArrival


class TflDataState(State):
    arrivals: [TflArrival]

    def __init__(self):
        self.arrivals = []

    @property
    def arrivals_minutes_string(self):
        return ",\n".join(list(map(lambda a: str(a.minutes_to_arrive), self.arrivals))[:3])
