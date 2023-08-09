# Your Game
[Русский](docs/README-ru.md)

Your Game (ygame) is simple game engine for start learning programming. 
The playing field consists of cells

## Installation
```commandline
    pip install ygame
```

## Hello, world!
```python
from ygame.core.color import GREEN, RED
from ygame.core.game import Game


class SimpleGame(Game):
    def initialize(self):
        self.set_title("Simple Game!")
        self.set_screen_size(3, 3)
        self.show_grid(True)

        self.set_turn_timer(500)

    def on_turn(self, step: int):
        color = GREEN if step % 2 == 0 else RED
        self.set_cell(1, 1, text=step, color=color)

        if step == 10:
            self.stop_turn_timer()

```

### Launch
```python
from ygame.example.simple_game.simple_game import SimpleGame
from ygame.tkinter.game_engine_tkinter import GameEngineTkinter


def main():
    GameEngineTkinter(SimpleGame()).initialize()


if __name__ == "__main__":
    main()
```

## Methods for Game

```python
from abc import ABC, abstractmethod

from ygame.core.cell import Cell
from ygame.core.color import Color
from ygame.core.game_engine import GameEngine


class Game(ABC):
    @abstractmethod
    def initialize(self):
        pass

    def set_title(self, title: str):
        pass

    def set_screen_size(self, width: int, height: int):
        pass

    def show_grid(self, flag: bool):
        pass

    def show_message(self, text: str):
        pass

    def set_cell(self, x: int, y: int, color=None, text=None):
        pass

    def get_cell_color(self, x: int, y: int) -> Color:
        pass

    def get_cell_text(self, x: int, y: int) -> str:
        pass

    def set_turn_timer(self, interval_ms: int):
        pass

    def stop_turn_timer(self):
        pass

    def on_turn(self, step: int):
        """
        :param step: step counting starts from one
        :return: None
        """

    def on_left_click(self, x: int, y: int):
        pass

    def on_right_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass
```

## Example:
1. [Calculator Game](/ygame/example/calculator_game/README.md)
1. [Tic Tac Toe Game](/ygame/example/tic_tac_toe_game/README.md)
2. [Snake Game](/ygame/example/snake_game/README.md)
3. [2048 Game](/ygame/example/game_2048/README.md)


## License
This project is licensed under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.