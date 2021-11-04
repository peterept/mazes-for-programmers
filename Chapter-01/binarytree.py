#!/usr/bin/env python3

import random

import gridy
import gridy_svg


def binarytree(grid: gridy.Grid):
    # for every cell, randomly carve out to the East or North (if possible)
    for cell in grid:
        dests = list(filter(None, [cell.n, cell.e]))
        if len(dests) > 0:
            dest = random.choice(dests)
            cell.link_cell(dest)

def main():
    grid = gridy.Grid(12, 8)

    binarytree(grid)

    print(grid)
    print(f"Maze {grid.width} x {grid.height}")

    svg = gridy_svg.GridSvg(grid)
    svg.save("test.svg")


if __name__ == "__main__":
    main()
