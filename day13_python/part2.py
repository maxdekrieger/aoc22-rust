from __future__ import annotations
import os
from typing import Tuple

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:

        packets: list[Packet] = list()
        divider_2 = create_packet('[[2]]')[0]
        divider_6 = create_packet('[[6]]')[0]
        packets.append(divider_2)
        packets.append(divider_6)

        for line in file:
            line = line.strip()
            if line:
                p = create_packet(line.strip())[0]
                packets.append(p)

        packets.sort()
        for p in packets:
            print(p.to_string())
        
        print((packets.index(divider_2) + 1) * (packets.index(divider_6) + 1))

def create_packet(text: str) -> Tuple[Packet, str]:
    packet = Packet()

    if text[0] == '[':
        text = text[1:]
    elif len(text) >= 2 and text[0].isdigit() and text[1].isdigit():
        packet.literal = int(text[:2])
        return (packet, text[2:])
    elif text[0].isdigit():
        packet.literal = int(text[0])
        return (packet, text[1:])

    while text:
        if text[0] == ']':
            return (packet, text[1:])
        elif text[0] == ',':
            text = text[1:]
        else:
            (subpacket, text) = create_packet(text)
            packet.subpackets.append(subpacket)
            # print(text)

    return (packet, text)

class Packet:
    def __init__(self) -> None:
        self.literal: int = None
        self.subpackets: list[Packet] = list()
        pass

    def __lt__(self, other) -> bool:
        result = self.compare(other)
        if result == 1:
            return True
        elif result == -1:
            return False
        else:
            raise RuntimeError(f"Comparing {self.to_string()} to {other.to_string()} gave 0")

    def is_literal(self) -> bool:
        return self.literal is not None

    def to_string(self) -> str:
        if self.is_literal():
            return str(self.literal)
        else:
            subpackets_str = list(map(lambda s : s.to_string(), self.subpackets))
            return f"[{','.join(subpackets_str)}]"

    def compare(self, other : Packet) -> int:
        # print(f"comparing {self.to_string()} to {other.to_string()}")
        if self.is_literal() and other.is_literal():
            if self.literal == other.literal:
                return 0
            elif self.literal < other.literal:
                return 1
            elif self.literal > other.literal:
                # print(f"Not in the right order: {self.literal} > {other.literal}")
                return -1
        elif self.is_literal():
            self.subpackets.append(create_packet(f'{self.literal}')[0])
            self.literal = None
        elif other.is_literal():
            other.subpackets.append(create_packet(f'{other.literal}')[0])
            other.literal = None

        for idx in range(len(self.subpackets)):
            if idx > (len(other.subpackets) - 1):
                # print(f"Not in the right order: left has more subpackets than right")
                return -1

            selfsub = self.subpackets[idx]
            othersub = other.subpackets[idx]

            subresult = selfsub.compare(othersub)
            if subresult != 0:
                return subresult

        if len(self.subpackets) < len(other.subpackets):
            return 1
        else:
            return 0

if __name__ == "__main__":
    main()
