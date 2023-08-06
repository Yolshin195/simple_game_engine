from src.core.game import Game


class CalculatorGame(Game):
    def initialize(self):
        self.set_title("Calculator")
        self.set_screen_size(5, 1)
        self.show_grid(True)

        self.set_cell(0, 0, text="A")
        self.set_cell(1, 0, text="+")
        self.set_cell(2, 0, text="B")
        self.set_cell(3, 0, text="=")
        self.set_cell(4, 0, text="C")
