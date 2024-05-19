from pyray import load_font_ex


class FontConfig(object):
    def __init__(self):
        self.__font = None

    @property
    def gogh(self):
        if self.__font is None:
            self.__font = load_font_ex("resources/Gogh.ttf", 150, None, 0)

        return self.__font
