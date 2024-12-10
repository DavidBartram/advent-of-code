import os
from itertools import combinations
from collections import deque


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

        input = [int(value) for value in input]
    return input


def get_files_and_gaps(input):
    files = []
    gaps = []
    pos = 0
    id = 0
    for i, value in enumerate(input):
        if i % 2 == 0:
            files.append({"pos": pos, "id": id, "size": value})
            id += 1
        else:
            gaps.append({"pos": pos, "size": value})

        pos += value

    return files, gaps


def move_file(gaps, file):
    for i, gap in enumerate(gaps):
        if gap["size"] >= file["size"] and gap["pos"] <= file["pos"]:
            file["pos"] = gap["pos"]

            if gap["size"] == file["size"]:
                gaps.pop(i)
            else:
                gap["pos"] += file["size"]
                gap["size"] -= file["size"]

            break

    return None


def move_files(files, gaps):

    files.reverse()

    for file in files:
        move_file(gaps, file)

    return None


def checksum(files):
    sum = 0
    for file in files:
        for k in range(file["pos"], file["pos"] + file["size"]):
            sum += file["id"] * k

    return sum


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input09-2")
    input = read_input_file(file_path)

    files, gaps = get_files_and_gaps(input)

    move_files(files, gaps)

    print(checksum(files))


if __name__ == "__main__":
    main()
