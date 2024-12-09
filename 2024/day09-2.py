import os
from itertools import combinations
from collections import deque


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

        input = [int(value) for value in input]
    return input


def get_files_and_gaps(input):
    files = {}
    gaps = {}
    pos = 0
    id = 0
    for i, value in enumerate(input):
        if i % 2 == 0:
            files[pos] = {"id": id, "size": value}
            id += 1
        else:
            gaps[pos] = {"size": value}

        pos += value

    return files, gaps


def move_file(files, gaps, pos):
    gap_positions = deque(sorted(list(gaps.keys())))

    file = files[pos]

    while len(gap_positions) > 0:
        gap_pos = gap_positions[0]

        if gaps[gap_pos]["size"] >= file["size"] and gap_pos < pos:
            files[gap_pos] = file

            if gaps[gap_pos]["size"] > file["size"]:
                new_gap_size = gaps[gap_pos]["size"] - file["size"]
                new_gap_pos = gap_pos + file["size"]
                new_gap = {"size": new_gap_size}
                gaps[new_gap_pos] = new_gap
                gap_positions.popleft()
                gap_positions.appendleft(new_gap_pos)

            del files[pos]
            del gaps[gap_pos]

            break

        gap_positions.popleft()

    return None


def move_files(files, gaps):

    positions = deque(sorted(list(files.keys()), reverse=True))
    while len(positions) > 0:
        if len(positions) % 1000 == 0:
            print(len(positions))
        move_file(files, gaps, positions[0])
        positions.popleft()

    return None


def checksum(files):
    sum = 0
    for pos in files:
        for k in range(pos, pos + files[pos]["size"]):
            sum += files[pos]["id"] * k

    return sum


def print_files(files):
    keys = list(files.keys())
    keys.sort()

    for k in keys:
        print(f"{k}: {files[k]}")


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input09-2")
    input = read_input_file(file_path)

    files, gaps = get_files_and_gaps(input)
    move_files(files, gaps)

    print(checksum(files))


if __name__ == "__main__":
    main()
