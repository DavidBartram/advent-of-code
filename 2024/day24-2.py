import os
from collections import deque, defaultdict
from itertools import product


def read_input_file(file_path):

    with open(file_path, "r") as file:
        contents = file.read()

    input_raw, instructions_raw = contents.split("\n\n")

    input = {}
    for line in input_raw.split("\n"):
        wire, value = line.split(": ")
        input[wire] = int(value)

    instructions = {}
    for line in instructions_raw.split("\n"):
        in1, op, in2, _, out = line.split(" ")
        instructions[out] = (in1, in2, op)

    z_length = sum(["z" in wire for wire in instructions])

    return input, instructions, z_length


gates = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "XOR": lambda x, y: x ^ y,
}


def get_wire_string(letter, number):
    return letter + str(number).rjust(2, "0")


# since the input is an attempt at a ripple adder
# we should expect the following rules to hold for every zn:
# zn = sn XOR cn   [z bit = sum bit XOR carry bit]
# cn = ic_(n-1) OR c_(n-1)   [carry bit = intermediate carry OR carry from previous bit]
# ic_(n-1) = sn AND c_(n-1)   [intermediate carry = sum bit AND carry from previous bit]
# c_n-1 = x_(n-1) AND y_(n-1) [carry from previous bit = x bit AND y bit]
# sn = xn XOR yn [sum bit = x bit XOR y bit]


def verify_sum_bit(wire, num, instructions):
    # verify zn = sn XOR cn   [z bit = sum bit XOR carry bit]
    if wire not in instructions:
        return False
    in1, in2, op = instructions[wire]
    if op == "XOR":
        return sorted([in1, in2]) == [
            get_wire_string("x", num),
            get_wire_string("y", num),
        ]
    else:
        return False


def verify_carry_bit(wire, num, instructions):
    # verify cn = ic_(n-1) OR c_(n-1)   [carry bit = intermediate carry OR carry from previous bit]

    # also, by calling other functions, verify:
    # ic_(n-1) = sn AND c_(n-1)   [intermediate carry = sum bit AND carry from previous bit]
    # c_n-1 = x_(n-1) AND y_(n-1) [carry from previous bit = x bit AND y bit]
    if wire not in instructions:
        return False
    in1, in2, op = instructions[wire]

    if num == 1:
        if op == "AND":
            return sorted([in1, in2]) == ["x00", "y00"]
        else:
            return False

    return (
        verify_carry_previous(in1, num - 1, instructions)
        and verify_intermediate_carry(in2, num - 1, instructions)
        or verify_carry_previous(in2, num - 1, instructions)
        and verify_intermediate_carry(in1, num - 1, instructions)
    )


def verify_carry_previous(wire, num, instructions):
    # verify c_n-1 = x_(n-1) AND y_(n-1) [carry from previous bit = x bit AND y bit]

    if wire not in instructions:
        return False

    in1, in2, op = instructions[wire]

    if op == "AND":
        return sorted([in1, in2]) == [
            get_wire_string("x", num),
            get_wire_string("y", num),
        ]
    else:
        return False


def verify_intermediate_carry(wire, num, instructions):
    # verify ic_(n-1) = sn AND c_(n-1)   [intermediate carry = sum bit AND carry from previous bit]

    if wire not in instructions:
        return False

    in1, in2, op = instructions[wire]

    if op == "AND":
        return (
            verify_sum_bit(in1, num, instructions)
            and verify_carry_bit(in2, num, instructions)
            or verify_sum_bit(in2, num, instructions)
            and verify_carry_bit(in1, num, instructions)
        )
    else:
        return False


def verify_output_bit(num, instructions):
    # verify xn = sn ^ cn
    # by calling other functions, verify the other rules

    wire = get_wire_string("z", num)
    if wire not in instructions:
        return False

    in1, in2, op = instructions[wire]

    if op == "XOR":
        if num == 0:
            return sorted([in1, in2]) == ["x00", "y00"]
        else:
            return (
                verify_sum_bit(in1, num, instructions)
                and verify_carry_bit(in2, num, instructions)
                or verify_sum_bit(in2, num, instructions)
                and verify_carry_bit(in1, num, instructions)
            )
    else:
        return False


def find_next_failure(instructions, z_length, start=0):
    # returns None if all are valid

    for i in range(start, z_length - 1):
        if not verify_output_bit(i, instructions):
            return i

    return None


def find_swaps(instructions, z_length):
    swaps = []

    next_failure = find_next_failure(instructions, z_length)
    print(f"Next failure: {next_failure}")

    while next_failure:

        for wire1 in instructions:
            if not next_failure:
                break

            for wire2 in instructions:
                if wire1 == wire2:
                    continue
                if tuple(sorted([wire1, wire2])) in swaps:
                    continue

                if not next_failure:
                    break

                # swap and see if we get further
                instructions[wire1], instructions[wire2] = (
                    instructions[wire2],
                    instructions[wire1],
                )

                next_failure_2 = find_next_failure(
                    instructions, z_length, start=next_failure
                )

                if not next_failure_2 or next_failure_2 > next_failure:
                    # the swap has made progress
                    swaps.append(tuple(sorted([wire1, wire2])))
                    next_failure = next_failure_2
                    print(f"Next failure: {next_failure}")
                    break
                else:
                    # the swap didn't help, so swap back
                    instructions[wire1], instructions[wire2] = (
                        instructions[wire2],
                        instructions[wire1],
                    )

    return swaps


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input24-2")
    input, instructions, z_length = read_input_file(file_path)

    swaps = find_swaps(instructions, z_length)

    print(f"\nFinal swaps: {swaps}")

    swap_wires = []
    for pair in swaps:
        swap_wires.extend(list(pair))

    print("\nFinal result (sorted swapped wires):\n")
    print(",".join(sorted(swap_wires)))


if __name__ == "__main__":
    main()
