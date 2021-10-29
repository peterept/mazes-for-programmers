#!/usr/bin/env python3

import random

import gridy
import gridy_svg


def main():
    grid = gridy.Grid(12, 8)

    # for every cell, randomly carve out to the East or North (if possible)
    for cell in grid:
        if random.randrange(0, 2):
            cell.carve(gridy.GridDir.EAST) or cell.carve(gridy.GridDir.NORTH)
        else:
            cell.carve(gridy.GridDir.NORTH) or cell.carve(gridy.GridDir.EAST)

    print(grid)
    print(f"Maze {grid.width} x {grid.height}")

    svg = gridy_svg.GridSvg(grid)
    svg.save("test.svg")


if __name__ == "__main__":
    main()
