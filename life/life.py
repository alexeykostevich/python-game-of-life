from typing import Iterable
from life.cell import Cell
from life.world import World


class Life(object):
    """Represents 'The Game of Life'."""

    @classmethod
    def originate_from(cls, world: World[Cell]) -> World[Cell]:
        """Returns a new iterator that can iterate over world states."""

        while True:
            next_world = world.empty()

            for x, y in world.through():
                cell = world[x, y]
                neibours = world.neighbours_of(x, y)

                next_world[x, y] = Life.next_cell(cell, neibours)

            world = next_world

            yield next_world

    @staticmethod
    def next_cell(cell: Cell, neigbours: Iterable[Cell]) -> Cell:
        """Returns the survivied cell, a regenerated cell or nothing for a new world."""
        neigbours_alive = sum(neigbour is not None for neigbour in neigbours)

        if cell and (neigbours_alive < 2 or 3 < neigbours_alive):
            return None

        if cell is None and neigbours_alive == 3:
            return Cell()

        return cell
