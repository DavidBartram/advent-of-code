import sys
from statistics import median

with open(sys.argv[1]) as file:
    data = file.read().splitlines()


map = {')':'(', ']': '[', '}': '{','>':'<'}

invmap = {value:key for key,value in map.items()}

openers = set(map.values())


def correct(line):
    stack = []

    for char in line:
        if char in openers:
            stack.append(char)
        
        else:
            if stack[-1] == map[char]:
                stack.pop()
            else:
                return False
    
    stack.reverse()

    stack = ''.join([invmap[x] for x in stack])

    return score(stack)

def score(string):
    scoremap = {')':1, ']':2, '}':3, '>':4}
    score = 0
    for char in string:
        score = score*5 + scoremap[char]

    return score

def solve_part_two(lines):
    scores = [correct(line) for line in lines if correct(line)]
    
    return(median(scores))


print(solve_part_two(data))

