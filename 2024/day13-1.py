import numpy as np
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

        prize_array = np.array(prize)
        matrix = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])

        problems.append((matrix, prize_array))

    return problems


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input13-1")
    problems = read_input_file(file_path)

    cost = 0
    for problem in problems:
        matrix = problem[0]
        prize = problem[1]

        if np.linalg.det(matrix) == 0:
            continue

        inverse_matrix = np.linalg.inv(matrix)

        solution = np.dot(inverse_matrix, prize)

        # hacky way to check for integer solution
        # round it and then check if the solution works
        # not guaranteed to be resilient to floating point errors
        solution = np.round(solution)
        if not np.array_equal(np.dot(matrix, solution), prize):
            continue

        if np.max(solution) > 100:
            continue

        cost += int(3 * solution[0] + solution[1])

    print(cost)


if __name__ == "__main__":
    main()
