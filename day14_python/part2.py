from __future__ import annotations
import os
from typing import Tuple
from enum import Enum

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:
        x_start = float('inf')
        x_end = float('-inf')
        y_start = float('inf')
        y_end = float('-inf')

        print(*range(3,1))

        grid: dict[Tuple[int, int], Element] = dict()
        for line in file:
            previous_x = None
            previous_y = None
            for coords in line.strip().split(' -> '):
                [x,y] = map(lambda s: int(s), coords.split(','))
                x_start = min(x_start, x)
                x_end = max(x_end, x)
                y_start = min(y_start, y)
                y_end = max(y_end, y)

                grid[(x,y)] = Element.ROCK
                if previous_x is not None and previous_y is not None:
                    if x == previous_x:
                        for n in range(min(y, previous_y), max(y, previous_y)):
                            grid[(x, n)] = Element.ROCK
                    elif y == previous_y:
                        for n in range(min(x, previous_x), max(x, previous_x)):
                            grid[(n, y)] = Element.ROCK

                previous_x = x
                previous_y = y

        for x in range(x_start, x_end + 1):
            grid[(x, y_end + 2)] = Element.ROCK

        for d in range(1, (x_end - x_start) * 3):
            grid[(x_start - d, y_end + 2)] = Element.ROCK
            grid[(x_end + d, y_end + 2)] = Element.ROCK

        print_grid(grid, x_start, x_end, y_start, y_end)

        current_sand_position: Tuple[int, int] = (500, 0)
        units_until_source_blocked = 1
        while True:
            down = (current_sand_position[0], current_sand_position[1] + 1)
            diag_left = (current_sand_position[0] - 1, current_sand_position[1] + 1)
            diag_right = (current_sand_position[0] + 1, current_sand_position[1] + 1)
            if down not in grid:
                current_sand_position = down
            elif diag_left not in grid:
                current_sand_position = diag_left
            elif diag_right not in grid:
                current_sand_position = diag_right
            else:
                grid[current_sand_position] = Element.SAND
                if current_sand_position == (500, 0):
                    break
                
                units_until_source_blocked += 1
                current_sand_position = (500, 0)
        print(units_until_source_blocked)


def print_grid(grid, x_start, x_end, y_start, y_end):
    for y in range(y_start, y_end + 3):
        row = ''
        for x in range(x_start - 15, x_end + 15):
            c = 0
            if (x,y) in grid:
                c = grid[(x,y)].value
            row = row + char[c]
        print(row)            

class Element(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2

char: dict[int, str] = {
    0: '.',
    1: '#',
    2: 'o',
}

if __name__ == "__main__":
    main()
