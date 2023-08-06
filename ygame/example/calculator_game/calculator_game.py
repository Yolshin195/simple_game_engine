from ygame.core.color import GREEN
from ygame.core.game import Game
from ygame.example.calculator_game.variable import Variable


class CalculatorGame(Game):
    def initialize(self):
        self.set_title("Calculator")
        self.set_screen_size(5, 1)
        self.show_grid(True)

        box = Variable(0, 0)
        box.text = "Y"
        box.color = GREEN
        self.draw_variable(box)

    def set_default_value(self):
        self.set_cell(0, 0, text="A")
        self.set_cell(1, 0, text="+")
        self.set_cell(2, 0, text="B")
        self.set_cell(3, 0, text="=")
        self.set_cell(4, 0, text="C")

    def draw_variable(self, variable: Variable):
        self.set_cell(variable.x, variable.y, text=variable.text, color=variable.color)
