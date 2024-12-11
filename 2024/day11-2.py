import os
import math


def read_input_file(file_path):
    with open(file_path, "r") as file:
        stones = file.read().split(" ")

        state = {}
        for stone in stones:
            if stone in state:
                state[int(stone)] += 1
            else:
                state[int(stone)] = 1

    return state


def count_digits(num: int):
    if num in {0, 1}:
        return 1
    else:
        return int(math.log10(num)) + 1


def apply_rules(state: dict):
    new_state = {}

    # Rule 2 & 3
    for key in list(state.keys()):
        if key == 0 or state[key] == 0:
            continue

        else:
            digits = count_digits(key)
            if digits % 2 == 0:
                half = 10 ** (digits // 2)
                first_half = key // half
                second_half = key % half
                new_state[first_half] = new_state.get(first_half, 0) + state[key]
                new_state[second_half] = new_state.get(second_half, 0) + state[key]
            else:
                new_state[key * 2024] = new_state.get(key * 2024, 0) + state[key]

    # Rule 1
    new_state[1] = new_state.get(1, 0) + state.get(0, 0)

    return new_state


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input11-2")
    state = read_input_file(file_path)

    for _ in range(75):
        new_state = apply_rules(state)
        state = new_state

    print(sum(state.values()))


if __name__ == "__main__":
    main()
