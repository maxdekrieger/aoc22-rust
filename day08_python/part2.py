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

        scenic_grid: list[list[int]] = list(map(lambda y: list(map(lambda x: 0, y)), grid))
        max_len = len(grid) - 1

        for y, row in enumerate(grid):
            for x, tree in enumerate(row):
                left = 0
                while can_see_left(grid, tree, x - left, y):
                    left += 1
                if x-left != 0:
                    left += 1
                
                right = 0
                while can_see_right(grid, tree, x + right, y):
                    right += 1
                if x+right != max_len:
                    right += 1

                up = 0
                while can_see_up(grid, tree, x, y - up):
                    up += 1
                if y-up != 0:
                    up += 1
                
                down = 0
                while can_see_down(grid, tree, x, y + down):
                    down += 1
                if y+down != max_len:
                    down += 1

                scenic_grid[y][x] = left * right * down * up
                # print(f"scenic score of [{x}][{y}]: {scenic_grid[y][x]}")
        
        best_scenic_score = max(map(lambda row: max(row), scenic_grid))
        print(best_scenic_score)
                

def can_see_left(grid, height, x, y):
    if x-1 < 0:
        return False
    else:
        return grid[y][x-1] < height

def can_see_right(grid, height, x, y):
    if x+1 >= len(grid):
        return False
    else:
        return grid[y][x+1] < height

def can_see_up(grid, height, x, y):
    if y-1 < 0:
        return False
    else:
        return grid[y-1][x] < height

def can_see_down(grid, height, x, y):
    if y+1 >= len(grid):
        return False
    else:
        return grid[y+1][x] < height

if __name__ == "__main__":
    main()
