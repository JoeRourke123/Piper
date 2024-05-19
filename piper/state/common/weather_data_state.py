from piper.state import State


class WeatherDataState(State):
    conditions: str
    temperature: int

    def __init__(self):
        self.conditions = "clear"
        self.temperature = 0
