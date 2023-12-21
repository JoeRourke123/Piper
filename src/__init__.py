from pyray import *

from src.screens.home_screen import HomeScreen
from src.util import DARK_BG
from src.util.store import Store

init_audio_device()

init_window(480, 320, "Piper")

ctx = Store()

ctx.push_screen(HomeScreen())

while not window_should_close():
    # Do updates
    ctx.peek_screen().update(ctx)
    ctx.update()

    # Do drawing
    begin_drawing()
    clear_background(DARK_BG)

    ctx.peek_screen().build(ctx)

    end_drawing()


close_window()