import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}

rotation = {
    (0, 1): (-1, 0),
    (1, 0): (0, 1),
    (0, -1): (1, 0),
    (-1, -0): (0, -1),
}  # rotate 90 degrees clockwise


def is_in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_plant(x, y, grid):
    if not is_in_bounds(x, y, grid):

        return None
    else:
        return grid[y][x]


def get_plots_dfs(visited, x, y, plant, direction, grid):

    if get_plant(x, y, grid) != plant:

        rotated_direction = rotation[direction]

        if (
            get_plant(x + rotated_direction[0], y + rotated_direction[1], grid) == plant
            or get_plant(
                x - direction[0] + rotated_direction[0],
                y - direction[1] + rotated_direction[1],
                grid,
            )
            != plant
        ):
            # then you've found a corner, and number of corners = number of sides
            return {"Area": 0, "Perimeter": 1, "Sides": 1}
        else:
            return {"Area": 0, "Perimeter": 1, "Sides": 0}

    elif (x, y) in visited:
        return {"Area": 0, "Perimeter": 0, "Sides": 0}

    else:
        visited.add((x, y))
        A, P, S = 1, 0, 0

        for direction in directions:
            delta = get_plots_dfs(
                visited, x + direction[0], y + direction[1], plant, direction, grid
            )
            A += delta["Area"]
            P += delta["Perimeter"]
            S += delta["Sides"]

    return {"Area": A, "Perimeter": P, "Sides": S}


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input12-2")
    grid = read_input_file(file_path)

    visited = set()
    cost = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            plot = get_plots_dfs(visited, x, y, get_plant(x, y, grid), (1, 0), grid)
            cost += plot["Area"] * plot["Sides"]

    print(cost)


if __name__ == "__main__":
    main()
