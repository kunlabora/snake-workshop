from unittest import TestCase

from snake_game import SnakeGame


class TestSnakeGame(TestCase):
    def test_given_game_with_initial_snake_position_snake_is_at_position(self):
        game = SnakeGame([(1, 1), (1, 2), (1, 3)], (5, 5), 25)

        self.assertEqual(game.get_snake_positions(), [(1, 1), (1, 2), (1, 3)])

    def test_given_game_with_snake_position_snake_is_at_position(self):
        game = SnakeGame([(1, 1), (1, 2), (1, 3)], (5, 5), 25)

        self.assertEqual(game.get_food_position(), (5,5))

    def test_snake_facing_north_moves_up_one_block(self):
        game = SnakeGame([(1, 1), (1, 2), (1, 3)], (5, 5), 25)

        game.tick()

        self.assertEqual(game.get_snake_positions(), [(1, 2), (1, 1), (1, 2)])
