import os;

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:
        
        # build structure
        grid: list[list[int]] = list()
        for line in file:
            horizontal = list(map(lambda x: int(x), [*line.strip()]))
            grid.append(horizontal)
        
        visibility_grid: list[list[bool]] = list(map(lambda y: list(map(lambda x: False, y)), grid))

        # from left to right and top to bottom
        tallest_in_column = list(map(lambda x: -1, grid))
        for y, row in enumerate(grid):
            tallest_in_row = -1
            for x, height in enumerate(row):
                if height > tallest_in_row:
                    visibility_grid[y][x] = True
                    tallest_in_row = height
                if height > tallest_in_column[x]:
                    visibility_grid[y][x] = True
                    tallest_in_column[x] = height

        for row in grid:
            row.reverse()
        grid.reverse()

        for row in visibility_grid:
            row.reverse()
        visibility_grid.reverse()

        # from right to left and bottom to top
        tallest_in_column = list(map(lambda x: -1, grid))
        for y, row in enumerate(grid):
            tallest_in_row = -1
            for x, height in enumerate(row):
                if height > tallest_in_row:
                    visibility_grid[y][x] = True
                    tallest_in_row = height
                if height > tallest_in_column[x]:
                    visibility_grid[y][x] = True
                    tallest_in_column[x] = height
        
        for row in grid:
            row.reverse()
        grid.reverse()

        for row in visibility_grid:
            row.reverse()
        visibility_grid.reverse()

        total_visible = sum(map(lambda y: sum(map(lambda b: 1 if b else 0, y)), visibility_grid))
        print(total_visible)

if __name__ == "__main__":
    main()
