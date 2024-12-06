import os
import re


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    return input


def sum_instructions(input):
    pattern = re.compile("mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")

    # output of pattern.findall(input) will look like this because of the capture groups:
    # [('2', '4', '', ''), ('', '', '', "don't()"), ('5', '5', '', ''), ('11', '8', '', ''), ('', '', 'do()', ''), ('8', '5', '', '')

    do = True
    sum = 0

    for result in pattern.findall(input):
        if result[0] != "" and result[1] != "":
            if do:
                sum += int(result[0]) * int(result[1])
        elif result[2] == "do()":
            do = True
        elif result[3] == "don't()":
            do = False

    return sum


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input03-2")
    input = read_input_file(file_path)

    print(sum_instructions(input))


if __name__ == "__main__":
    main()
