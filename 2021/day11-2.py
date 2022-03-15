import sys

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

#initialise a dict from tuples (i,j) to energy level of the point at coords (i,j)
grid = {}

for j, row in enumerate(data):
    for i, item in enumerate(row):
        grid[(i,j)] = int(item)

rows = len(data)
cols = len(data[0])

def neighbour_coords(i,j,grid):
    #returns a list of coords of points adjacent to (i,j) in the grid
    coords_list = []
    steps = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    
    for step in steps:
        (dx,dy) = step
        if 0 <= i+dx < cols and 0 <= j+dy < rows: 
            coords_list.append((i+dx,j+dy))
    
    return coords_list

def nb_dict(grid):
    #populates a dictionary from each point in the grid to a list of neighbouring points
    nbdict = {}

    for point in grid.copy():
        nbdict[point] = neighbour_coords(point[0],point[1],grid)
    
    return nbdict

def flash(point,grid,flashed_points,nbdict):
    #causes a point to flash, and recursively flashes any neighbours whose energy goes above 9

    flashed_points.append(point) #keep track of points which have already flashed

    nbs = nbdict[point]

    for nb in nbs:
        grid[nb] += 1
    
    for nb in nbs:
        if grid[nb]>9 and nb not in flashed_points: #only flash points that have not flashed this iteration
            grid, flashed_points = flash(nb, grid, flashed_points, nbdict)
    
    return grid,flashed_points

def advance_step(grid, nbdict, flash_sum):
    for point in grid:
        grid[point] += 1

    flashed_points = []

    for point in grid:
        if grid[point] > 9 and point not in flashed_points: #only flash points that have not flashed this iteration
            grid, flashed_points = flash(point,grid, flashed_points, nbdict)

    for point in flashed_points:
        grid[point] = 0   #reset points which have flashed to 0 energy

    flash_sum += len(flashed_points) #count flashed points
    
    return flash_sum

def advance_until_synched(grid):
    nbdict = nb_dict(grid)
    flash_sum = 0
    i=0

    while True:
        advance_step(grid, nbdict,flash_sum)
        i+=1

        if max(grid.values()) == 0: #when all points flash
            return i

print(advance_until_synched(grid))
