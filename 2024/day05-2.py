import os
from copy import deepcopy

def read_input_file(file_path):
    with open(file_path, "r") as file:
        input = file.read()

    split = input.split("\n\n")

    rules = [line.split("|") for line in split[0].split("\n")]

    updates = [line.split(",") for line in split[1].split("\n")]

    return rules, updates


def rules_to_dict(rules):
    rules_dict = {}
    for rule in rules:
        if rule[0] in rules_dict:
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]

    return rules_dict


def is_correctly_ordered(update, rules_dict):
    for i, page in enumerate(update):
        if page not in rules_dict:
            pass
        else:
            previous_pages = update[:i]
            if any(value in rules_dict[page] for value in previous_pages):
                return False,i

    return True,None

def find_middle_odd(list):
    assert len(list) % 2 == 1
    middle_index = len(list) // 2
    return list[middle_index]

def reposition_element(update, rules_dict,i):
    previous_pages = update[:i]
    new_pos = None

    for j,prev_page in enumerate(previous_pages):
        if prev_page in rules_dict[update[i]]:
            new_pos = j
            break
    
    update_copy = deepcopy(update)
    
    update_copy.insert(new_pos, update_copy.pop(i))

    return update_copy


def reposition_all_elements(update, rules_dict): 
    is_ordered, first_violation = is_correctly_ordered(update, rules_dict)

    if is_ordered:
        return update
    
    else:
        new_update = reposition_element(update, rules_dict, first_violation)
        return reposition_all_elements(new_update, rules_dict)

def sum_middles(updates, rules_dict):

    sum = 0
    for update in updates:
        if not is_correctly_ordered(update, rules_dict)[0]:
            new_update = reposition_all_elements(update, rules_dict)
            sum += int(find_middle_odd(new_update))

    return sum


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input05-2")
    rules, updates = read_input_file(file_path)

    rules_dict = rules_to_dict(rules)

    print(sum_middles(updates, rules_dict))


if __name__ == "__main__":
    main()
