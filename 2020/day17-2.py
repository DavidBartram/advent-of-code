import sys
from copy import deepcopy
from itertools import product

with open(sys.argv[1]) as file:
    initial = file.read().replace('#','1').replace('.','0').splitlines()
    initial = [list(line) for line in initial]
    initial = [list(map(int, line)) for line in initial]

def neighbours(i,j,k,l):

    steps = list(product([-1,0,1], repeat=4))

    steps.remove((0,0,0,0))
        
    neighbours = []
        
    for (a,b,c,d) in steps:
        w,z,y,x = i+a, j+b, k+c, l+d
        neighbours.append((w,z,y,x))
    
    return neighbours

def neighdict(grid):
    dict_ = {}
    for coords in grid:
        i,j,k,l = coords
        dict_[i,j,k,l] = neighbours(i,j,k,l)
    return dict_

def advance(grid,nbdict):
    newgrid = deepcopy(grid)

    for (i,j,k,l) in grid:
            nbs = nbdict[(i,j,k,l)]
            occ = 0

            for (w,x,y,z) in nbs:
                if grid.get((w,x,y,z),0) == 1:
                    occ += 1
            
            if grid.get((i,j,k,l),0) == 0 and occ == 3:
                newgrid[(i,j,k,l)]= 1
            
            if grid.get((i,j,k,l),0) == 1 and occ != 3 and occ != 2:
                newgrid[(i,j,k,l)] = 0
    
    return newgrid

print(initial)

n = 6

w=len(initial[0])+n+1
h=len(initial)+n+1
d=n+1
grid = {(i,j,k,l):0 for i in range(-w,w) for j in range(-h,h) for k in range(-d,d) for l in range(-d,d)}

for i, row in enumerate(initial):
    for j, num in enumerate(row):
        grid[(i,j,0,0)] = num


nbdict = neighdict(grid)

for i in range(n):
    newgrid = advance(grid,nbdict)
    grid = newgrid

count=0
for coords, val in grid.items():
    if val == 1:
        count += 1

print(count)

