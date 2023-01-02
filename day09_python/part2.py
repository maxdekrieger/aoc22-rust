import os;

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test-part2.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:

        tail_visited: set[tuple[int, int]] = {(0,0)}

        knots_x = [0 for _ in range(10)]
        knots_y = [0 for _ in range(10)]

        for line in file:
            [direction, amount] = line.split()
            for _ in range(int(amount)):
                if direction == 'L':
                    knots_x[0] -= 1
                elif direction == 'R':
                    knots_x[0] += 1
                elif direction == 'U':
                    knots_y[0] -= 1
                elif direction == 'D':
                    knots_y[0] += 1

                for k in range(9):
                    if head_and_tail_touching(knots_x[k], knots_y[k], knots_x[k+1], knots_y[k+1]): continue

                    
                    # not touching so tail needs to move
                    # first figure out if it needs to move diagonal
                    if needs_diagonal_move(knots_x[k], knots_y[k], knots_x[k+1], knots_y[k+1]):
                        # print(f"  needs diagonal move")
                        if knots_x[k] - knots_x[k+1] == 1: knots_x[k+1] += 1
                        elif knots_x[k] - knots_x[k+1] == -1: knots_x[k+1] -= 1
                        elif knots_y[k] - knots_y[k+1] == 1: knots_y[k+1] += 1
                        elif knots_y[k] - knots_y[k+1] == -1: knots_y[k+1] -= 1
                        elif (knots_x[k] - knots_x[k+1] == -2) and (knots_y[k] - knots_y[k+1] == -2):
                            knots_x[k+1] -= 1
                            knots_y[k+1] -= 1
                        elif (knots_x[k] - knots_x[k+1] == -2) and (knots_y[k] - knots_y[k+1] == 2):
                            knots_x[k+1] -= 1
                            knots_y[k+1] += 1
                        elif (knots_x[k] - knots_x[k+1] == 2) and (knots_y[k] - knots_y[k+1] == 2):
                            knots_x[k+1] += 1
                            knots_y[k+1] += 1
                        elif (knots_x[k] - knots_x[k+1] == 2) and (knots_y[k] - knots_y[k+1] == -2):
                            knots_x[k+1] += 1
                            knots_y[k+1] -= 1
                        else:
                            print("this shouldnt happen")

                    # then move straight up or down
                    if knots_y[k] == knots_y[k+1] and knots_x[k] < knots_x[k+1]: knots_x[k+1] -= 1 # move tail left
                    if knots_y[k] == knots_y[k+1] and knots_x[k] > knots_x[k+1]: knots_x[k+1] += 1 # move tail right
                    if knots_x[k] == knots_x[k+1] and knots_y[k] > knots_y[k+1]: knots_y[k+1] += 1 # move tail down
                    if knots_x[k] == knots_x[k+1] and knots_y[k] < knots_y[k+1]: knots_y[k+1] -= 1 # move tail down

                tail_visited.add((knots_x[9], knots_y[9]))
        
        print(len(tail_visited))
                


def head_and_tail_touching(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) < 2 and abs(head_y - tail_y) < 2

def needs_diagonal_move(head_x, head_y, tail_x, tail_y):
    return abs(head_x - tail_x) > 0 and abs(head_y - tail_y) > 0
    

if __name__ == "__main__":
    main()
