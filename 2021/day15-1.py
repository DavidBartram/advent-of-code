import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()


def initialise(data):
    grid = {}

    for j, row in enumerate(data):
        for i, item in enumerate(row):
            grid[(i,j)] = int(item)

    start = (0,0)
    unvisited = {start:(start,0)}
    visited = []
    distance = {start:0}
    target = (len(data[0])-1 , len(data[1])-1)

    return grid,distance,unvisited,visited,start,target

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

def dijkstra(grid,distance,unvisited,visited,node,target):

    if node in visited:
        pass

    if node == target:
        print(distance[target])
        return None

    for nb in neighbour_coords(node,grid):
        if nb not in visited:
            if (not distance.get(nb)) or (distance[node] + grid[nb] < distance.get(nb)):
                distance[nb] = distance[node] + grid[nb]
                unvisited[nb] = (nb,distance[node] + grid[nb])
    
    visited.append(node)
    unvisited.pop(node)

    unvisited = {k: v for k, v in sorted(unvisited.items(), key=lambda item: item[1][1])}

    return next(iter(unvisited))

        


grid,distance,unvisited,visited,start,target = initialise(data)

node = start

i = 0

go = True

while go:
    node = dijkstra(grid,distance,unvisited,visited,node,target)

    if not node:
        go = False

    i += 1
    if i%2000 == 0:
        print(i)








