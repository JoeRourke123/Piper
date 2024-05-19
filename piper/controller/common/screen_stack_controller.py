from collections import deque

from piper.controller import Controller
from piper.screen import Screen


class ScreenStackController(Controller):
    def __init__(self, initial_screen: Screen):
        self.__stack = deque[Screen]()
        self.__stack.append(initial_screen)

    @property
    def top(self) -> Screen:
        return self.__stack[0]

    def go(self, screen: Screen):
        self.__stack.append(screen)

    def back(self):
        self.__stack.pop()

    def update(self):
        for screen in self.__stack:
            screen.controller.update()
