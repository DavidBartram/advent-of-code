import sys
from collections import defaultdict

def parse_line(string):
    #parse a single line of commands from the input
    cmds = []

    while string:
        if string[0] in {'e','w'}:
            cmds.append(string[0])
            string = string[1:]
        
        if string[0] in {'n','s'}:
            #north and south don't exist on this hex grid, only ne,nw,se,sw
            #so take two characters
            cmds.append(string[0:2])
            string = string[2:]
        
        if string[0] in {'\n'}:
            #ignore line break character
            string = string[1:]
    
    return cmds

#Use the "cube coordinates" system from https://www.redblobgames.com/grids/hexagons/

def shift(coords, dir):
    #shift the given coordinates one hex in the direction specified
    (x,y,z) = coords
    if dir == 'ne':
        coords = (x+1, y, z-1)
    if dir == 'e':
        coords = (x+1, y-1, z)
    if dir == 'se':
        coords = (x, y-1, z+1)
    if dir == 'sw':
        coords = (x-1, y, z+1)
    if dir == 'w':
        coords = (x-1, y+1, z)
    if dir == 'nw':
        coords = (x, y+1, z-1)
    
    return coords

def initialise():
    #initialise the hex grid
    #the grid is represented by a defaultdict
    #key = tuple of coordinates
    #value = 0 for a white tile, 1 for a black tile
    grid = defaultdict(int)

    #parse the input file
    with open(sys.argv[1]) as file:
        lines = file.readlines()

    lines_cmds = [parse_line(line) for line in lines]

    #flip tiles according to the input
    for line in lines_cmds:
        coords = (0,0,0)
        for cmd in line:
            coords = shift(coords, cmd)

        if grid[coords] == 0:
            grid[coords] = 1

        else:
            grid[coords] = 0
    
    return grid

def count_black(grid):
    #count the black tiles in a grid
    count=0
    for val in grid.values():
        if val == 1:
            count += 1
    return count

def create_nb_grid(grid):
    #create a new defaultdict
    #key = tuple of coordinates
    #value = number of neighbouring tiles which are black

    nb_grid = defaultdict(int)
    for coords, val in grid.items():
        if val == 1:
            #every black tile increases the count of black tiles
            #for its neighbours by one
            for cmd in {'ne','e','se','sw','w','nw'}:
                nb_grid[shift(coords,cmd)] += 1
    
    return nb_grid
            
def advance(grid):
    #advance the grid one generation according to the rules

    #create the grid showing how many black tiles neighbour each tile
    nb_grid = create_nb_grid(grid)
    
    #initialise new grid
    new_grid = defaultdict(int)

    #apply the rules to determine the new state of each hex tile
    for coords in nb_grid:
        if grid[coords] == 1:
            if nb_grid[coords]==0 or nb_grid[coords] > 2:
                new_grid[coords] = 0
            else:
                new_grid[coords] = 1
        
        if grid[coords] ==0:
            if nb_grid[coords]==2:
                new_grid[coords] = 1
            else:
                new_grid[coords] = 0
    
    return new_grid


#Part 1
grid = initialise()
print(count_black(grid))

#Part 2
n = 100

for _ in range(n):
    grid = advance(grid)

print(count_black(grid))
