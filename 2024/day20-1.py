import os
from itertools import product


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [list(line.strip()) for line in input]

    return input


def render(grid):
    for row in grid:
        print("|".join(row))

    print("\n")


def get_start_and_end(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                start = (x, y)
            if grid[y][x] == "E":
                end = (x, y)
    return start, end


dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def get_next_point(point, grid, visited):
    (x, y) = point
    for dir in dirs:
        (dx, dy) = dir
        if (x + dx, y + dy) in visited or not (
            0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)
        ):
            continue
        next_value = grid[y + dy][x + dx]
        if next_value and next_value != "#":
            return (x + dx, y + dy)


def get_path(grid, start, end):
    visited = set()
    current = start
    path = {}
    count = 0
    while current != end:
        path[current] = count
        visited.add(current)
        current = get_next_point(current, grid, visited)
        count += 1

    path[end] = count
    grid[end[1]] = grid[end[1]][: end[0]] + [str(count)] + grid[end[1]][end[0] + 1 :]
    return path


def get_cheats_for_point(grid, point, path):
    (x, y) = point
    nbs = []
    for dir in dirs:
        (dx, dy) = dir
        if not (0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid)):
            continue
        next_value = grid[y + dy][x + dx]
        if next_value and next_value != "#":
            nbs.append(path[(x + dx, y + dy)])

    diffs = [abs(x - y) for x, y in product(nbs, repeat=2)]

    if len(diffs) == 0:
        return 0

    return max(diffs) - 2


def get_cheats(grid, path):
    cheats = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                cheat_value = get_cheats_for_point(grid, (x, y), path)
                if cheat_value in cheats:
                    cheats[cheat_value] += 1
                else:
                    cheats[cheat_value] = 1
    return cheats


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input20-1")
    grid = read_input_file(file_path)

    start, end = get_start_and_end(grid)

    path = get_path(grid, start, end)

    cheats = get_cheats(grid, path)

    total = 0
    for key in cheats:
        if key >= 100:
            total += cheats[key]

    print(total)


if __name__ == "__main__":
    main()
