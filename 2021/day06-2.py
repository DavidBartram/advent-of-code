import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().split(',')

data = [int(x) for x in data]

counts = defaultdict(lambda: 0)

for x in data:
    counts[x] += 1

def advance(state):
    newstate = defaultdict(lambda: 0)

    

    for t in range(8,-1,-1):
        if t==8:
            newstate[8] = state[0]
        elif t==6:
            newstate[6] = state[7] + state[0]
        else:
            newstate[t] = state[t+1]
    
    return newstate

generations = 256

for i in range(generations):
    counts = advance(counts)

print(sum(counts.values()))
