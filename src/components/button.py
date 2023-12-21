from pyray import Color, draw_circle_gradient, get_mouse_position, is_mouse_button_pressed, MouseButton

from src.util.store import Store
from src.screens import Screen


class Button(object):
    def __init__(self, x: int, y: int, radius: float, colour_one: Color, colour_two: Color, screen: Screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour_one = colour_one
        self.colour_two = colour_two
        self.screen = screen

    def draw(self):
        draw_circle_gradient(self.x, self.y, self.radius, self.colour_one, self.colour_two)

    def was_clicked(self):
        mouse_position = get_mouse_position();

        within_x_bounds = self.x - (self.radius) < mouse_position.x < self.x + self.radius
        within_y_bounds = self.y - (self.radius) < mouse_position.y < self.y + self.radius

        return within_x_bounds and within_y_bounds and is_mouse_button_pressed(MouseButton.MOUSE_BUTTON_LEFT);

    def click_check(self, ctx: Store):
        if self.was_clicked():
            ctx.push_screen(self.screen)