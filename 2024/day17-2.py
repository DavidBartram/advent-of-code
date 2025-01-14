import os
from collections import deque

registers = {"A": 4, "B": 0, "C": 0}

instructions = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 3, 5, 5, 3, 0]


def get_combo_operand(operand, registers):
    if operand in {0, 1, 2, 3}:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    else:
        return None


def binary(num, digits):
    return format(num, "0" + str(digits) + "b")


def execute(instructions, registers):
    stack = deque(instructions)
    output = []

    while len(stack) > 0:
        ins = stack.popleft()
        operand = stack.popleft()

        combo_operand = get_combo_operand(operand, registers)

        if ins == 0:
            registers["A"] = registers["A"] // 2**combo_operand
        elif ins == 1:
            registers["B"] = registers["B"] ^ operand
            # bitwise XOR of B and operand
        elif ins == 2:
            registers["B"] = combo_operand % 8
        elif ins == 3:
            # jump
            if registers["A"] != 0:
                stack = deque(instructions[operand:])
        elif ins == 4:
            registers["B"] = registers["B"] ^ registers["C"]
            # bitwise XOR of B and C
        elif ins == 5:
            output.append(combo_operand % 8)
        elif ins == 6:
            registers["B"] = registers["A"] // 2**combo_operand
        elif ins == 7:
            registers["C"] = registers["A"] // 2**combo_operand

    return output


def get_neighbours(string, target, instructions):

    nbs = []
    for i in range(0, 8):
        attempt = string + binary(i, 3)
        attempt_dec = int(attempt, 2)
        result = execute(instructions, {"A": attempt_dec, "B": 0, "C": 0})
        if result == target:
            nbs.append(attempt)
    return nbs


def dfs(instructions, string, visited=set()):
    visited.add(string)
    target_length = (len(string) // 3) + 1
    target = instructions[-target_length:]

    nbs = get_neighbours(string, target, instructions)

    for nb in nbs:
        if nb not in visited:
            dfs(instructions, nb, visited)

    return visited


valid = dfs(instructions, "")

valid_length = [int(v, 2) for v in valid if len(v) // 3 == len(instructions)]

print(min(valid_length))

# for vl in valid_length:
#     print(execute(instructions, {"A": vl, "B": 0, "C": 0}))
