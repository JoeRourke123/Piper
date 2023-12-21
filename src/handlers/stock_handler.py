import requests
from pyray import GREEN, RED

from src.handlers.timed_handler import TimedHandler


class Stocks(object):
    ticker_name: str
    current_value: float
    change: float
    percentage_change: float

    def __init__(self, ticker_name: str, current_value: float, change: float):
        self.ticker_name = ticker_name
        self.current_value = round(current_value, 2)
        self.change = round(change, 2)

        percentage_change = (1 - ((current_value - change) / current_value)) * 100
        self.percentage_change = round(percentage_change, 2)

    def get_change_str(self):
        if self.change > 0:
            return f"+${ str(self.change) }"
        else:
            return f"-${ str(self.change) }"

    def get_percentage_str(self):
        if self.change > 0:
            return f"+{ str(self.percentage_change) }%"
        else:
            return f"-{ str(self.percentage_change) }%"

    def get_colour(self):
        return GREEN if self.change > 0 else RED


class StockHandler(TimedHandler):
    stocks: [Stocks] = []

    @property
    def seconds_pause(self) -> int:
        return 360

    def handle(self, ctx):
        if super().handle(ctx):
            stocks_endpoint = ctx.get_config("stock_endpoint_url")
            stocks_response = requests.get(stocks_endpoint).json()

            self.stocks = list(map(lambda s: Stocks(
                s["symbol"],
                s["price"],
                s["changes"]
            ), stocks_response))

