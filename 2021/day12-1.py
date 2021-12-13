import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

graph = defaultdict(lambda: [])

for line in data:
    line = line.split('-')
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])


def dfs(graph, node, target, path, paths):
    path.append(node)

    if node == target:
        paths.append(path[:]) #append a copy of the current path, not a pointer to the path variable which keeps changing

    else:
        for neighbour in graph[node]:
            if not (neighbour in path and neighbour.islower()):
                dfs(graph,neighbour,target,path, paths)

    #we are using the same path variable for all the recursive calls
    #when a function call completes, we want to leave path the way we found it
    #so remove the node we appended above
    path.pop()

    return paths

print(len(dfs(graph,'start','end',[],[])))


