# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.
from ygame.core.color import WHITE
from ygame.core.game import Game
from ygame.example.game_2048.map import Map


class Game2048(Game):
    width = 4
    height = 4
    map_game = None

    def initialize(self):
        self.set_title("2048")
        self.set_screen_size(4, 4)

        self.start()

    def start(self):
        self.map_game = Map(self.width, self.height)
        self.random()
        self.random()
        self.draw()

    def random(self):
        x = self.get_random_number(0, self.width-1)
        y = self.get_random_number(0, self.height-1)

        if not self.map_game.set(x, y, 2):
            return self.random()

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                self.set_cell(x, y, text=self.map_game.get(x, y, ""), color=WHITE)

    def on_key_press(self, char: str, keycode: int):
        match keycode:
            case 38:
                self.map_game.move_up()
                self.map_game.merge_up()
                self.map_game.move_up()
            case 40:
                self.map_game.move_down()
                self.map_game.merge_down()
                self.map_game.move_down()
            case 37:
                self.map_game.move_left()
                self.map_game.merge_left()
                self.map_game.move_left()
            case 39:
                self.map_game.move_right()
                self.map_game.merge_right()
                self.map_game.move_right()

        self.random()
        self.draw()
