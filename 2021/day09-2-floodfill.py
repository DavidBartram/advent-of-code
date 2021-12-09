import sys
from collections import defaultdict, Counter
from functools import reduce
import operator

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

# Since all the grid heights are between 0 and 9, 10 is a suitable default value
# When the grid dictionary is asked to look up coords beyond the grid, it will return 10
# this ensures that coords beyond the grid will result in a value lower than coords within the grid
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

def flood_fill(point,grid,k):
    #starting with a point (x,y) that is in a basin
    #replace all height values in the same basin with k
    #note that every basin is entirely surrounded by points with height 9

    if grid[point] == 9:
        #stop if you've reached the edge of the basin
        return
    
    elif grid[point] == k:
        return
    
    else:
        grid[point] = k

        #recursively fill the neighbouring points
        for nb in neighbour_coords(point[0], point[1], grid):
            flood_fill(nb,grid,k)

def three_largest_basins(grid):
    #we should only count points that are labelled as part of a basin
    #make sure we don't count high points grid[high point] == 9
    #also make sure we don't count points outside the grid grid[outside point] == 10
    counts = Counter([x for x in grid.values() if x>10])

    counts_list = sorted(list(counts.values()), reverse=True)

    return reduce(operator.mul,counts_list[:3],1)

lps = find_low_points(grid)

#replace all heights of basin points with a distinct label for the basin
#use i+20 as the basin label, to ensure it is distinct from all original height values and the default value 10
for i, lp in enumerate(lps):
    flood_fill(lp,grid,(i+20))

print(three_largest_basins(grid))








