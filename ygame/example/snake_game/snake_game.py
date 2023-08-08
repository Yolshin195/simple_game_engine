# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.core.color import WHITE
from ygame.core.game import Game
from ygame.example.snake_game.apple import Apple
from ygame.example.snake_game.direction import direction
from ygame.example.snake_game.point import Point
from ygame.example.snake_game.snake import Snake


class SnakeGame(Game):
    width: int = 9
    height: int = 9
    apple: Apple = None
    snake: Snake = None
    is_pause: bool = False
    is_game: bool = False

    def initialize(self):
        self.set_title("Snake Game!")
        self.set_screen_size(9, 9, 50)

        self.start()

    def start(self):
        self.stop_turn_timer()
        self.clear_map()
        self.snake = Snake()
        self.spawn_apple()

        self.snake.draw(self.draw_point)

        self.is_game = True
        self.set_turn_timer(300)

    def loop(self):
        self.snake.move()

        if self.snake == self.snake:
            self.is_game = False
            self.show_message("Game over!")

        if self.snake == self.apple:
            self.snake.feed()
            self.spawn_apple()

        self.snake.draw(self.draw_point, self.remove_point)

    def draw_point(self, point: Point):
        self.set_cell(point.x, point.y, text=point.label, text_color=point.color)

    def remove_point(self, point: Point):
        self.set_cell(point.x, point.y, text="")

    def spawn_apple(self):
        if self.apple is not None:
            self.apple.draw(self.remove_point)

        x = self.get_random_number(0, 8)
        y = self.get_random_number(0, 8)

        apple = Apple(x, y)
        if self.snake == apple:
            self.spawn_apple()
        else:
            self.apple = apple.draw(self.draw_point)

    def clear_map(self):
        for x in range(self.width):
            for y in range(self.height):
                self.set_cell(x, y, color=WHITE, text="")

    def on_key_press(self, char: str, keycode: int):
        if keycode == 82:
            self.is_game = False
            self.start()
            return

        if keycode == 32:
            self.is_pause = True
            self.snake.set_direction(None)
            self.show_message("Pause!")
            return

        if self.is_game:
            self.is_pause = False
            self.snake.set_direction(direction[keycode])
            return

        self.show_message("Press 'R' for restart")

    def on_turn(self, step: int):
        if self.is_pause:
            return

        if not self.is_game:
            self.stop_turn_timer()
            return

        self.loop()
