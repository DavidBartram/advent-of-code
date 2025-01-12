import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}


def is_in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_plots_dfs(visited, x, y, plant, grid):

    if not is_in_bounds(x, y, grid) or grid[y][x] != plant:
        return {"Area": 0, "Perimeter": 1}
    elif (x, y) in visited:
        return {"Area": 0, "Perimeter": 0}

    else:
        visited.add((x, y))
        A, P = 1, 0

        for direction in directions:
            delta = get_plots_dfs(
                visited, x + direction[0], y + direction[1], plant, grid
            )
            A += delta["Area"]
            P += delta["Perimeter"]

    return {"Area": A, "Perimeter": P}


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input12-1")
    grid = read_input_file(file_path)

    visited = set()
    cost = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            plot = get_plots_dfs(visited, x, y, grid[y][x], grid)
            cost += plot["Area"] * plot["Perimeter"]

    print(cost)


if __name__ == "__main__":
    main()
