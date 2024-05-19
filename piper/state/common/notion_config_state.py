from datetime import datetime, timedelta

from piper.state import State


class NotionConfigState(State):
    def __init__(self):
        self.config_store = {}

    def get_config(self, key: str, config_type=str):
        return config_type(self.config_store.get(key))

    def update_config(self, updated_config_store):
        self.config_store = updated_config_store
