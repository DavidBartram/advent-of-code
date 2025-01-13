import os
from collections import deque, defaultdict

WIDTH = 71
HEIGHT = 71


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    grid = defaultdict(lambda: -1)

    for i in range(WIDTH):
        for j in range(HEIGHT):
            grid[(i, j)] = float("inf")

    for t, line in enumerate(lines):
        splitline = line.strip().split(",")
        x, y = splitline[0], splitline[1]
        grid[(int(x), int(y))] = t

    return lines, grid


dirs = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def get_neighbours(point, grid, t):
    nbs = set()
    (x, y) = point

    for dir in dirs:
        dx, dy = dirs[dir]
        value = grid[(x + dx, y + dy)]
        result = t < grid[(x + dx, y + dy)]
        if result:
            nbs.add((x + dx, y + dy))

    return nbs


def get_reachable(grid, q: deque, end, t):
    visited = set()
    while not len(q) == 0:
        point = q.popleft()
        nbs = get_neighbours(point, grid, t)
        for nb in nbs:
            if nb not in visited:
                q.append(nb)
                visited.add(nb)

    if end not in visited:
        return visited, True

    return visited, False


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input18-2")
    lines, grid = read_input_file(file_path)

    start = (0, 0)
    end = (WIDTH - 1, HEIGHT - 1)

    reachable = set()
    for j in range(HEIGHT):
        for i in range(WIDTH):
            reachable.add((i, j))

    low, high = 0, len(lines) - 1
    result_t = -1

    while low <= high:
        mid = (low + high) // 2
        q = deque()
        q.append(start)

        reachable, finished = get_reachable(grid, q, end, mid)

        if finished:
            result_t = mid
            high = mid - 1
        else:
            low = mid + 1

    if result_t != -1:
        print(lines[result_t])
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
