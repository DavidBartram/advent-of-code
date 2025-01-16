import os
from functools import cache


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.readlines()

    contents = [int(line.strip()) for line in contents]

    return contents


def mix(value1, value2):
    return value1 ^ value2


def prune(value):
    return value % 16777216


def advance(value):
    x = prune(mix(value * 64, value))

    y = prune(mix(x // 32, x))

    return prune(mix(y * 2048, y))


def advance_n_steps(value, n):
    for _ in range(n):
        value = advance(value)

    return value


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input22-1")
    initial_values = read_input_file(file_path)

    sum = 0
    for initial_value in initial_values:
        sum += advance_n_steps(initial_value, 2000)

    print(sum)


if __name__ == "__main__":
    main()
