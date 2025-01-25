import os
from collections import defaultdict


def read_input_file(file_path):

    connections = defaultdict(set)

    with open(file_path, "r") as file:
        input = file.readlines()

    for line in input:
        p1, p2 = line.strip().split("-")
        connections[p1].add(p2)
        connections[p2].add(p1)

    return connections


def get_cliques(connections):
    # get the cliques (complete subgraphs) in the graph#

    # cliques is a set of frozensets (which are hashable)
    # being a set, we will only store unique cliques
    cliques = set()

    # the stack contains points to be processed
    # for each point, a known clique containing the point is also provided
    # the stack is initialized with each point and a clique containing only that point
    stack = [(point, frozenset({point})) for point in connections]
    while stack:
        point, known_clique = stack.pop()

        # consider each point connected to the current point but not in the known clique
        for point2 in connections[point].difference(known_clique):
            # clique.union(point2) is a potential new clique
            # it's only a new clique if point2 is connected to all the points in the known clique
            if connections[point2].issuperset(known_clique):
                clique2 = known_clique.union({point2})
                if clique2 not in cliques:
                    cliques.add(clique2)
                    # at some point we'll need to consider point2 and clique2, to see if
                    # the clique can be extended further
                    stack.append((point2, clique2))

    return cliques


def main():
    repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
    file_path = os.path.join(repo_root, "2024/input/input23-1")
    connections = read_input_file(file_path)

    cliques = get_cliques(connections)

    count = 0

    for clique in cliques:
        if len(clique) == 3 and any(point.startswith("t") for point in clique):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
