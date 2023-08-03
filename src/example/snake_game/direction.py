from src.example.snake_game.point import Point

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
