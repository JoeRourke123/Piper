from kink import di

from piper.controller.common.common_state_controller import CommonStateController
from piper.controller.common.notion_config_controller import NotionConfigController
from piper.controller.common.screen_stack_controller import ScreenStackController
from piper.controller.common.tfl_data_controller import TflDataController
from piper.controller.common.weather_data_controller import WeatherDataController
from piper.screen.home_screen import HomeScreen
from piper.state.common.notion_config_state import NotionConfigState
from piper.state.common.tfl_data_state import TflDataState
from piper.state.common.weather_data_state import WeatherDataState
from piper.state.home_state import HomeState
from piper.util.font_config import FontConfig
from piper.util.texture_config import TextureConfig


def bootstrap_di():
    # Page States
    di[HomeState] = HomeState()

    # States and Controllers for Common State Objects
    di[NotionConfigState] = NotionConfigState()
    di[NotionConfigController] = NotionConfigController()
    di[TflDataState] = TflDataState()
    di[TflDataController] = TflDataController()
    di[WeatherDataState] = WeatherDataState()
    di[WeatherDataController] = WeatherDataController()

    # Global Top-Level Controllers
    di[FontConfig] = FontConfig()
    di[TextureConfig] = TextureConfig()
    di[ScreenStackController] = ScreenStackController(initial_screen=HomeScreen())
    di[CommonStateController] = CommonStateController()

