from datetime import datetime
from math import floor

from dateutil.parser import parse


class TflArrival(object):
    time_to_station: int
    expected_arrival: datetime
    current_location: str
    towards: str

    def __init__(self, time_to_station: int, expected_arrival: str, current_location: str, towards: str):
        self.towards = towards
        self.time_to_station = time_to_station
        self.expected_arrival = parse(expected_arrival)
        self.current_location = current_location

    def __str__(self):
        return f"{ self.towards }          { self.mins_to_arrival } mins (Currently at { self.current_location })"

    @property
    def minutes_to_arrive(self) -> int:
        return floor(self.time_to_station / 60)

    @staticmethod
    def build(arrival):
        return TflArrival(
            arrival["timeToStation"],
            arrival["expectedArrival"],
            arrival["currentLocation"],
            arrival["towards"]
        )