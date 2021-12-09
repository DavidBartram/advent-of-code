import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

grid = defaultdict(lambda: 100)

for j, row in enumerate(data):
    for i, item in enumerate(row):
        grid[(i,j)] = int(item)

def neighbours(i,j,grid):
    neigh_list = []

    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for step in steps:
        (dx,dy) = step
        neigh_list.append(grid[(i+dx,j+dy)])
    
    return neigh_list

def risk_level(grid):
    risk = 0
    for j, row in enumerate(data):
        for i, _ in enumerate(row):
            if grid[(i,j)] < min(neighbours(i,j,grid)):
                risk += grid[(i,j)] + 1

    return risk

print(risk_level(grid))
