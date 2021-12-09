import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Since all the grid heights are between 0 and 9, 100 is a suitable default value
# When the grid dictionary is asked to look up coords beyond the grid, it will return 100
# this ensures that coords beyond the grid will result in a value lower than coords within the grid
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
