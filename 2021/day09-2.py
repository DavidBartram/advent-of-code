import sys
from collections import defaultdict
from functools import reduce
import operator

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

def neighbour_coords(i,j,grid):
    coords_list = []
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for step in steps:
        (dx,dy) = step
        if grid[(i+dx,j+dy)] != 100:
            coords_list.append((i+dx,j+dy))
    
    return coords_list

def get_basin_ID(i,j,grid,basin_IDs):
    if basin_IDs[(i,j)] >= -1:
        #print('basin ID already known ', basin_IDs[(i,j)])
        return basin_IDs[(i,j)]

    elif grid[(i,j)] == 9:
        basin_IDs[(i,j)] = -1
        return -1
    
    else:
        neigh_coords = neighbour_coords(i,j,grid)
        neigh_vals = {grid[(x,y)]:(x,y) for (x,y) in neigh_coords}

        min_value = min(neigh_vals.keys())
        min_coords = neigh_vals[min_value]

        #print('min_value ', min_value)
        #print('min_coords ', min_coords)

        if grid[(i,j)] < min_value:
            new_basin_ID = max(basin_IDs.values()) + 1
            basin_IDs[(i,j)] = new_basin_ID
            #print('new basin ID ', new_basin_ID)
            return new_basin_ID
        
        else:
            return get_basin_ID(min_coords[0], min_coords[1], grid, basin_IDs)


def find_basins(grid):
    basin_IDs = defaultdict(lambda: -2)
    for j, row in enumerate(data):
        for i, _ in enumerate(row):
            #print('grid coords ', (i,j))
            basin_IDs[(i,j)] = get_basin_ID(i,j,grid,basin_IDs)

    return basin_IDs
    

def three_largest_basins(basin_IDs):
    counts = defaultdict(lambda: 0)
    for value in basin_IDs.values():
        if value >= 0:
            counts[value] += 1
    
    counts_list = list(counts.values())
    counts_list.sort(reverse=True)

    return reduce(operator.mul,counts_list[:3],1)

basin_IDs = find_basins(grid)

total = three_largest_basins(basin_IDs)

print(total)

            






