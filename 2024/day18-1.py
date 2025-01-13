import os
from queue import PriorityQueue
from collections import defaultdict

WIDTH = 71
HEIGHT = 71
MAX_INPUT = 1024


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    grid = defaultdict(lambda: "#")

    for i in range(WIDTH):
        for j in range(HEIGHT):
            grid[(i, j)] = "."

    for k, line in enumerate(lines):
        splitline = line.strip().split(",")
        x, y = splitline[0], splitline[1]
        grid[(int(x), int(y))] = "#"
        if k == MAX_INPUT - 1:
            break

    return grid

dirs = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

def get_neighbours(point, grid):
    nbs = set()
    (x, y) = point

    for dir in dirs:
        dx, dy = dirs[dir]

        if grid[(x + dx, y + dy)] != "#":
            nbs.add((x + dx, y + dy))

    return nbs


def dijkstra(grid, q, end):
    costs = {}
    while not q.empty():
        (d, point) = q.get()
        nbs = get_neighbours(point, grid)
        for nb in nbs:
            if d + 1 < costs.get(nb, float("inf")):
                costs[nb] = d + 1
                q.put((costs[nb], nb))

    return costs[end]


def render(grid):
    for j in range(HEIGHT):
        for i in range(WIDTH):
            print(grid[(i, j)], end="")
        print("\n")

    print("\n")


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input18-1")
    grid = read_input_file(file_path)

    start = (0, 0)
    end = (WIDTH-1, HEIGHT-1)

    q = PriorityQueue()
    q.put((0, start))

    print(dijkstra(grid, q, end))


if __name__ == "__main__":
    main()
