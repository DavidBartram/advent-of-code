import os
from copy import deepcopy
from multiprocessing import Pool, cpu_count


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}

turn_right = {"N": "E", "E": "S", "S": "W", "W": "N"}


def is_in_bounds(pos, grid):
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])


def step_or_turn(pos, direction, grid):
    new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

    if not is_in_bounds(new_pos, grid):
        return new_pos, direction
    if grid[new_pos[1]][new_pos[0]] != "#":
        return new_pos, direction
    else:
        return pos, turn_right[direction]


def get_start_pos(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                return (x, y)


def has_loop(grid, start_posdir, new_obstacle):
    pos = start_posdir[0]
    direction = start_posdir[1]
    visited = set()
    new_grid = deepcopy(grid)
    new_grid[new_obstacle[1]] = (
        new_grid[new_obstacle[1]][: new_obstacle[0]]
        + "#"
        + new_grid[new_obstacle[1]][new_obstacle[0] + 1 :]
    )
    while True:
        if is_in_bounds(pos, new_grid):
            if (pos, direction) in visited:
                return True
            visited.add((pos, direction))
            pos, direction = step_or_turn(pos, direction, new_grid)
        else:
            return False


def initial_path(start_posdir, grid):
    pos = start_posdir[0]
    direction = start_posdir[1]
    visited = []
    while True:
        if is_in_bounds(pos, grid):
            visited.append((pos, direction))
            pos, direction = step_or_turn(pos, direction, grid)
        else:
            break

    return visited


def check_loop(args):
    grid, start_pos, obstacle_pos = args
    return has_loop(grid, start_pos, obstacle_pos)


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input06-2")
    grid = read_input_file(file_path)

    start_posdir = (get_start_pos(grid), "N")

    # Get the initial path with no new obstacle
    # these are the only points we will need to
    # try adding new obstacles to
    initial_path_list = initial_path(start_posdir, grid)

    obstacle_pos_and_start_posdirs = []

    for i, (pos, dir) in enumerate(initial_path_list):
        if i == 0:
            continue

        # We only need need to include unique positions for obstacles
        # obstacles do not care about direction
        if pos not in [pos for pos, _ in obstacle_pos_and_start_posdirs]:
            # When we place a new obstacle, we can start the new simulation from the
            # position and direction immedately before the obstacle
            # NOTE: We do not need to add the previously visited elements from the initial path
            # if we have a loop, then it will inevitably repeat starting from the position before the obstacle
            # I experimented with taking into account a set of the elements before the obstacle, but it slowed down the process
            new_element = (pos, initial_path_list[i - 1])
            obstacle_pos_and_start_posdirs.append(new_element)

    with Pool(cpu_count()) as pool:
        results = pool.map(
            check_loop,
            [
                (grid, new_start_pos, obstacle_pos)
                for (obstacle_pos, new_start_pos) in obstacle_pos_and_start_posdirs
            ],
        )

    loop_positions = sum(results)

    print(loop_positions)


if __name__ == "__main__":
    main()
