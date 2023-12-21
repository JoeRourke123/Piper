from src.handlers.timed_handler import TimedHandler


class ConfigHandler(TimedHandler):
    @property
    def seconds_pause(self) -> int:
        return 120

    def handle(self, ctx):
        if super().handle(ctx):
            print("Fetching config map...")
            ctx.configs = ctx.db.get_config_map()
            print(ctx.configs)