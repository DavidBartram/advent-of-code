import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    input = [
        [int(value) if value != "." else 100 for value in line.strip()]
        for line in lines
    ]

    return input


directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}

memo = set()


def is_in_bounds(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])


def search(x, y, seen, grid, height=0):
    if is_in_bounds(x, y, grid) and grid[y][x] == height:

        if height == 9:
            if (x, y) not in seen:
                seen.add((x, y))
                return 1
            else:
                return 0

        else:
            return sum(
                search(x + dx, y + dy, seen, grid, height + 1) for dx, dy in directions
            )

    else:
        return 0


def get_trailheads(grid):
    trailheads = set()
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            value = grid[y][x]
            if value == 0:
                trailheads.add((x, y))

    return trailheads


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input10-1")
    grid = read_input_file(file_path)

    trailheads = get_trailheads(grid)
    scores = {}

    for trailhead in trailheads:
        scores[trailhead] = search(trailhead[0], trailhead[1], set(), grid)

    sum_ = 0
    for _, v in scores.items():
        sum_ += v

    print(sum_)


if __name__ == "__main__":
    main()
