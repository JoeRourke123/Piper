import os
from datetime import datetime

from notion_client import Client

from src.util import compare_times


class PiperDB:
    __nc = Client(auth=os.environ["NOTION_TOKEN"])

    @property
    def alarms(self):
        return self.__nc.databases.query("69c3e55d5c1845a386183577ac73abf0", filter={
            "property": "type",
            "multi_select": {
                "contains": "alarm"
            }
        })

    @property
    def configs(self):
        return self.__nc.databases.query("69c3e55d5c1845a386183577ac73abf0", **{
            "filter": {
                "property": "type",
                "multi_select": {
                    "contains": "config"
                }
            }
        })

    def is_active_alarm(self, now: datetime, alarm_store=alarms):
        for alarm in alarm_store["results"]:
            alarm_time = datetime(now.year, now.month, now.day, alarm["properties"]["hour"]["number"],
                                  alarm["properties"]["minute"]["number"])
            current_day = now.strftime('%a')

            if not compare_times(alarm_time, now) and current_day in map(lambda d: d["name"], alarm["properties"]["days"]["multi_select"]):
                return True

        return False

    def get_config_map(self):
        config_entries = self.configs["results"]

        return {r["properties"]["title"]["title"][0]["plain_text"]: r["properties"]["value"]["rich_text"][0]["plain_text"] for r
                in config_entries}
