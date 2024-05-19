from kink import inject
from pyray import init_window, init_audio_device, begin_drawing, end_drawing, window_should_close, set_target_fps

from piper.controller import Controller
from piper.controller.common.common_state_controller import CommonStateController
from piper.controller.common.screen_stack_controller import ScreenStackController
from piper.view import View


@inject
class ApplicationRunner(Controller, View):
    def __init__(self,
                 screen_stack_controller: ScreenStackController,
                 common_state_controller: CommonStateController
                 ):
        self.__screen_stack = screen_stack_controller
        self.__common_state = common_state_controller
        init_audio_device()
        init_window(480, 320, "Piper")
        set_target_fps(12)

    def run(self):
        while not window_should_close():
            begin_drawing()

            self.update()
            self.draw()

            end_drawing()

    def update(self):
        self.__common_state.update()
        self.__screen_stack.update()

    def draw(self):
        current_screen = self.__screen_stack.top
        current_screen.view.draw()