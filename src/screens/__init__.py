from abc import ABC, abstractmethod


class Screen(ABC):
    @abstractmethod
    def update(self, ctx):
        pass

    @abstractmethod
    def build(self, ctx):
        pass
