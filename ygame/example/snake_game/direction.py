# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

from ygame.example.snake_game.point import Point

UP = Point(x=0, y=-1)
DOWN = Point(x=0, y=1)
LEFT = Point(x=-1, y=0)
RIGHT = Point(x=1, y=0)

direction = {
    38: UP,
    40: DOWN,
    37: LEFT,
    39: RIGHT
}
