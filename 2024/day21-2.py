import os
from collections import deque, defaultdict
from itertools import product


def read_input_file(file_path):

    with open(file_path, "r") as file:
        input = file.readlines()

    return [line.strip() for line in input]


numeric_pad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

direction_pad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

dirs = {(0, 1): "v", (0, -1): "^", (1, 0): ">", (-1, 0): "<"}


def get_neighbours(x, y, pad):
    # returns a list of neighbours to a button
    # each entry in the list is a tuple containing (x,y), dir
    # where (x,y) are the coordinates of the neighbour
    # and dir is the direction to reach the neighbour (e.g. "v" for down)
    neighbours = []
    for dx, dy in dirs:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_y < len(pad) and 0 <= new_x < len(pad[0]):
            if pad[new_y][new_x] != None:
                neighbours.append(((new_x, new_y), dirs[(dx, dy)]))

    return neighbours


def find_optimal_paths(pad):
    # returns a dict from pair of buttons to list of optimal paths between them
    # all paths end in A because you have to push A to tell the robot to push the final button
    # e.g. on numereric pad, optimal_paths[('7','6')] = ['v>>A', '>v>A', '>>vA']
    # e.g. on direction pad, optimal_paths[('<', 'A')] = ['>^>A', '>>^A']

    # dict from value to coordinates, e.g. "1" -> (2, 0)
    positions = {}
    for j, row in enumerate(pad):
        for i, val in enumerate(row):
            if val != "None":
                positions[val] = (i, j)

    optimal_paths = defaultdict(list)

    for pos1 in positions:
        for pos2 in positions:
            if pos1 == pos2:
                # you're already at the desired position
                # so just press A to push the button
                optimal_paths[(pos1, pos2)] = ["A"]
                continue
            else:
                # BFS for the shortest path between pos1 and pos2

                # min_length will improve as we find shorter paths
                min_length = float("inf")

                # deque contains tuples of coordinates and current path as a string
                q = deque([(positions[pos1], "")])

                visited = set()

                while q:
                    (x, y), current_path = q.popleft()

                    visited.add((x, y))

                    for (new_x, new_y), dir in get_neighbours(x, y, pad):
                        if (new_x, new_y) in visited:
                            continue
                        path = current_path + dir
                        if (new_x, new_y) == positions[pos2]:
                            # we've reached the desired position
                            # we need to push the button
                            path = path + "A"
                            if len(path) < min_length:
                                # this path is shorter
                                min_length = len(path)
                                # discard any previous paths
                                optimal_paths[(pos1, pos2)] = [path]
                            elif len(path) == min_length:
                                optimal_paths[(pos1, pos2)].append(path)
                        else:
                            q.append(((new_x, new_y), path))

    return optimal_paths


def find_optimal_length(path, depth, dir_paths, dir_lengths, memo={}):

    # memoize
    # we will revisit the same path, depth many many times
    if (path, depth) in memo:
        return memo[(path, depth)]

    # the robot starts at "A"
    # we want to consider all consecutive buttons in the path
    # e.g. for path = "v>>A", we want to consider ("A","v"), ("v",">"), (">","A")
    # this zip will achieve that
    pairs = list(zip("A" + path, path))

    if depth == 1:
        # we are considering the last directional pad before the numeric pad

        # the optimal length is the sum of the lengths of the shortest
        # paths between each pair of buttons in the path
        optimal_length = sum([dir_lengths[(a, b)] for a, b in pairs])
        memo[(path, depth)] = optimal_length
        return optimal_length
    else:
        # we are at an intermediate directional pad
        # we need to build up the optimal length
        optimal_length = 0

        # consider each pair of buttons in the path
        for a, b in pairs:
            # there are multiple paths between a and b ("subpaths")
            # we need to find the optimal length
            # by taking the minimum of the optimal length for each subpath
            subpath_lengths = [
                find_optimal_length(subpath, depth - 1, dir_paths, dir_lengths, memo)
                for subpath in dir_paths[(a, b)]
            ]
            optimal_length += min(subpath_lengths)

        memo[(path, depth)] = optimal_length
        return optimal_length


def all_optimal_paths(full_path, pairwise_optimal_paths):

    # the robot starts at "A"
    # we want to consider all consecutive buttons in the path
    # e.g. for full_path = "143A", we want to consider ("A","1"), ("1","4"), ("4","3"), ("3","A")
    # this zip will achieve that
    pairs = list(zip("A" + full_path, full_path))

    possibilities = [pairwise_optimal_paths[(a, b)] for a, b in pairs]

    # we then want a cartesian product of all these optimal possibilities

    # e.g. using the path "143A" on the numeric pad
    # ('A', '1'): ['^<<A', '<^<A']
    # ('1', '4'): ['^A']
    # ('4', '3'): ['v>>A', '>v>A', '>>vA']
    # ('3', 'A'): ['vA']

    # we get an optimal paths if we combine any selection of one from each list,
    # e.g. optimal paths include (the | chars are not part of the path, just to show the separation)
    # '^<<A|^A|v>>A|vA'
    # '<^<A|^A|>>vA|vA'
    # etc

    return ["".join(p) for p in product(*possibilities)]


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input21-2")
    input = read_input_file(file_path)

    num_paths = find_optimal_paths(numeric_pad)
    dir_paths = find_optimal_paths(direction_pad)

    dir_lengths = {key: len(dir_paths[key][0]) for key in dir_paths}

    max_depth = 25

    score = 0

    # we might revisit the same path, depth across multiple lines of the input
    # so worth keeping the memo between lines
    memo = {}

    for line in input:
        # first we need to get all possible optimal paths on the numerical pad
        # you can think of this as depth=0
        initial = all_optimal_paths(line, num_paths)
        # now for each optimal path we recurse from depth = max_depth to depth = 1
        # we want the minimum length out of all these possibilities
        length = min(
            [
                find_optimal_length(path, max_depth, dir_paths, dir_lengths, memo)
                for path in initial
            ]
        )
        score += length * int(line[:-1])

    print(score)


if __name__ == "__main__":
    main()
