import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.readlines()

    input = [line.strip() for line in input]

    return input


directions = {"N":(0, -1), "E":(1, 0), "S": (0, 1), "W": (-1, 0)}

turn_right = {"N": "E", "E": "S", "S": "W", "W": "N"}


def is_in_bounds(pos, grid):
    return 0 <= pos[1] < len(grid) and 0 <= pos[0] < len(grid[0])


def one_step(pos, direction, grid):
    new_pos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
    
    if not is_in_bounds(new_pos, grid):
        return new_pos, direction
    if grid[new_pos[1]][new_pos[0]] != "#":
        return new_pos, direction
    else:
        # print(f"Obstacle at {new_pos}")
        # print(f"Current direction: {direction}, new_direction: {turn_right[direction]}")
        # print(f"Visited so far: {visited}")
        # print(f"Visited so far length: {len(visited)}")
        # print("\n\n")
        #if we assume the point is never fully surrounded by obstacles
        #then this will eventually return a new position and direction
        return one_step(pos, turn_right[direction],grid)

def get_start_pos(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "^":
                return (x, y)

def simulate(grid):
    pos = get_start_pos(grid)
    visited = set()
    direction = "N"
    while True:
        if is_in_bounds(pos, grid):
            visited.add(pos)
            pos, direction = one_step(pos, direction, grid)
        else:
            break
        
    return visited

def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input06-1")
    grid = read_input_file(file_path)

    visited = simulate(grid)

    print(len(visited))


if __name__ == "__main__":
    main()
