import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.read()

    split_contents = contents.split("\n\n")

    patterns = frozenset(split_contents[0].strip().split(", "))

    targets = split_contents[1].split("\n")

    return patterns, targets


def dfs(patterns, string, target, memo):

    if (string, target) in memo:
        return memo[(string, target)]

    if string == target:
        memo[(string, target)] = True
        return True

    else:
        nbs = set()
        for pattern in patterns:
            attempt = string + pattern
            if target.startswith(attempt):
                nbs.add(attempt)

    for nb in nbs:
        if dfs(patterns, nb, target, memo):
            memo[(nb, target)] = True
            return True

    memo[(string, target)] = False


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input19-1")
    patterns, targets = read_input_file(file_path)

    count = 0
    for i, target in enumerate(targets):
        result = dfs(patterns, "", target, {})
        if result:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
