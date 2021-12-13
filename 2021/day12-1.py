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
    newpath = path[:] + [node] #create a new copy of the path each time the function is called and append the current node

    if node == target:
        paths.append(newpath[:])

    else:
        for neighbour in graph[node]:
            if not (neighbour in newpath and neighbour.islower()):
                dfs(graph,neighbour,target,newpath, paths)

    return paths

print(len(dfs(graph,'start','end',[],[])))


