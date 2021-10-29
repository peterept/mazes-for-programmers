#!/usr/bin/env python3

import gridy

# To install svgwrite:
# c:\> py -0p
# c:\> py -3.6-64 -m pip install svgwrite
import svgwrite


class GridSvg:
    def __init__(self, grid: gridy.Grid):
        self.grid = grid

    def save(self, filename: str):
        border = 0.5
        dwg = svgwrite.Drawing(
            filename,
            viewBox=(
                f"{-border} {-border} {self.grid.width + 1 + border} {self.grid.height + 1 + border}"
            ),
        )

        stroke_width = 0.1
        stroke_width_half = stroke_width / 2
        stroke_style = {"stroke": "black", "stroke_width": stroke_width}

        # draw every cell border
        for cell in self.grid:
            # assume borders
            x = cell.x
            y = cell.y
            if cell.has_wall(gridy.GridDir.NORTH):
                dwg.add(
                    dwg.line(
                        (x - stroke_width_half, y),
                        (x + 1 + stroke_width_half, y),
                        **stroke_style,
                    )
                )
            if cell.has_wall(gridy.GridDir.SOUTH):
                dwg.add(
                    dwg.line(
                        (x - stroke_width_half, y + 1),
                        (x + 1 + stroke_width_half, y + 1),
                        **stroke_style,
                    )
                )
            if cell.has_wall(gridy.GridDir.WEST):
                dwg.add(
                    dwg.line(
                        (x, y - stroke_width_half),
                        (x, y + 1 + stroke_width_half),
                        **stroke_style,
                    )
                )
            if cell.has_wall(gridy.GridDir.EAST):
                dwg.add(
                    dwg.line(
                        (x + 1, y + stroke_width_half),
                        (x + 1, y + 1 + stroke_width_half),
                        **stroke_style,
                    )
                )
        dwg.save()
