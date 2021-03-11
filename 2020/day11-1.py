import sys
from copy import deepcopy

with open(sys.argv[1]) as file:
    initial = file.read().splitlines()
    initial = [list(line) for line in initial]

def is_occ(i,j, layout):
        cols = len(layout[0])
        rows = len(layout)
        x = layout[i][j] if 0 <= i <= rows-1 and 0 <= j <= cols-1 else '.'
        if x == '#':
            return True
        else:
            return False

def advance(layout):
    cols = len(layout[0])
    rows = len(layout)
    newlayout = deepcopy(layout)

    for i in range(rows):
        for j in range(cols):

            adj_occ = 0
            if is_occ(i-1,j-1, layout):
                adj_occ += 1
            if is_occ(i-1,j, layout):
                adj_occ += 1
            if is_occ(i-1,j+1, layout):
                adj_occ += 1
            if is_occ(i,j-1, layout):
                adj_occ += 1
            if is_occ(i,j+1, layout):
                adj_occ += 1
            if is_occ(i+1,j-1, layout):
                adj_occ += 1
            if is_occ(i+1,j, layout):
                adj_occ += 1
            if is_occ(i+1,j+1, layout):
                adj_occ += 1
            
            if layout[i][j] == 'L' and adj_occ == 0:
                newlayout[i][j] = '#'
            
            if layout[i][j] == '#' and adj_occ >= 4:
                newlayout[i][j] = 'L'
    
    return newlayout

def findstability(layout):
    oldlayout = layout
    while True:
        oldlayout, newlayout = oldlayout, advance(oldlayout)
        if newlayout == oldlayout:
            count = 0
            for row in newlayout:
                count += row.count('#')
            return count
        else:
            oldlayout = newlayout


print(findstability(initial))


