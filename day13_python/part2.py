from __future__ import annotations
import os
import string

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    grid: list[list[Square]] = list()
    start: Square = None
    end: Square = None

    with open(input_path, 'r') as file:
        for y, line in enumerate(file):
            row: list[Square] = list()
            for x, c in enumerate(line.strip()):
                s = Square(x, y, c)
                if c == 'S':
                    start = s
                elif c == 'E':
                    end = s
                row.append(s)
            grid.append(row)

    for row in grid:
        for s in row:
            s.find_and_add_adjacent(grid)

    # flatten grid into set
    unvisited = set([item for sublist in grid for item in sublist])
    start.distance = 0
    while len(unvisited) > 0:
        u = min(unvisited, key=lambda x: x.distance)
        unvisited.remove(u)
        for v in u.adjacent.intersection(unvisited):
            alt = u.distance + 1
            if alt < v.distance:
                v.distance = alt
                v.previous = u

    print(end.distance)

class Square:
    def __init__(self, x: int, y: int, elevation: str) -> None:
        self.x = x
        self.y = y
        elevation = 'a' if elevation == 'S' else elevation
        elevation = 'z' if elevation == 'E' else elevation
        self.elevation: int = string.ascii_lowercase.index(elevation)
        self.adjacent: set[Square] = set()

        self.distance: int = 0 if elevation == 'a' else float('inf')
        self.previous: Square = None

    def find_and_add_adjacent(self, grid: list[list[Square]]):
        #left
        if self.x > 0:
            left = grid[self.y][self.x - 1]
            if left.elevation <= (self.elevation + 1):
                self.adjacent.add(left)
        #right
        if self.x < (len(grid[0]) - 1):
            right = grid[self.y][self.x + 1]
            if right.elevation <= (self.elevation + 1):
                self.adjacent.add(right)
        #up
        if self.y > 0:
            up = grid[self.y - 1][self.x]
            if up.elevation <= (self.elevation + 1):
                self.adjacent.add(up)
        #down
        if self.y < (len(grid) - 1):
            down = grid[self.y + 1][self.x]
            if down.elevation <= (self.elevation + 1):
                self.adjacent.add(down)

if __name__ == "__main__":
    main()
