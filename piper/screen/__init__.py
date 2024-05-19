from abc import ABC, abstractproperty

from piper.controller import Controller
from piper.view import View


class Screen(ABC):
    controller: Controller
    view: View
