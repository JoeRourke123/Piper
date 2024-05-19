from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def draw(self):
        pass
