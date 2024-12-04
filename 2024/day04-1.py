import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


directions = {(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)}


def is_in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def count_grid(grid, word):
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            count += count_point(x, y, grid, word)
    return count


def count_point(x, y, grid, word):

    count = 0

    if grid[y][x] != word[0]:
        return count
    for direction in directions:
        if check_direction(x, y, direction, grid, word):
            count += 1

    return count


def check_direction(x, y, direction, grid, word):
    for i in range(1, len(word)):
        x += direction[0]
        y += direction[1]
        if not is_in_bounds(x, y, grid):
            return False
        elif grid[y][x] != word[i]:
            return False

    return True


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input04-1")
    grid = read_input_file(file_path)

    print(count_grid(grid, "XMAS"))


if __name__ == "__main__":
    main()
