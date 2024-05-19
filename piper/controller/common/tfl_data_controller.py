from datetime import timedelta

import requests
from kink import inject

from piper.controller import PeriodicController
from piper.state.common.notion_config_state import NotionConfigState
from piper.state.common.tfl_data_state import TflDataState
from piper.util.tfl_arrival import TflArrival


@inject
class TflDataController(PeriodicController):
    def __init__(self, notion_config: NotionConfigState, tfl_data: TflDataState):
        super().__init__()
        self.notion_config = notion_config
        self.tfl_data = tfl_data

    def periodic_update(self):
        tfl_url = self.notion_config.get_config("tfl_endpoint_url")
        platform_name = self.notion_config.get_config("tfl_platform_name")
        line_id = self.notion_config.get_config("tfl_line_id")
        min_distance_in_seconds = self.notion_config.get_config("tfl_min_distance", config_type=int) * 60

        arrivals_response = requests.get(tfl_url, headers={"Cache-Control": "no-cache"}).json()
        filtered_arrivals = []

        for arrival in arrivals_response:
            if arrival["platformName"] == platform_name and arrival["lineId"] == line_id and arrival["timeToStation"] >= min_distance_in_seconds:
                filtered_arrivals.append(TflArrival.build(arrival))

        filtered_arrivals = sorted(filtered_arrivals, key=lambda ar: ar.minutes_to_arrive)
        self.tfl_data.arrivals = filtered_arrivals

    @property
    def update_every(self) -> timedelta:
        return timedelta(seconds=45)
