import unittest
from typing import List
from life import BoundedWorld, Life


def neibours(count: int) -> List[bool]:
    return [True] * count + [None] * (8 - count)


class BoundedWorldTestCase(unittest.TestCase):
    def test_next_cell_remains_dead(self):
        for alive in range(3):
            next_cell = Life.next_cell(None, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

        for neiboirs_exist in range(4, 8):
            next_cell = Life.next_cell(None, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

    def test_next_cell_remains_alive(self):
        for alive in range(2, 3):
            next_cell = Life.next_cell(True, neibours(alive), lambda: True)
            self.assertTrue(next_cell)

    def test_next_cell_dies(self):
        for alive in range(2):
            next_cell = Life.next_cell(True, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

        for alive in range(4, 9):
            next_cell = Life.next_cell(True, neibours(alive), lambda: True)
            self.assertIsNone(next_cell)

    def test_next_cell_regenerates(self):
        next_cell = Life.next_cell(None, neibours(3), lambda: True)
        self.assertTrue(next_cell)

    def test_originate_from_loaf(self):
        original_world = BoundedWorld.from_data(
            [None, True, True, None],
            [True, None, None, True],
            [None, True, None, True],
            [None, None, True, None]
        )

        generation = Life.originate_from(original_world, lambda: True)
        actual_world = next(generation)

        self.assertEqual(actual_world, original_world)

    def test_originate_from_block(self):
        original_world = BoundedWorld.from_data(
            [None, None, None, None],
            [None, True, True, None],
            [None, True, True, None],
            [None, None, None, None]
        )

        generation = Life.originate_from(original_world, lambda: True)
        actual_world = next(generation)

        self.assertEqual(actual_world, original_world)

    def test_originate_from_blinker(self):
        original_world = BoundedWorld.from_data(
            [None, True, None],
            [None, True, None],
            [None, True, None]
        )

        expected_world = BoundedWorld.from_data(
            [None, None, None],
            [True, True, True],
            [None, None, None]
        )

        generation = Life.originate_from(original_world, lambda: True)
        actual_world = next(generation)

        self.assertEqual(actual_world, expected_world)

    def test_originate_from_toad(self):
        original_world = BoundedWorld.from_data(
            [None, None, None, None],
            [None, True, True, True],
            [True, True, True, None],
            [None, None, None, None]
        )

        expected_world = BoundedWorld.from_data(
            [None, None, True, None],
            [True, None, None, True],
            [True, None, None, True],
            [None, True, None, None]
        )

        generation = Life.originate_from(original_world, lambda: True)
        actual_world = next(generation)

        self.assertEqual(actual_world, expected_world)


if __name__ == '__main__':
    unittest.main()