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


def similarity_score(columns):
    assert len(columns) == 2

    return sum(value * columns[1].count(value) for value in columns[0])


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input01-2")
    columns = read_input_file(file_path)

    print(similarity_score(columns))


if __name__ == "__main__":
    main()
