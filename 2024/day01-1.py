import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    columns = [[], []]
    for line in lines:
        values = map(int, line.split())
        for i, values in enumerate(values):
            columns[i].append(values)

    return columns


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input01-1")
    columns = read_input_file(file_path)

    assert len(columns) == 2

    sorted_columns = [sorted(column) for column in columns]

    distance = sum([abs(x - y) for (x, y) in zip(*sorted_columns)])

    print(distance)


if __name__ == "__main__":
    main()
