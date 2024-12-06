import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


# only diagonal directions are relevant
# check_direction handles the opposite direction
# so only need one dir on each diagonal axis
directions = {(1, 1), (1, -1)}


def is_in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def count_grid(grid):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            count += check_point(x, y, grid)
    return count


def check_point(x, y, grid):

    if grid[y][x] != "A":
        return 0

    if all(check_direction(x, y, direction, grid) for direction in directions):
        return 1
    else:
        return 0


def check_direction(x, y, direction, grid):
    x1 = x + direction[0]
    y1 = y + direction[1]

    x2 = x - direction[0]
    y2 = y - direction[1]

    if not is_in_bounds(x1, y1, grid) or not is_in_bounds(x2, y2, grid):
        return False

    point1 = grid[y1][x1]
    point2 = grid[y2][x2]

    return {point1, point2} == {"M", "S"}


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input04-2")
    grid = read_input_file(file_path)

    print(count_grid(grid))


if __name__ == "__main__":
    main()
