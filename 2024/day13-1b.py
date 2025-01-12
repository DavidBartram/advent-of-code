import os
import re


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()

    blocks = contents.split("\n\n")

    problems = []

    for block in blocks:
        lines = block.split("\n")
        button_pattern = re.compile(r"Button ([AB]): X\+(\d+), Y\+(\d+)")
        prize_pattern = re.compile(r"Prize: X=(\d+), Y=(\d+)")

        buttonA_match = button_pattern.match(lines[0])
        buttonB_match = button_pattern.match(lines[1])
        prize_match = prize_pattern.match(lines[2])

        buttonA = (int(buttonA_match.group(2)), int(buttonA_match.group(3)))
        buttonB = (int(buttonB_match.group(2)), int(buttonB_match.group(3)))
        prize = (int(prize_match.group(1)), int(prize_match.group(2)))

        problems.append((buttonA, buttonB, prize))

    return problems


def solve_problem_integer(buttonA, buttonB, prize):
    a0, a1 = buttonA
    b0, b1 = buttonB
    p0, p1 = prize

    det = a0 * b1 - a1 * b0

    if det == 0:
        return None

    x = p0 * b1 - p1 * b0  # must be an integer as all coefficients are integers
    y = p1 * a0 - p0 * a1  # must be an integer as all coefficients are integers

    for w in (x, y):
        if (
            w % det != 0
        ):  # if the remainder is not 0, then the solution is not an integer
            return None

    x = x // det
    y = y // det

    if not (
        0 <= x <= 100 and 0 <= y <= 100
    ):  # negative solutions are not valid, for part 1 solutions >100 are not valid
        return None

    return 3 * x + y


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input13-1")
    problems = read_input_file(file_path)

    cost = 0
    for problem in problems:
        buttonA, buttonB, prize = problem

        solution = solve_problem_integer(buttonA, buttonB, prize)
        if solution:
            cost += solution

    print(cost)


if __name__ == "__main__":
    main()
