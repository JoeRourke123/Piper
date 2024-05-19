import os
from datetime import timedelta

from kink import inject
from notion_client import Client

from piper.controller import PeriodicController
from piper.state.common.notion_config_state import NotionConfigState


@inject
class NotionConfigController(PeriodicController):
    def __init__(self, notion_config_state: NotionConfigState):
        super().__init__()
        self.__notion_client = Client(auth=os.environ["NOTION_TOKEN"])
        self.notion_config_state = notion_config_state

    @property
    def update_every(self) -> timedelta:
        return timedelta(minutes=2)

    def periodic_update(self):
        config_db = self.__get_config_map()

        self.notion_config_state.update_config(config_db)

    def __get_config_map(self):
        config_db = self.__fetch_config_db()
        return self.__get_map_from_results(config_db)

    def __fetch_config_db(self):
        return self.__notion_client.databases.query("69c3e55d5c1845a386183577ac73abf0", **{
            "filter": {
                "property": "type",
                "multi_select": {
                    "contains": "config"
                }
            }
        })

    @staticmethod
    def __get_map_from_results(config_db):
        config_entries = config_db["results"]

        return {
            r["properties"]["title"]["title"][0]["plain_text"]: r["properties"]["value"]["rich_text"][0]["plain_text"]
            for r
            in config_entries}