class YeelightBulb(object):
    ip: str
    name: str
    is_on: bool
    brightness: int
    rgb: str

    def __init__(self, ip: str, name: str, is_on: bool, brightness: int, rgb: str):
        self.ip = ip
        self.name = name
        self.is_on = is_on
        self.brightness = brightness
        self.rgb = rgb

    def __init__(self, yeelight_bulb_object: dict):
        bulb_capabilities = yeelight_bulb_object["capabilities"]
        self.name = bulb_capabilities["name"]
        self.is_on = bulb_capabilities["power"] == "on"
        self.brightness = bulb_capabilities["brightness"]
        self.rgb = bulb_capabilities["rgb"]

    def build(self, ip=None, name=None, is_on=None, brightness=None, rgb=None):
        if ip is None:
            ip = self.ip
        if name is None:
            name = self.name
        if is_on is None:
            is_on = self.is_on
        if brightness is None:
            brightness = self.brightness
        if rgb is None:
            rgb = self.rgb

        return YeelightBulb(ip, name, is_on, brightness, rgb)
