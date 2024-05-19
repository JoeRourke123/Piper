from piper.controller.home_controller import HomeController
from piper.screen import Screen
from piper.view.home_view import HomeView


class HomeScreen(Screen):
    def __init__(self):
        self.controller = HomeController()
        self.view = HomeView()
