from typing import Callable
import os
from math import lcm

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    monkeys: list[Monkey] = list()
    test_numbers: list[int] = list()

    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('Monkey'):
                monkeys.append(Monkey(line))
            elif line.startswith('Starting items'):
                monkeys[-1].set_items(line)
            elif line.startswith('Operation'):
                monkeys[-1].set_operation(line)
            elif line.startswith('Test'):
                test_numbers.append(int(line.split()[-1]))
                monkeys[-1].set_test(line)
            elif line.startswith('If'):
                monkeys[-1].add_next_step(line)

    test_lcm = lcm(*test_numbers)

    print_rounds = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    for round in range(10000):
        for m in monkeys:
            while len(m.items) > 0:
                item = m.items.pop(0)
                item_after_op = m.operation(item)
                item_after_lcm = item_after_op % test_lcm
                next = m.next[m.test( item_after_lcm )]
                # print(f"Monkey {m.number} throws item {item}: {item_after_op} / 3 = {item_bored} to monkey {next}")
                monkeys[next].items.append( item_after_lcm )

            if (round + 1) in print_rounds:
                print(f"After round {round + 1}:")
                for m in monkeys:
                    print(f"  Monkey {m.number}: {m.inspects} inspects")

        # print(f'After round {round + 1}:')
        # for m in monkeys:
        #     m.print()

    monkeys.sort(reverse=True)
    print(monkeys[0].inspects * monkeys[1].inspects)

class Monkey:
    def __init__(self, number_str: str) -> None:
        self.number                          = int(number_str[-2])
        self.items: list[int]                = list()
        self.operation: Callable[[int], int] = None
        self.test: Callable[[int], bool]     = None
        self.next: dict[bool, int]           = dict()
        self.inspects: int                   = 0

    def __lt__(self, other):
        return self.inspects < other.inspects

    def set_items(self, items_str: str) -> None:
        self.items = list(map(lambda s : int(s), items_str.split(': ')[1].split(', ')))

    def set_operation(self, operation_str: str) -> None:
        last_char = operation_str.split()[-1]
        is_digit = last_char.isdigit()
        number = int(last_char) if is_digit else -1
        def operation_add(old: int) -> int:
            self.inspects += 1
            return old + number
        def operation_mult(old: int) -> int:
            self.inspects += 1
            return old * number
        def operation_double(old: int) -> int:
            self.inspects += 1
            return old + old
        def operation_square(old: int) -> int:
            self.inspects += 1
            return old * old
        
        if "+" in operation_str and is_digit:
            self.operation = operation_add
        elif "*" in operation_str and is_digit:
            self.operation = operation_mult
        elif "+" in operation_str:
            self.operation = operation_double
        elif "*" in operation_str:
            self.operation = operation_square
        else:
            raise RuntimeError(f"Error in operation: {operation_str}")

    def set_test(self, test_str: str) -> None:
        number = int(test_str.split()[-1])
        def test(x: int) -> bool:
            return x % number == 0
        self.test = test

    def add_next_step(self, next_str: str) -> None:
        next_monkey = int(next_str[-1])
        if "true" in next_str:
            self.next[True] = next_monkey
        elif "false" in next_str:
            self.next[False] = next_monkey
        else:
            raise RuntimeError(f"Error in next step: {next_str}")

    def print(self, verbose: bool = False) -> None:
        print(f'  Monkey {self.number}: {self.items}')
        if verbose:
            print(f'    Operation: {self.operation}')
            print(f'    Test: {self.test}')
            print(f'    Next Step: {self.next}')

if __name__ == "__main__":
    main()
