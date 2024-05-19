from kink import inject

from piper.controller import Controller
from piper.controller.common.notion_config_controller import NotionConfigController
from piper.controller.common.tfl_data_controller import TflDataController
from piper.controller.common.weather_data_controller import WeatherDataController


@inject
class CommonStateController(Controller):
    controllers: [Controller]

    def __init__(
        self,
        notion_config_controller: NotionConfigController,
        tfl_data_controller: TflDataController,
        weather_data_controller: WeatherDataController
    ):
        self.controllers = [
            notion_config_controller,
            tfl_data_controller,
            weather_data_controller
        ]

    def update(self):
        for controller in self.controllers:
            controller.update()
