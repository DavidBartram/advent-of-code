import sys

with open(sys.argv[1]) as file:
    data = file.read().splitlines()


map = {')':'(', ']': '[', '}': '{','>':'<'}

openers = set(map.values())


def check_line(line):

    stack = []

    for char in line:
        if char in openers:
            stack.append(char)
        
        else:
            if stack[-1] == map[char]:
                stack.pop()
            else:
                return char

def solve_part_one(lines):
    scoremap = {')':3, ']':57, '}':1197, '>':25137}
    scores = []
    for line in lines:
        illegal_char = check_line(line)
        if illegal_char:
            scores.append(scoremap[illegal_char])
    return sum(scores)


print(solve_part_one(data))

