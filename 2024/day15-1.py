import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    blocks = input.split("\n\n")

    grid = [list(line.strip()) for line in blocks[0].split("\n")]

    instructions = list(blocks[1].replace("\n", ""))

    return grid, instructions


instruction_to_direction = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def move(current, new_pos, grid):
    x, y = current
    x2, y2 = new_pos
    grid[y2][x2] = grid[y][x]
    grid[y][x] = "."


def apply_instructions(start, instructions, grid):

    robot_pos = start

    for instruction in instructions:
        # render(grid)
        # print(f"Robot pos: {robot_pos}")
        # print(f"Instruction: {instruction}")
        dir = instruction_to_direction[instruction]

        x2, y2 = robot_pos[0] + dir[0], robot_pos[1] + dir[1]

        if grid[y2][x2] == "#":
            continue

        if grid[y2][x2] == ".":
            move(robot_pos, (x2, y2), grid)
            robot_pos = robot_pos[0] + dir[0], robot_pos[1] + dir[1]

        if grid[y2][x2] == "O":
            block_start = (x2, y2)
            while grid[y2][x2] == "O":
                x2, y2 = x2 + dir[0], y2 + dir[1]
            if grid[y2][x2] == "#":
                continue
            if grid[y2][x2] == ".":
                move(
                    block_start, (x2, y2), grid
                )  # moving the start of the block of Os past the end is the same as moving the block
                move(robot_pos, block_start, grid)  # still need to move the robot
            robot_pos = robot_pos[0] + dir[0], robot_pos[1] + dir[1]


def render(grid):
    for row in grid:
        print("".join(row))

    print("\n")


def get_robot_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                return (x, y)


def score_grid(grid):
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O":
                score += 100 * y + x
    return score


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input15-1")
    grid, instructions = read_input_file(file_path)
    start = get_robot_start(grid)

    apply_instructions(start, instructions, grid)

    print(score_grid(grid))


if __name__ == "__main__":
    main()
