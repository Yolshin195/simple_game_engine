# This file is part of ygame.
#
# ygame is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by the Massachusetts
# Institute of Technology. See the LICENSE.txt file for more details.

class User:
    def __init__(self, label: str):
        self.label = label


USER_X = User("X")
USER_O = User("O")
