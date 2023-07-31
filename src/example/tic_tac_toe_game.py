from src.core.game import Game


class TicTacToeGame(Game):
    def initialize(self):
        self.title = "Tic Tac Toe!"
        self.set_screen_size(3, 3)

    def on_mouse_click(self, x: int, y: int):
        self.set_cell(x, y, text="X")

    def on_key_press(self, char: str, keycode: int):
        if 49 <= keycode <= 57:
            self.set_cell_by_index(int(char) - 1, text="X")
