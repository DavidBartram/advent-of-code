import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

graph = defaultdict(lambda: [])

for line in data:
    line = line.split('-')
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])


def dfs(graph, node, target, path, paths, revisits):
    
    if node in path and node.islower():
        revisits = False
    
    path.append(node)

    if node == target:
        paths.append(path[:])

    else:
        for neighbour in graph[node]:

            if revisits == True:
                valid_neighbour = not (neighbour == 'start')
            else:
                valid_neighbour = not (neighbour in path and neighbour.islower())

            if valid_neighbour:
                dfs(graph,neighbour,target,path, paths, revisits)

    path.pop() #backtrack if target reached or no neighbours are valid

    return paths

print(len(dfs(graph,'start','end',[],[], True)))


