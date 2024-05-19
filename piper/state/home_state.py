from piper.state import State


class HomeState(State):
    def __init__(self):
        self.is_dimmed = True

        self.hour = "00"
        self.minute = "00"
