import os
from collections import deque

registers = {"A": 34615120, "B": 0, "C": 0}

instructions = [2,4,1,5,7,5,1,6,0,3,4,3,5,5,3,0]


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

    print(",".join([str(x) for x in output]))
    print(registers)


execute(instructions, registers)
