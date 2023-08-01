from src.core.game import Game


class TicTacToeGame(Game):
    def initialize(self):
        self.set_title("Tic Tac Toe!")
        self.set_screen_size(3, 3)

    def on_left_click(self, x: int, y: int):
        self.set_cell(x, y, text="X")

    def on_right_click(self, x: int, y: int):
        self.set_cell(x, y, text="0")

    def on_key_press(self, char: str, keycode: int):
        pass
