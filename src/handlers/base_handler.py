from abc import ABC, abstractmethod

from src.util import HandlerTimer


class BaseHandler(ABC):
    handler_timer = HandlerTimer()
    disabled = False

    @abstractmethod
    def handle(self, ctx):
        pass
