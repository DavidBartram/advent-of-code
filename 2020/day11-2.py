import sys
from copy import deepcopy

with open(sys.argv[1]) as file:
    initial = file.read().splitlines()
    initial = [list(line) for line in initial]


def ray(i,j,k,l, grid):
    cols = len(grid[0])
    rows = len(grid)

    y,x = i+k, j+l

    if 0<=y<rows and 0<=x<cols:
        if grid[y][x] != '.':
            return (y,x)
        elif 0<=y+k<rows and 0<=x+l<cols:
            return ray(y,x,k,l,grid)
        else:
            return False
    else:
        return False

def nbs(i,j, grid):

    steps = [(-1,-1), (-1,0), (-1,+1), (0,-1), (0,+1), (+1,-1), (+1,0), (+1,+1)]
        
    nbs = []
        
    for (k,l) in steps:
        if ray(i,j,k,l,grid):
            nbs.append(ray(i,j,k,l,grid))
    
    return nbs

def nbdict(grid):
    dict_ = {}
    cols = len(grid[0])
    rows = len(grid)
    for i in range(rows):
        for j in range(cols):
            dict_[i,j] = nbs(i,j,grid)
    return dict_

def advance(grid,nbdict):
    cols = len(grid[0])
    rows = len(grid)
    newgrid = deepcopy(grid)

    for i in range(rows):
        for j in range(cols):

            nbs = nbdict[i,j]
            occ = 0

            for y,x in nbs:
                if grid[y][x] == '#':
                    occ += 1
            
            if grid[i][j] == 'L' and occ == 0:
                newgrid[i][j] = '#'
            
            if grid[i][j] == '#' and occ >= 4:
                newgrid[i][j] = 'L'
    
    return newgrid

def findstability(grid, nbdict):
    oldgrid = grid
    while True:
        newgrid = advance(oldgrid, nbdict)
        if newgrid == oldgrid:
            count = 0
            for row in newgrid:
                count += row.count('#')
            return count
        else:
            oldgrid = newgrid

nbdict = nbdict(initial)

output = findstability(initial, nbdict)

print(output)
