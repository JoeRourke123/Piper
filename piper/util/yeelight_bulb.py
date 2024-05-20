class YeelightBulb(object):
    name: str
    is_on: bool
    brightness: int
    rgb: str

    def __init__(self, name: str, is_on: bool, brightness: int, rgb: str):
        self.name = name
        self.is_on = is_on
        self.brightness = brightness
        self.rgb = rgb
