from __future__ import annotations;
from typing import Optional;
import os;

def main():
    input_name = 'data/input.txt'
    # input_name = 'data/input-test.txt'
    input_path = os.path.join(os.path.dirname(__file__), input_name)

    with open(input_path, 'r') as file:

        efs: list[ElvenDirectory] = list()
        efs.append(ElvenDirectory('/', None))

        current_dir = efs[0]

        # build structure
        for line in file:
            if line.startswith('$ cd /'):
                current_dir = efs[0]

            elif line.startswith('$ cd'):
                dir = line.split()[-1]
                if dir == '..':
                    current_dir = current_dir.parent
                elif dir in current_dir.children.keys():
                    current_dir = current_dir.children[dir]
                else:
                    raise RuntimeError(f"cd {dir}: {dir} is not a child of {current_dir.name} ({current_dir.children.keys()})")
            
            if not line.startswith('$'):
                [first_part, name] = line.split()
                if first_part == 'dir':
                    if name in current_dir.children.keys():
                        print(f"{name} is already in {current_dir.name}'s children: {current_dir.children.keys()}")
                        continue

                    new_dir = ElvenDirectory(name, current_dir)
                    efs.append(new_dir)
                    current_dir.children[name] = new_dir
                else:
                    if name in current_dir.files.keys(): continue
                    new_file = ElvenFile(name, current_dir, int(first_part))
                    current_dir.files[name] = new_file
        
        # calculate sizes
        result = 0
        for dir in efs:
            if dir.get_size() <= 100000: result += dir.get_size()
        
        print(result)
            

class ElvenDirectory:
    def __init__(self, name: str, parent: Optional[ElvenDirectory]):
        self.name = name
        self.parent = parent
        self.children: dict[str, ElvenDirectory] = dict()
        self.files: dict[str, ElvenFile] = dict()
        self.size: Optional[int] = None

    def get_size(self) -> int:
        if self.size is not None:
            return self.size
        
        size = sum(map(lambda x:x.size, self.files.values()))
        for c in self.children.values():
            size += c.get_size()
        
        self.size = size
        return size

class ElvenFile:
    def __init__(self, name: str, parent: ElvenDirectory, size: int):
        self.name = name
        self.parent = parent
        self.size = size

if __name__ == "__main__":
    main()
