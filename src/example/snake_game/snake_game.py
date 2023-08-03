from src.core.color import GREEN, RED
from src.core.game import Game


class SnakeGame(Game):
    APPLE = "\U0001F34E"
    SNAKE_HEAD = "\U0001F440"
    SNAKE_BODY = "\U0001F534"

    def initialize(self):
        self.set_title("Snake Game!")
        self.set_screen_size(9, 9, 50)
        self.show_grid(True)

        self.set_cell(4, 4, text=self.APPLE, text_color=RED)
        self.set_cell(3, 3, text=self.SNAKE_HEAD)
        self.set_cell(3, 2, text=self.SNAKE_BODY, text_color=GREEN)
        self.set_cell(3, 2, text=self.SNAKE_BODY, text_color=GREEN)
        self.set_cell(4, 2, text=self.SNAKE_BODY, text_color=GREEN)
        self.set_cell(5, 2, text=self.SNAKE_BODY, text_color=GREEN)
        self.set_cell(5, 1, text=self.SNAKE_BODY, text_color=GREEN)
