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
        paths.append(path[:])

    else:
        for neighbour in graph[node]:
            if not (neighbour in path and neighbour.islower()):
                dfs(graph,neighbour,target,path, paths)

    path.pop() #backtrack if target reached or no neighbours are valid

    return paths

print(len(dfs(graph,'start','end',[],[])))


