import unittest

from ygame.example.game_2048.map import Map


class TestMap(unittest.TestCase):
    def test_move_left(self):
        map_game = Map(4, 4)
        map_game.value = [2, None, None, 2,  4, None, None, 2,  None, None, None, None,  2, 2, 2, 2]
        map_game.move_left()
        map_game.merge_left()
        map_game.move_left()

        print(map_game.value)

        self.assertEqual(map_game.value, [
            4,      None,   None,   None,
            4,      2,      None,   None,
            None,   None,   None,   None,
            4,      4,      None,   None
        ])

    def test_move_right(self):
        map_game = Map(4, 4)
        map_game.value = [2, None, None, 2,  4, None, None, 2,  None, None, None, None,  2, 2, 2, 2]
        map_game.move_right()
        map_game.merge_right()
        map_game.move_right()

        print(map_game.value)

        self.assertEqual(map_game.value, [
            None,   None,   None,   4,
            None,   None,   4,      2,
            None,   None,   None,   None,
            None,   None,   4,      4,
        ])

    def test_move_up(self):
        map_game = Map(4, 4)
        map_game.value = [
            2,      None,   None,   2,
            4,      None,   None,   2,
            None,   None,   None,   None,
            2,      2,      2,      2
        ]
        map_game.move_up()
        map_game.merge_up()
        map_game.move_up()

        print(map_game.value)

        self.assertEqual(map_game.value, [
            2,      2,      2,      4,
            4,      None,   None,   2,
            2,      None,   None,   None,
            None,   None,   None,   None,
        ])
