import sys
from copy import deepcopy
from itertools import product

with open(sys.argv[1]) as file:
    initial = file.read().replace('#','1').replace('.','0').splitlines()
    initial = [list(line) for line in initial]
    initial = [list(map(int, line)) for line in initial]

def neighbours(i,j,k):

    steps = list(product([-1,0,1], repeat=3))

    steps.remove((0,0,0))
        
    neighbours = []
        
    for (l,m,n) in steps:
        z,y,x = i+l, j+m, k+n
        neighbours.append((z,y,x))
    
    return neighbours

def neighdict(matrix):
    dict_ = {}
    for coords in matrix:
        i,j,k= coords
        dict_[i,j,k] = neighbours(i,j,k)
    return dict_

def advance(matrix,nbdict):
    newmatrix = deepcopy(matrix)

    for (i,j,k) in matrix:
            nbs = nbdict[(i,j,k)]
            occ = 0

            for (x,y,z) in nbs:
                if matrix.get((x,y,z),0) == 1:
                    occ += 1
            
            if matrix.get((i,j,k),0) == 0 and occ == 3:
                newmatrix[(i,j,k)]= 1
            
            if matrix.get((i,j,k),0) == 1 and occ != 3 and occ != 2:
                newmatrix[(i,j,k)] = 0
    
    return newmatrix

print(initial)

n = 6

w=len(initial[0])+n+1
h=len(initial)+n+1
d=n+1
matrix = {(i,j,k):0 for i in range(-w,w) for j in range(-h,h) for k in range(-d,d)}

for i, row in enumerate(initial):
    for j, num in enumerate(row):
        matrix[(i,j,0)] = num


nbdict = neighdict(matrix)

for i in range(n):
    newmatrix = advance(matrix,nbdict)
    matrix = newmatrix

count=0
for coords, val in matrix.items():
    if val == 1:
        count += 1

print(count)
