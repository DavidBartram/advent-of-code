import sys
from statistics import median

with open(sys.argv[1]) as file:
    data = file.read().splitlines()


bracketmap = {')':'(', ']': '[', '}': '{','>':'<'}

invbracketmap = {value:key for key,value in bracketmap.items()}

openers = set(bracketmap.values())


def completion_string(line):
    stack = []

    for char in line:
        if char in openers:
            stack.append(char)
        
        else:
            if stack[-1] == bracketmap[char]:
                stack.pop()
            else:
                return False
    
    stack.reverse()

    stack = ''.join([invbracketmap[x] for x in stack])

    return stack

def score(string):
    scoremap = {')':1, ']':2, '}':3, '>':4}
    score = 0
    for char in string:
        score = score*5 + scoremap[char]

    return score

def solve_part_two(lines):
    scores = [score(completion_string(line)) for line in lines if completion_string(line)]
    
    return(median(scores))


print(solve_part_two(data))
