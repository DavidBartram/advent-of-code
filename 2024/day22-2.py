import os


def read_input_file(file_path):
    with open(file_path, "r") as file:
        contents = file.readlines()

    contents = [int(line.strip()) for line in contents]

    return contents


def mix(value1, value2):
    return value1 ^ value2


def prune(value):
    return value % 16777216


def advance(value):
    x = prune(mix(value * 64, value))

    y = prune(mix(x // 32, x))

    return prune(mix(y * 2048, y))


def advance_n_steps(value, n):
    prices = []
    price_deltas = []
    for _ in range(n):
        prices.append(int(str(value)[-1]))
        value = advance(value)
        if len(prices) > 1:
            price_deltas.append(prices[-1] - prices[-2])

    return value, prices, price_deltas


# take a list of integers
# for each consecutive sublist of length 4
# return a dict from the sublist to the index in the list where it first appears
def get_sublist_to_index_dict(initial_value, lst, lst2, sublist_to_price_dict={}):
    for i in range(len(lst) - 3):
        sublist = tuple(lst[i : i + 4])

        if sublist not in sublist_to_price_dict:
            sublist_to_price_dict[sublist] = {initial_value: lst2[i + 4]}
        elif initial_value not in sublist_to_price_dict[sublist]:
            sublist_to_price_dict[sublist][initial_value] = lst2[i + 4]

    return sublist_to_price_dict


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input22-2")
    initial_values = read_input_file(file_path)

    prices_dict = {}
    price_deltas_dict = {}
    sublist_to_price_dict = {}
    for initial_value in initial_values:
        value, prices, price_deltas = advance_n_steps(initial_value, 2000)
        prices_dict[initial_value] = prices
        price_deltas_dict[initial_value] = price_deltas
        sublist_to_price_dict = get_sublist_to_index_dict(
            initial_value, price_deltas, prices, sublist_to_price_dict
        )

    max_value = 0
    for key in sublist_to_price_dict:
        value = sum(sublist_to_price_dict[key].values())
        if value == 1701:
            print(key)
            for key2 in sublist_to_price_dict[key]:
                print(f"{key2}: {sublist_to_price_dict[key][key2]}")
        max_value = max(max_value, value)

    print(max_value)


if __name__ == "__main__":
    main()
