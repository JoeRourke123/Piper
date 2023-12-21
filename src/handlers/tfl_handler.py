from datetime import datetime

import requests
from math import floor

from src.handlers.timed_handler import TimedHandler

class Arrivals:
    time_to_station: int
    expected_arrival: datetime
    current_location: str
    towards: str

    def __init__(self, time_to_station: int, expected_arrival: str, current_location: str, towards: str):
        self.towards = towards
        self.time_to_station = time_to_station
        self.expected_arrival = datetime.fromisoformat(expected_arrival)
        self.current_location = current_location

    def __str__(self):
        return f"{ self.towards }          { self.mins_to_arrival } mins (Currently at { self.current_location })"

    @property
    def mins_to_arrival(self) -> int:
        return floor(self.time_to_station / 60)

class TflHandler(TimedHandler):
    arrivals: [Arrivals]

    @property
    def seconds_pause(self) -> int:
        return 30

    def handle(self, ctx):
        if super().handle(ctx):
            tfl_url = ctx.get_config("tfl_endpoint_url")
            platforn_name = ctx.get_config("tfl_platform_name")
            line_id = ctx.get_config("tfl_line_id")
            minimum_distance_in_mins = int(ctx.get_config("tfl_min_distance"))
            min_distance_in_secs = minimum_distance_in_mins * 60

            self.arrivals = []
            arrivals = requests.get(tfl_url, headers={"Cache-Control": "no-cache"}).json()

            for arrival in arrivals:
                if arrival["platformName"] == platforn_name and arrival["lineId"] == line_id and arrival["timeToStation"] >= min_distance_in_secs:
                    self.arrivals.append(Arrivals(
                        arrival["timeToStation"],
                        arrival["expectedArrival"],
                        arrival["currentLocation"],
                        arrival["towards"]
                    ))