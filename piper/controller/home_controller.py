from datetime import datetime

from kink import inject

from piper.controller import Controller
from piper.state.common.notion_config_state import NotionConfigState
from piper.state.home_state import HomeState


@inject
class HomeController(Controller):
    def __init__(self, home_state: HomeState, notion_config_state: NotionConfigState):
        self.home_state = home_state
        self.notion = notion_config_state

    def update(self):
        # Update the current display time in the home state
        current_time = datetime.now()
        self.home_state.hour = str(current_time.hour)
        self.home_state.minute = str(current_time.minute).rjust(2, "0")
