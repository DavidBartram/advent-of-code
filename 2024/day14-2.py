import os
import re
from functools import reduce
from operator import mul

WIDTH = 101
HEIGHT = 103


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


def count_neighbours(pos, counts):
    x, y = pos
    nbs = 0
    for direction in {
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    }:
        neighbour_pos = (x + direction[0], y + direction[1])
        if neighbour_pos in counts:
            nbs += 1
    return nbs


def render(counts):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) in counts:
                print(counts[(x, y)], end="")
            else:
                print(".", end="")
        print()


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input14-1")
    robots = read_input_file(file_path)

    neighbour_scores = []
    for i in range(0, HEIGHT * WIDTH):
        steps = i
        final_counts = {}
        for robot in robots:
            new_pos = get_robot_position(robot, steps)
            if new_pos not in final_counts:
                final_counts[new_pos] = 1
            else:
                final_counts[new_pos] += 1

        neighbour_score = 0
        for pos in final_counts:
            neighbour_score += count_neighbours(pos, final_counts)

        neighbour_score = neighbour_score / len(final_counts.keys())

        neighbour_scores.append(neighbour_score)

        if neighbour_scores[-1] > 5 * sum(neighbour_scores) / len(neighbour_scores):
            print(i, neighbour_score)
            render(final_counts)


if __name__ == "__main__":
    main()
