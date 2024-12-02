import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    rows = [list(map(int, line.split())) for line in lines]

    return rows


def is_row_safe(row):

    diffs = [(b - a) for a, b in zip(row, row[1:])]

    asc_desc_check = all(diff < 0 for diff in diffs) or all(diff > 0 for diff in diffs)

    step_check = all(1 <= abs(diff) <= 3 for diff in diffs)

    return asc_desc_check and step_check


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input02-1")
    rows = read_input_file(file_path)

    # for row in rows:
    #     print(is_row_safe(row))

    print(sum(is_row_safe(row) for row in rows))


if __name__ == "__main__":
    main()
