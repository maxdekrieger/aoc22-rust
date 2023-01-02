import os;

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:
        lines = file.readlines()

        current_instruction = None
        end_current_instruction_at = None

        sum_of_signal_strengths = 0
        measurement_points = [20, 60, 100, 140, 180, 220]

        register_x = 1
        for cycle in range(1, 221):
            # start of cycle
            if current_instruction == None and len(lines) > 0:
                current_instruction = lines.pop(0).strip()
                
                end_current_instruction_at = cycle if current_instruction == 'noop' else (cycle + 1)
            
            
            # print(f"Register X at cycle {cycle}: {register_x}. Current instruction: {current_instruction}, ends {'this cycle' if end_current_instruction_at == cycle else 'next cycle'}")

            # during cycle
            if cycle in measurement_points:
                
                sum_of_signal_strengths += cycle * register_x

            # end of cycle
            if end_current_instruction_at == cycle:
                if current_instruction.startswith('addx'):
                    register_x += int(current_instruction.split()[-1])
                
                current_instruction = None
                end_current_instruction_at = None

        print(sum_of_signal_strengths)

if __name__ == "__main__":
    main()
