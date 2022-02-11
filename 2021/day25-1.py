import sys
from copy import deepcopy


with open(sys.argv[1]) as file:
    data = file.read().splitlines()

data = [list(row) for row in data]
#print(data)

width = len(data[0])
height = len(data)

def advance(grid):
    grid1 = deepcopy(grid)

    for i,row in enumerate(grid):
        for j,char in enumerate(row):
            if char=='>':
                destination = row[(j+1)%width]
                if destination == '.':
                    grid1[i][j] ='.'
                    grid1[i][(j+1)%width] = '>'

    grid2 = deepcopy(grid1)
    
    for i,row in enumerate(grid1):
        for j,char in enumerate(row):
            if char=='v':
                destination = grid1[(i+1)%height][j]
                if destination == '.':
                    grid2[i][j] = '.'
                    grid2[(i+1)%height][j] = 'v'
    
    return grid2

def find_stability(grid):
    stable = False
    i = 0

    while stable == False:
        i+=1
        newgrid = advance(grid)
        if newgrid == grid:
            stable = True
        else:
            grid = newgrid
    
    return i

print(find_stability(data))
