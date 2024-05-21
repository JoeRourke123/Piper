from abc import ABC, abstractmethod

from pyray import is_mouse_button_down, MouseButton, Vector2, get_mouse_position, Rectangle, check_collision_point_rec, \
    is_mouse_button_pressed

from piper.controller import Controller
from piper.view import View


class Component(View, Controller, ABC):
    @abstractmethod
    def draw_component(self):
        pass

    @staticmethod
    @abstractmethod
    def build() -> ['Component']:
        pass

    def draw(self):
        self.update()
        self.draw_component()


class ClickableComponent(Component, ABC):
    @property
    @abstractmethod
    def collision_area(self) -> Rectangle:
        pass

    @abstractmethod
    def on_click(self):
        pass

    def update_component(self):
        pass

    def update(self):
        self.detect_clicking()
        self.update_component()

    def detect_clicking(self):
        current_mouse_position = get_mouse_position()
        is_in_area = check_collision_point_rec(current_mouse_position, self.collision_area)
        is_clicking = is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT)

        if is_in_area and is_clicking:
            self.on_click()


class SwipableComponent(Component, ABC):
    SWIPING_THRESHOLD = 40

    def __init__(self):
        self.is_mouse_down = False
        self.starting_mouse_position = Vector2(0, 0)

    @property
    @abstractmethod
    def collision_area(self) -> Rectangle:
        pass

    def update_component(self):
        pass

    def update(self):
        self.detect_swiping()
        self.update_component()

    def detect_swiping(self):
        current_mouse_position = get_mouse_position()
        current_mouse_down = is_mouse_button_down(MouseButton.MOUSE_BUTTON_LEFT)

        if self.is_mouse_down and not current_mouse_down:
            direction_map = {
                "LEFT":  self.starting_mouse_position.x - self.SWIPING_THRESHOLD < current_mouse_position.x,
                "RIGHT":  self.starting_mouse_position.x + self.SWIPING_THRESHOLD > current_mouse_position.x,
                "UP": self.starting_mouse_position.y - self.SWIPING_THRESHOLD > current_mouse_position.y,
                "DOWN": self.starting_mouse_position.y + self.SWIPING_THRESHOLD < current_mouse_position.y
            }
            direction_map = {dir: val for dir,val in direction_map.items() if val}

            if len(direction_map) == 1:
                if "LEFT" in direction_map:
                    self.on_swipe_left()
                elif "RIGHT" in direction_map:
                    self.on_swipe_right()
                elif "UP" in direction_map:
                    self.on_swipe_up()
                elif "DOWN" in direction_map:
                    self.on_swipe_down()

            self.is_mouse_down = False
        elif not self.is_mouse_down and current_mouse_down:
            is_touching_component = check_collision_point_rec(current_mouse_position, self.collision_area)

            if is_touching_component:
                self.is_mouse_down = True
                self.starting_mouse_position = current_mouse_position

    def on_swipe_left(self):
        pass

    def on_swipe_right(self):
        pass

    def on_swipe_up(self):
        pass

    def on_swipe_down(self):
        pass
