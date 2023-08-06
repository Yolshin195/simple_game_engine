from src.core.game import Game


class Game2048(Game):
    def initialize(self):
        self.set_title("2048")
        self.set_screen_size(4, 4)
        self.show_grid(True)

        self.set_cell(2, 2, text="2048")

    def move(self):
        pass

    def on_key_press(self, char: str, keycode: int):
        match keycode:
            case 38:
                "UP"
            case 40:
                "DOWN"
            case 37:
                "LEFT"
            case 39:
                "RIGHT"
