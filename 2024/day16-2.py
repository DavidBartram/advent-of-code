import os
from queue import PriorityQueue


def read_input_file(file_path):
    with open(file_path, "r") as file:
        grid = file.readlines()

    grid = [line.strip() for line in grid]

    return grid


dirs = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

dir_change_costs = {
    "NE": 1000,
    "NS": 2000,
    "NW": 1000,
    "EN": 1000,
    "ES": 1000,
    "EW": 2000,
    "SN": 2000,
    "SE": 1000,
    "SW": 1000,
    "WN": 1000,
    "WE": 2000,
    "WS": 1000,
}


def get_value(grid, x, y):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return None
    return grid[y][x]


def get_neighbours(point, grid):
    nbs = {}
    (x, y, facing) = point

    for dir in dirs:
        if dir == facing:
            continue
        nbs[(x, y, dir)] = dir_change_costs[facing + dir]

    (dx, dy) = dirs[facing]

    next_value = get_value(grid, x + dx, y + dy)
    if next_value and next_value != "#":
        nbs[(x + dx, y + dy, facing)] = 1

    return nbs


def backtrack(parents, start, end):

    current = end
    visited = set()
    
    visited.add(current)
    current_parents = parents[current]

    if current_parents == {}:
        return visited

    for parent in parents[current]:
        new_visited = backtrack(parents, start, parent)
        visited = visited.union(new_visited)
    
    return visited


def dijkstra(grid, start, end):
    q = PriorityQueue()
    q.put((0, (start[0], start[1], "E")))
    costs = {(start[0], start[1], "E"): 0}

    parents = {(start[0], start[1], "E"): {}}

    while not q.empty():
        (d, point) = q.get()
        nbs = get_neighbours(point, grid)
        for nb in nbs:
            cost = nbs[nb]
            if d + cost < costs.get(nb, float("inf")):
                costs[nb] = d + cost
                parents[nb] = {point}
                q.put((costs[nb], nb))
            if d + cost == costs.get(nb):
                parents[nb].add(point)

    end_costs = [costs[(end[0], end[1], dir)] for dir in dirs]

    min_cost = min(end_costs)
    visited = set()
    for dir in dirs:
        if costs[(end[0], end[1], dir)] == min_cost:
            visited = visited.union(
                backtrack(parents, (start[0], start[1], "E"), (end[0], end[1], dir))
            )

    visited_positions = {v[:2] for v in visited}

    return len(visited_positions)


def get_start_and_end(grid):
    start = None
    end = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if get_value(grid, x, y) == "S":
                start = (x, y)
            if get_value(grid, x, y) == "E":
                end = (x, y)
    return start, end


def render(grid):
    for row in grid:
        print(row)

    print("\n")


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input16-2")
    grid = read_input_file(file_path)
    start, end = get_start_and_end(grid)

    print(dijkstra(grid, start, end))


if __name__ == "__main__":
    main()
