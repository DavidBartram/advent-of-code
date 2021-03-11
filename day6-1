import sys

with open(sys.argv[1]) as file:
    groups = file.read().split('\n\n')

groups = [group.replace('\n','') for group in groups]

groups = [set(group) for group in groups]

counts = [len(group) for group in groups]

print(sum(counts))
