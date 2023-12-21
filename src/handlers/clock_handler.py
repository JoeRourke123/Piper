from datetime import datetime

from src.handlers.base_handler import BaseHandler
from src.util import store


class TimeHandler(BaseHandler):
    def handle(self, ctx: store):
        ctx.current_time = datetime.now()