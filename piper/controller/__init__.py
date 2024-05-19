from abc import ABC, abstractmethod
from datetime import timedelta, datetime


class Controller(ABC):
    @abstractmethod
    def update(self):
        pass


class PeriodicController(Controller, ABC):
    def __init__(self):
        self.last_updated = datetime.now() - timedelta(days=1)

    @abstractmethod
    def periodic_update(self):
        pass

    @property
    @abstractmethod
    def update_every(self) -> timedelta:
        pass

    def update(self):
        current_date_time = datetime.now()

        should_update = current_date_time >= self.last_updated + self.update_every

        if should_update:
            print(f"Updating Config For: {self.__class__}")
            self.last_updated = current_date_time
            self.periodic_update()
