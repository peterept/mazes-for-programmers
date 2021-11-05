#!/usr/bin/env python3

import random

import gridy
import gridy_svg


def sidewinder(grid: gridy.Grid):
    for row in grid.rows:
        print("row")
        run = []
        for cell in row:
            run.append(cell)
            if not cell.n and cell.e:
                # top
                cell.link_cell(cell.e)
            elif cell.e and random.random() >= 0.5:
                # east
                cell.link_cell(cell.e)
            else:
                # north
                dest = random.choice(run)
                dest.link_cell(dest.n)
                run = []

def main():
    grid = gridy.Grid(12, 8)

    sidewinder(grid)

    print(grid)
    print(f"Maze {grid.width} x {grid.height}")

    svg = gridy_svg.GridSvg(grid)
    svg.save("test.svg")


if __name__ == "__main__":
    main()
