import os;
from math import floor

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:
        lines = file.readlines()

        current_instruction = None
        end_current_instruction_at = None

        crt = list(map(lambda _: list(map(lambda _: False, range(40))), range(6)))

        register_x = 1
        for cycle in range(1, 241):
            # start of cycle
            if current_instruction == None and len(lines) > 0:
                current_instruction = lines.pop(0).strip()
                end_current_instruction_at = cycle if current_instruction == 'noop' else (cycle + 1)
            
            idx = cycle - 1
            crt[floor(idx / 40)][idx % 40] = idx % 40 in [register_x - 1, register_x, register_x + 1]

            # end of cycle
            if end_current_instruction_at == cycle:
                if current_instruction.startswith('addx'):
                    register_x += int(current_instruction.split()[-1])
                
                current_instruction = None
                end_current_instruction_at = None

        for row in crt:
            pixels = map(lambda b: '#' if b else '.', row)
            print(''.join(pixels))

if __name__ == "__main__":
    main()
