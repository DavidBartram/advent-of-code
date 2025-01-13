import os
from collections import deque
from copy import deepcopy


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    blocks = input.split("\n\n")

    grid = [
        list(
            line.strip()
            .replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        )
        for line in blocks[0].split("\n")
    ]

    instructions = list(blocks[1].replace("\n", ""))

    return grid, instructions


instruction_to_direction = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def affected_positions_horizontal(x, y, dir, grid):
    # find the set of points affected by
    # the horizontal movement of a [ or ] at (x,y)
    visited = set()
    visited.add((x, y))

    while grid[y][x] != ".":
        # step in the direction of motion
        x, y = x + dir[0], y + dir[1]

        if grid[y][x] in {"[", "]"}:
            # We've hit another box part, so add it to affected positions
            visited.add((x, y))
        if grid[y][x] == "#":
            # We've hit a wall in the direction of motion
            # no positions will move
            return None

    return visited


def get_partner(x, y, char):
    if char == "[":
        return (x + 1, y)
    if char == "]":
        return (x - 1, y)
    else:
        raise Exception("bad input for partner function")


def affected_positions_vertical(x, y, dir, grid):
    # use BFS to find the set of points affected by
    # the vertical movement of a [ or ] at (x,y)

    # This is a nice example, all the [ and ] in this need to move up
    # if the next instruction is ^

    # ##........##
    # ##.....[].##
    # ##.[].[]..##
    # ##..[][]..##
    # ##...[]...##
    # ##....@...##

    visited = set()
    q = deque()
    q.append((x, y))
    while q:
        pos = q.popleft()
        visited.add(pos)

        # Ensure the "other half" of any affected box gets added to the queue
        # e.g. if a ] moves, then the [ to the left of it also needs to move
        char = grid[pos[1]][pos[0]]
        partner = get_partner(pos[0], pos[1], char)
        if partner not in visited:
            q.append(partner)

        # step in the direction of motion
        x2, y2 = pos[0] + dir[0], pos[1] + dir[1]
        char2 = grid[y2][x2]

        if char2 in {"[", "]"}:
            # we've hit part of another box, so we need to add its position to the queue
            if (x2, y2) not in visited:
                q.append((x2, y2))
        elif char2 == "#":
            # we've hit a wall in the direction of motion
            # so nothing will move
            return None
    return visited


def move_set(positions, dir, grid):
    original = dict()

    for x, y in positions:
        # clear all the positions
        # storing the original char for each pos in a dict
        original[(x, y)] = grid[y][x]
        grid[y][x] = "."

    for x, y in positions:
        # write the original chars in their new position in the grid
        grid[y + dir[1]][x + dir[0]] = original[(x, y)]


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
            robot_set = set()
            robot_set.add(robot_pos)
            move_set(robot_set, dir, grid)
            robot_pos = robot_pos[0] + dir[0], robot_pos[1] + dir[1]

        if grid[y2][x2] in {"[", "]"}:
            if dir in {(1, 0), (-1, 0)}:
                affected_set = affected_positions_horizontal(x2, y2, dir, grid)
            else:
                affected_set = affected_positions_vertical(x2, y2, dir, grid)

            if affected_set:
                affected_set.add(robot_pos)
                move_set(affected_set, dir, grid)
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
            if grid[y][x] == "[":
                score += 100 * y + x
    return score


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input15-2")
    grid, instructions = read_input_file(file_path)
    start = get_robot_start(grid)

    apply_instructions(start, instructions, grid)

    print(score_grid(grid))


if __name__ == "__main__":
    main()
