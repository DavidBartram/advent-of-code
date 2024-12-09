import os
from itertools import combinations


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


def get_antinodes_from_pair(pt1, pt2, width, height):
    x1, y1 = pt1
    x2, y2 = pt2

    vec = (x2 - x1, y2 - y1)

    antinodes = set()

    # the puzzle description suggests we don't need to worry about antinodes
    # between the two points
    an1 = (x2 + vec[0], y2 + vec[1])
    an2 = (x1 - vec[0], y1 - vec[1])

    for an in [an1, an2]:
        if is_in_bounds(an[0], an[1], width, height):
            antinodes.add(an)

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
    file_path = os.path.join(repo_root, "2024/input/input08-1")
    grid = read_input_file(file_path)

    width = len(grid[0])
    height = len(grid)

    antennas = get_antennas(grid)

    print(len(get_all_antinodes(antennas, width, height)))


if __name__ == "__main__":
    main()
