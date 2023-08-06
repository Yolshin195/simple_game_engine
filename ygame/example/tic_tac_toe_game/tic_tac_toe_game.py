from ygame.core.color import GREEN, WHITE
from ygame.core.game import Game
from ygame.example.tic_tac_toe_game.map import Map
from ygame.example.tic_tac_toe_game.user import USER_X, USER_O, User
import random
import time


class TicTacToeGame(Game):
    users = USER_X, USER_O
    player_turn = None
    is_game = False
    is_loop = False
    step = 0
    width = 3
    height = 3
    map: Map

    def initialize(self):
        self.set_title("Tic Tac Toe!")
        self.set_screen_size(self.width, self.height)

        random.seed(time.time())

        self.start()

    def start(self):
        self.is_game = True
        self.step = 0

        self.clear_map()
        self.map = Map(self.width, self.height)
        self.select_first_player()

    def loop(self):
        winning_combination = self.map.find_winning_combination()
        if len(winning_combination):
            self.is_game = False
            self.show_winning_combination(winning_combination)
            self.show_message(f'Winner: {self.get_current_player().label}')
            return

        self.set_next_player()
        self.step += 1

        if self.step > 8:
            self.is_game = False
            self.show_draw()
            self.show_message("It was a draw!")

    def select_first_player(self):
        self.player_turn = random.randint(0, 1)
        self.show_message(f'First: {self.get_current_player().label}')

    def set_next_player(self):
        self.player_turn = (self.player_turn + 1) % len(self.users)

    def get_current_player(self) -> User:
        return self.users[self.player_turn]

    def on_left_click(self, x: int, y: int):
        if self.is_game:
            self.is_loop = True
            if self.map.set(x, y, self.get_current_player().label):
                self.set_cell(x, y, text=self.get_current_player().label)
                self.loop()
            else:
                self.show_message("Choose another cell")
            self.is_loop = False
        else:
            self.show_message("Press 'R' for restart")

    def on_key_press(self, char: str, keycode: int):
        if char == 'r' or char == 'R':
            self.start()

    def clear_map(self):
        for x in range(self.width):
            for y in range(self.height):
                self.set_cell(x, y, color=WHITE, text="")

    def show_draw(self):
        label = "X", "=", "O"
        for x in range(self.width):
            for y in range(self.height):
                self.set_cell(x, y, color=GREEN, text=label[x])

    def show_winning_combination(self, winning_combination: list[list]):
        winner = self.get_current_player().label
        for x, y, _ in winning_combination:
            self.set_cell(x, y, color=GREEN, text=winner)
