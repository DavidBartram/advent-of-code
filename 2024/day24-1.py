import os
from collections import deque, defaultdict
from itertools import product


def read_input_file(file_path):

    with open(file_path, "r") as file:
        contents = file.read()

    input_raw, instructions_raw = contents.split("\n\n")

    input = {}
    for line in input_raw.split("\n"):
        wire, value = line.split(": ")
        input[wire] = int(value)

    instructions = {}
    for line in instructions_raw.split("\n"):
        in1, op, in2, _, out = line.split(" ")
        instructions[out] = (in1, in2, op)

    z_length = sum(["z" in wire for wire in instructions])

    return input, instructions, z_length


gates = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}


def print_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")


def simulate_wire(wire, input, instructions):

    visited = input.copy()
    if wire in visited:
        return visited[wire]

    in1, in2, op = instructions[wire]
    visited[wire] = gates[op](
        simulate_wire(in1, visited, instructions),
        simulate_wire(in2, visited, instructions),
    )

    return visited[wire]


def get_wire_string(letter, number):
    return letter + str(number).rjust(2, "0")


def simulate(input, instructions, z_length):
    z = ""
    for i in range(z_length):
        wire = get_wire_string("z", i)
        z += str(simulate_wire(wire, input, instructions))

    return z[::-1]


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input24-1")
    input, instructions, z_length = read_input_file(file_path)

    # print_dict(input)
    # print_dict(instructions)

    # print(z_length)

    print(int(simulate(input, instructions, z_length), 2))


if __name__ == "__main__":
    main()
