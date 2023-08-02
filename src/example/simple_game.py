from src.core.color import GREEN, RED
from src.core.game import Game


class SimpleGame(Game):
    def initialize(self):
        self.set_title("Simple Game!")
        self.set_screen_size(7, 5)
        self.show_grid(True)

    def on_left_click(self, x: int, y: int):
        self.set_cell(x, y, text="X", color=GREEN)

    def on_right_click(self, x: int, y: int):
        self.set_cell(x, y, text="0", color=RED)

    def on_key_press(self, char: str, keycode: int):
        self.show_message(f'You press: {char}')
