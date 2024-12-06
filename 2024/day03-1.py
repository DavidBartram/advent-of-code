import os
import re


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    return input


def sum_instructions(input):
    pattern = re.compile("mul\((\d+),(\d+)\)")

    return sum(int(a) * int(b) for a, b in pattern.findall(input))


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input03-1")
    input = read_input_file(file_path)

    print(sum_instructions(input))


if __name__ == "__main__":
    main()
