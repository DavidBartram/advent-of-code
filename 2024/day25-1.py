import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    blocks = input.split("\n\n")

    keys = []
    locks = []
    lock = None

    for block in blocks:
        if block.startswith("#####"):
            rows = block.split("\n")[1:]
            lock = True
        else:
            rows = block.split("\n")[:-1]
            lock = False

        counts = {}

        for i in range(len(rows)):
            counts[i] = 0

        available_space = len(rows) - 1

        for row in rows:
            for i, val in enumerate(row):
                if val == "#":
                    if i in counts:
                        counts[i] += 1

        if lock:
            locks.append([counts[i] for i in sorted(counts.keys())])
        else:
            keys.append([counts[i] for i in sorted(counts.keys())])

    return locks, keys, available_space


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input25-1")
    locks, keys, available_space = read_input_file(file_path)
    score = 0

    for lock in locks:
        for key in keys:
            if all([sum(x) <= available_space for x in zip(lock, key)]):
                score += 1
    print(score)


if __name__ == "__main__":
    main()
