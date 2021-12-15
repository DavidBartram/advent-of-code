import sys
from collections import defaultdict
from queue import PriorityQueue
import math

with open(sys.argv[1]) as file:
    data = file.read().splitlines()


def initialise(data):
    grid = {}

    for j, row in enumerate(data):
        for i, item in enumerate(row):
            grid[(i,j)] = int(item)

    visit = PriorityQueue()
    visit.put((0,(0,0)))

    distance = defaultdict(lambda: math.inf)

    distance[(0,0)] = 0

    target = (len(data[0])-1, len(data)-1)

    return grid,visit,distance, target

def neighbour_coords(point,grid):
#returns a list of coords of points adjacent to (i,j) in the grid
    coords_list = []
    steps = [(1,0),(-1,0),(0,1),(0,-1)]
        
    for step in steps:
        (i,j) = point
        (dx,dy) = step
        if grid.get((i+dx,j+dy)):
            coords_list.append((i+dx,j+dy))
        
    return coords_list

def dijkstra(grid,visit,distance,target):

    while not visit.empty():
        (d,(x,y)) = visit.get()

        for nb in neighbour_coords((x,y), grid):
            if d + grid[nb] < distance[nb]:
                distance[nb] = d + grid[nb]
                visit.put((distance[nb], nb))
    
    return distance[target]

        


grid,visit,distance, target = initialise(data)

print(dijkstra(grid,visit,distance,target))








