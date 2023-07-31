# simple_game_engine
![Иллюстрация к проекту](https://github.com/Yolshin195/simple_game_engine/blob/main/source/ticTacToeGame.png)

## Methods for Game
```python
class Game:
    def initialize(self):
        pass
    
    def set_screen_size(self, width: int, height: int):
        pass
    
    def show_grid(self, flag: bool):
        pass

    def set_cell(self, x: int, y: int, color=None, text=None):
        pass

    def get_cell(self, x: int, y: int):
        pass

    def on_mouse_click(self, x: int, y: int):
        pass

    def on_key_press(self, char: str, keycode: int):
        pass

    def on_key_release(self, char: str, keycode: int):
        pass
```