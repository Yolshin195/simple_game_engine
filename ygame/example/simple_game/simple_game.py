# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

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
