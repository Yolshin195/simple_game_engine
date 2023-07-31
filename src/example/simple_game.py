from src.core.color import GREEN
from src.core.game import Game


class SimpleGame(Game):
    def initialize(self):
        self.title = "Simple Game!"
        self.set_screen_size(3, 3)

    def on_mouse_click(self, x: int, y: int):
        pass
