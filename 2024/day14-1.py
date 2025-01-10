import os
import re
from functools import reduce
from operator import mul

WIDTH = 101
HEIGHT = 103
STEPS = 100


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.readlines()

    robots = []

    for line in contents:
        pattern = re.compile(r"p=(-{0,1}\d+),(-{0,1}\d+) v=(-{0,1}\d+),(-{0,1}\d+)")
        match = pattern.match(line)
        (x, y, vx, vy) = map(int, match.groups())

        robots.append((x, y, vx, vy))

    return robots


def get_robot_position(robot, n):
    x, y, vx, vy = robot

    x1 = (x + n * vx) % WIDTH
    y1 = (y + n * vy) % HEIGHT

    return (x1, y1)


def get_quadrant(pos):
    x, y = pos

    if x == WIDTH // 2 or y == HEIGHT // 2:
        return None

    elif x < WIDTH // 2 and y < HEIGHT // 2:
        return 1
    elif x > WIDTH // 2 and y < HEIGHT // 2:
        return 2
    elif x < WIDTH // 2 and y > HEIGHT // 2:
        return 3
    elif x > WIDTH // 2 and y > HEIGHT // 2:
        return 4


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input14-1")
    robots = read_input_file(file_path)

    final_counts = {}

    for robot in robots:
        new_pos = get_robot_position(robot, STEPS)
        if new_pos not in final_counts:
            final_counts[new_pos] = 1
        else:
            final_counts[new_pos] += 1

    quadrant_scores = {1: 0, 2: 0, 3: 0, 4: 0}

    for pos in final_counts:
        quadrant = get_quadrant(pos)
        if quadrant:
            quadrant_scores[quadrant] += final_counts[pos]

    print(reduce(mul, quadrant_scores.values()))


if __name__ == "__main__":
    main()
