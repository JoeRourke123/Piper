from pyray import load_texture


class TextureConfig(object):
    def __init__(self):
        self.__tfl_icon_texture = None

    @property
    def tfl_icon(self):
        if self.__tfl_icon_texture is None:
            self.__tfl_icon_texture = load_texture("resources/tfl.png")

        return self.__tfl_icon_texture
