from src.core.color import GREEN, RED, BLACK
from src.core.game import Game


class SimpleGame(Game):
    def initialize(self):
        self.set_title("Simple Game!")
        self.set_screen_size(3, 3)
        self.show_grid(True)

        self.set_cell(0, 0, text="W", color=BLACK)

        self.set_turn_timer(1000)

    def on_left_click(self, x: int, y: int):
        self.set_cell(x, y, text="X", color=GREEN)

    def on_right_click(self, x: int, y: int):
        self.set_cell(x, y, text="0", color=RED)

    def on_key_press(self, char: str, keycode: int):
        pass

    def on_turn(self, step: int):
        if step % 2 == 0:
            self.set_cell(1, 1, text="X", color=GREEN)
        else:
            self.set_cell(1, 1, text="0", color=RED)

        if step == 10:
            self.stop_turn_timer()
