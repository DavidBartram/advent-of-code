import os
from operator import add, mul


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    equations = []
    for line in lines:
        total = int(line.split(":")[0])
        values = [int(value) for value in line.split(":")[1].split()]
        equations.append((total, values))

    return equations


def check_equation(acc, total, values):
    if len(values) == 0:
        return acc == total
    if acc == None:
        acc = values[0]
        return check_equation(acc, total, values[1:])
    if acc > total:
        return False
    else:
        return check_equation(mul(acc, values[0]), total, values[1:]) or check_equation(
            add(acc, values[0]), total, values[1:]
        )


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input07-1")
    equations = read_input_file(file_path)

    sum = 0
    for equation in equations:
        total, values = equation
        if check_equation(None, total, values):
            sum += total

    print(sum)


if __name__ == "__main__":
    main()
