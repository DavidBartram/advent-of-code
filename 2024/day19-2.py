import os
from functools import cache


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()

    split_contents = contents.split("\n\n")

    patterns = frozenset(split_contents[0].strip().split(", "))

    targets = split_contents[1].split("\n")

    return patterns, targets


def ways(target, patterns, memo):
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    count = 0
    for pattern in patterns:
        if target.startswith(pattern):
            count += ways(target[len(pattern) :], patterns, memo)

    memo[target] = count
    return count


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input19-2")
    patterns, targets = read_input_file(file_path)

    count = 0
    for target in targets:
        memo = {}
        count += ways(target, patterns, memo)
    print(count)


if __name__ == "__main__":
    main()
