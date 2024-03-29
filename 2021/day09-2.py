import sys
from collections import defaultdict, Counter
from functools import reduce
import operator
from random import randint

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Since all the grid heights are between 0 and 9, 100 is a suitable default value
grid = defaultdict(lambda: 100)

for j, row in enumerate(data):
    for i, item in enumerate(row):
        grid[(i,j)] = int(item)

rows = len(data)
cols = len(data[0])

def neighbour_coords(i,j,grid):
    #returns a list of coords of points adjacent to (i,j) in the grid
    coords_list = []
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
    
    for step in steps:
        (dx,dy) = step
        if grid[(i+dx,j+dy)] != 100: #default value is 100 if (i+dx,j_dy) is not already in grid
            coords_list.append((i+dx,j+dy))
    
    return coords_list

def get_basin_ID(i,j,grid,basin_IDs):
    #recursive function to calculate the basin ID of a grid position (i,j)
    #high points (height=9) will be assigned basin ID = -1
    #other points will be assigned the same ID as the low point of the basin they are in

    if basin_IDs[(i,j)] >= -1:
        #if the basin ID of the point (i,j) is already known, return the known value
        return basin_IDs[(i,j)]

    elif grid[(i,j)] == 9:
        #assign high points a basin ID of -1
        basin_IDs[(i,j)] = -1
        return -1
    
    else:

        #find the value and coords of the lowest point neighbouring (i,j)

        neigh_coords = neighbour_coords(i,j,grid)
        neigh_vals = {grid[(x,y)]:(x,y) for (x,y) in neigh_coords}

        min_value = min(neigh_vals.keys())
        min_coords = neigh_vals[min_value]

        if grid[(i,j)] < min_value:
            #if (i,j) is a new low point, we need to assign it a new basin ID
            new_basin_ID = max(basin_IDs.values()) + 1
            basin_IDs[(i,j)] = new_basin_ID
            #print('new basin ID ', new_basin_ID)
            return new_basin_ID
        
        else:
            #if (i,j) is not known, and is not a new low point
            #recursively call the function for the coords of the lowest neighbouring point
            #this recursion will eventually reach a previously known value or a new low point
            #in either case the basin ID of the original point will match this value
            return get_basin_ID(min_coords[0], min_coords[1], grid, basin_IDs)


def find_basins(grid):
    #populates a dictionary where the keys are the coordinates on the grid and the values are the basin IDs
    #high points (height=9) will be assigned basin ID = -1
    #other points will be assigned the same ID as the low point of the basin they are in
    basin_IDs = defaultdict(lambda: -2) #-2 is the ID of any grid position that has not been assigned a basin yet
    for j in range(rows):
        for i in range(cols):
            #print('grid coords ', (i,j))
            basin_IDs[(i,j)] = get_basin_ID(i,j,grid,basin_IDs)

    return basin_IDs
    

def three_largest_basins(basin_IDs):
    #The high points (height=9) were assigned basin ID = -1
    #high points are not in any basin so should not be counted
    counts = Counter([x for x in basin_IDs.values() if x >=0])

    counts_list = sorted(list(counts.values()), reverse=True)

    return reduce(operator.mul,counts_list[:3],1)

basin_IDs = find_basins(grid)

total = three_largest_basins(basin_IDs)

print(total)

            






