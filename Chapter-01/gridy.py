#!/usr/bin/env python3

class GridCell:
    def __init__(self, grid: "Grid", x: int, y: int):
        self.grid = grid
        self.x = x
        self.y = y
        self.links = []

    @property
    def n(self):
        return self.grid[self.x, self.y - 1]

    @property
    def s(self):
        return self.grid[self.x, self.y + 1]

    @property
    def e(self):
        return self.grid[self.x + 1, self.y]

    @property
    def w(self):
        return self.grid[self.x - 1, self.y]

    def is_linked(self, cell: "GridCell") -> bool:
        if cell:
            return cell in self.links
        return False

    def carve_e(self):
        cell = self.grid[self.x + 1, self.y]
        if cell != None:
            self.link_cell(cell)

    def carve_n(self):
        cell = self.grid[self.x, self.y + 1]
        if cell != None:
            self.link_cell(cell)

    def link_cell(self, cell: "GridCell"):
        if cell != None:
            if not cell in self.links:
                print(f"link_cell: {self.x},{self.y} to {cell.x},{cell.y}")
                self.links.append(cell)
                print(self.links)
            if not self in cell.links:
                cell.links.append(self)        


class Grid:
    def __init__(self, width: int, height: int):
        """Create a grid of specified width and height"""
        self.width = width
        self.height = height
        self.cells = [[None for x in range(0, width)] for y in range(0, height)]
        for y in range(height):
            for x in range(width):
                self.cells[y][x] = GridCell(self, x, y) 


    def __getitem__(self, xy) -> GridCell:
        """Get the cell at grid[x,y]"""
        x, y = xy
        if x in range(self.width) and y in range(self.height):
            return self.cells[y][x]
        return None

    def __repr__(self) -> str:
        """Output grid as a string"""
        rows = []
        for row in self.cells:
            s1 = ""
            s2 = ""
            for cell in row:
                s1 += " "
                s1 += " " if cell.is_linked(cell.e) else "|"
                s2 += " " if cell.is_linked(cell.s) else "-"
                s2 += "+"
            rows.append(s1[:-1])
            rows.append(s2[:-1])
        hdr = "#" * (self.width * 2 + 1) + "\n" 
        return hdr + "#" + "#\n#".join(rows[:-1]) + "#\n" + hdr

    def __iter__(self):
        return GridIterator(self)

    @property
    def rows(self):
        return self.cells


class GridIterator:
    def __init__(self, grid: Grid):
        self.itery = iter(grid.cells)
        self.iterx = None

    def __next__(self) -> GridCell:
        if self.iterx == None:
            self.iterx = iter(next(self.itery))
        try:
            cell = next(self.iterx)
        except StopIteration:
            self.iterx = iter(next(self.itery))
            cell = next(self.iterx)
        return cell
