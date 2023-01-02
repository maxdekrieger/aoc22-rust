import os;

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:

        tail_visited: set[tuple[int, int]] = {(0,0)}

        head_x = 0
        head_y = 0
        tail_x = 0
        tail_y = 0

        for line in file:
            [direction, amount] = line.split()
            for _ in range(int(amount)):
                if direction == 'L':
                    head_x -= 1
                elif direction == 'R':
                    head_x += 1
                elif direction == 'U':
                    head_y -= 1
                elif direction == 'D':
                    head_y += 1
            
                if head_and_tail_touching(head_x, head_y, tail_x, tail_y): continue

                # not touching so tail needs to move
                # first figure out if it needs to move diagonal
                if needs_diagonal_move(head_x, head_y, tail_x, tail_y):
                    # print(f"  needs diagonal move")
                    if head_x - tail_x == 1: tail_x += 1
                    elif head_x - tail_x == -1: tail_x -= 1
                    elif head_y - tail_y == 1: tail_y += 1
                    elif head_y - tail_y == -1: tail_y -= 1

                # then move straight up or down
                if head_y == tail_y and head_x < tail_x: tail_x -= 1 # move tail left
                if head_y == tail_y and head_x > tail_x: tail_x += 1 # move tail right
                if head_x == tail_x and head_y > tail_y: tail_y += 1 # move tail down
                if head_x == tail_x and head_y < tail_y: tail_y -= 1 # move tail down

                tail_visited.add((tail_x, tail_y))
        
        print(len(tail_visited))
                


def head_and_tail_touching(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) < 2 and abs(head_y - tail_y) < 2

def needs_diagonal_move(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) > 0 and abs(head_y - tail_y) > 0
    

if __name__ == "__main__":
    main()
