import os
from itertools import combinations
from math import gcd


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


def is_in_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def get_antennas(grid):
    antennas = dict()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            freq = grid[y][x]
            if freq == ".":
                continue
            if freq not in antennas:
                antennas[freq] = [(x, y)]
            else:
                antennas[freq].append((x, y))
    return antennas


def get_points(dx, dy, x, y, width, height):
    points = set()
    while is_in_bounds(x, y, width, height):
        points.add((x, y))
        x += dx
        y += dy
    return points


def get_antinodes_from_pair(pt1, pt2, width, height):
    x1, y1 = pt1
    x2, y2 = pt2

    dx = x2 - x1
    dy = y2 - y1

    denom = gcd(dx, dy)

    dx = dx // denom
    dy = dy // denom

    antinodes = set()

    antinodes = antinodes.union(get_points(dx, dy, x2, y2, width, height))
    antinodes = antinodes.union(get_points(-dx, -dy, x2, y2, width, height))

    return antinodes


def get_all_antinodes(antennas, width, height):

    antinodes = set()

    for freq in antennas:
        points = antennas[freq]
        pairs = combinations(points, 2)
        for pair in pairs:
            pt1, pt2 = pair
            antinodes = antinodes.union(
                get_antinodes_from_pair(pt1, pt2, width, height)
            )

    return antinodes


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input08-2")
    grid = read_input_file(file_path)

    width = len(grid[0])
    height = len(grid)

    antennas = get_antennas(grid)

    print(len(get_all_antinodes(antennas, width, height)))


if __name__ == "__main__":
    main()
