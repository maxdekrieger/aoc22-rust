from __future__ import annotations
import os
from typing import Tuple

def main():
    # input_name = 'data/input.txt'
    input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:
        left: Packet = None
        right: Packet = None
        sum = 0

        index = 1
        for line in file:
            if left is None:
                left = create_packet(line.strip())[0]
            elif right is None:
                right = create_packet(line.strip())[0]
            else: 
                # Calculate if its correct
                # at the end
                left = None
                right = None
                index += 1

def create_packet(text: str) -> Tuple[Packet, str]:
    packet = Packet()

    if text[0] == '[':
        text = text[1:]
    elif text[0].isdigit() and text[1].isdigit():
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
            print(text)

    return (packet, text)

class Packet:
    def __init__(self) -> None:
        self.literal: int = None
        self.subpackets: list[Packet] = list()
        pass

if __name__ == "__main__":
    main()
