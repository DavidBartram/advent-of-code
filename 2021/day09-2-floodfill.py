import sys
from collections import defaultdict, Counter
from functools import reduce
import operator

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Since all the grid heights are between 0 and 9, 10 is a suitable default value
# When the grid dictionary is asked to look up coords beyond the grid, it will return 10
# this ensures that coords beyond the grid will result in a value higher than coords within the grid
grid = defaultdict(lambda: 10)

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
    #returns a list of coords of points adjacent to (i,j) in the grid
    coords_list = []
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
        
    for step in steps:
        (dx,dy) = step
        if grid[(i+dx,j+dy)] != 10: #default value is 10 if (i+dx,j_dy) is not already in grid
            coords_list.append((i+dx,j+dy))
        
    return coords_list

def find_low_points(grid):
    low_points = []
    for j, row in enumerate(data):
        for i, _ in enumerate(row):
            if grid[(i,j)] < min(neighbours(i,j,grid)):
                low_points.append((i,j))

    return low_points

def flood_fill_and_count(point,grid):
    #starting with a point (x,y) that is in a basin (e.g. the low point)
    #count all the points in that basin
    #note that every basin is entirely surrounded by points with height 9

    count = 0

    if grid[point] == 9:
        #stop if you've reached the edge of the basin
        #or a point that's already been counted (see below)
        return count
        
    else:
        count += 1 #count this point
        grid[point] = 9 #flood fill with 9s, prevents counting this point again

        #recursively count the neighbouring points
        for nb in neighbour_coords(point[0], point[1], grid):
            count += flood_fill_and_count(nb,grid)
    
    return count

def find_basin_sizes(low_points, grid):
    basin_sizes = []
    for lp in low_points:
        basin_sizes.append(flood_fill_and_count(lp,grid))

    return basin_sizes

def solve_puzzle(grid):
    lps = find_low_points(grid)

    basin_sizes = find_basin_sizes(lps, grid)

    return reduce(operator.mul,sorted(basin_sizes, reverse=True)[:3],1)

print(solve_puzzle(grid))








