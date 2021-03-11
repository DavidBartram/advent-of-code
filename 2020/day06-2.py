import sys

with open(sys.argv[1]) as file:
    groups = file.read().split('\n\n')

output = []

for group in groups:
    x = set(group)
    for line in group.split('\n'):
        x = x.intersection(set(line))
    
    output.append(len(x))
        
print(sum(output))
