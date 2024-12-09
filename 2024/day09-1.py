import os
from itertools import combinations


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

        input = [int(value) for value in input]
    return input


def populate_memory(input):
    memory = dict()

    id = 0
    pos = 0
    for i, value in enumerate(input):
        if i % 2 == 0:
            for k in range(pos, pos + value):
                memory[k] = id
            id += 1
        pos += value
    return memory


def defrag(memory):
    keys = list(memory.keys())
    keys.sort(reverse=True)
    i = 0
    while i <= keys[0]:
        if i not in memory:
            memory[i] = memory[keys[0]]
            del memory[keys[0]]
            keys.pop(0)
        i += 1

    return memory


def checksum(memory):
    return sum([k * v for k, v in memory.items()])


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input09-1")
    input = read_input_file(file_path)

    memory = populate_memory(input)

    new_memory = defrag(memory)
    print(checksum(new_memory))


if __name__ == "__main__":
    main()
