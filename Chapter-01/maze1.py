#!/usr/bin/env python3

import random
from enum import Enum


class GridDir(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


class GridCell:
    def __init__(self, grid: "Grid", x: int, y: int):
        self.grid = grid
        self.x = x
        self.y = y
        self.xy = (x, y)

    def carve(self, dir: GridDir):
        """Carve (remove) the wall in the direction for this cell. returns true if valid"""
        return self.grid.carve(self, dir)


class Grid:
    OUTER_WALLS = ["###", "# #", "###"]
    INNER_WALLS = ["+-+", "| |", "+-+"]

    def __init__(self, width: int, height: int):
        """Create a grid of specified width and height"""
        self.width = width
        self.height = height
        self.g = [
            [self.OUTER_WALLS[0][0] for x in range(0, width * 2 + 1)]
            for y in range(0, height * 2 + 1)
        ]
        for cell in self:
            self.init_cell(cell)

    def __repr__(self) -> str:
        """Output grid as a string"""
        s = ""
        for y in self.g:
            for x in y:
                s += x
            s += "\n"
        return s

    def __iter__(self):
        return GridIterator(self)

    def intern_xy(self, xy: int) -> int:
        """Translate a grid co-ordinate to an internal co-ordinate"""
        return xy * 2 + 1

    def intern_is_border(self, x: int, y: int) -> bool:
        """True if the internal co-ordinate is in the grids border (outside grid bounds)"""
        return x == 0 or x == (self.width * 2) or y == 0 or y == (self.height * 2)

    def init_cell(self, cell: GridCell):
        dirs = [
            [-1, -1], [0, -1], [1, -1],
            [-1, 0],  [0, 0],  [1, 0],
            [-1, 1],  [0, 1],  [1, 1],
        ]
        for dir in dirs:
            gx = self.intern_xy(cell.x) + dir[0]
            gy = self.intern_xy(cell.y) + dir[1]
            walls = self.INNER_WALLS
            if self.intern_is_border(gx, gy):
                walls = self.OUTER_WALLS
            self.g[gy][gx] = walls[dir[1] + 1][dir[0] + 1]

    def cell(self, x: int, y: int) -> GridCell:
        """Returns a GridCell given it's grid co-ordinate"""
        return GridCell(self, x, y)

    def carve(self, cell: GridCell, dir: GridDir):
        """Carve (remove) the wall in the direction for this cell. returns true if valid"""
        dirs = {
            GridDir.NORTH: [0, -1],
            GridDir.SOUTH: [0, 1],
            GridDir.EAST: [1, 0],
            GridDir.WEST: [-1, 0],
        }
        gx = self.intern_xy(cell.x) + dirs[dir][0]
        gy = self.intern_xy(cell.y) + dirs[dir][1]
        if self.intern_is_border(gx, gy):
            return False
        self.g[gy][gx] = " "

        # tidy up the wall segments around the one we just removed
        if dir == GridDir.NORTH or dir == GridDir.SOUTH:
            for dx in [-1, 1]:
                wx = gx + dx
                if self.g[gy][wx] == self.INNER_WALLS[0][0]:
                    # + no longer makes sense if we don't have an opposite wall, make it |
                    if self.g[gy][wx + dx] == " ":
                        self.g[gy][wx] = self.INNER_WALLS[1][0]
        else:
            for dy in [-1, 1]:
                wy = gy + dy
                if self.g[wy][gx] == self.INNER_WALLS[0][0]:
                    # + no longer makes sense if we don't have an opposite wall, make it -
                    if self.g[wy + dy][gx] == " ":
                        self.g[wy][gx] = self.INNER_WALLS[0][1]
        return True


class GridIterator:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.x = self.y = 0

    def __next__(self) -> GridCell:
        if self.y == self.grid.height:
            raise StopIteration
        result = self.grid.cell(self.x, self.y)
        self.x += 1
        if self.x == self.grid.width:
            self.x = 0
            self.y += 1
        return result


def main():
    grid = Grid(12, 8)

    # for every cell, randomly carve out to the East or North (if possible)
    for cell in grid:
        if random.randrange(0, 2):
            cell.carve(GridDir.EAST) or cell.carve(GridDir.NORTH)
        else:
            cell.carve(GridDir.NORTH) or cell.carve(GridDir.EAST)

    print(grid)
    print(f"Maze {grid.width} x {grid.height}")


if __name__ == "__main__":
    main()
