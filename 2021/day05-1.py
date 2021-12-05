import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

end_points = []

for line in data:
    coords = line.replace(' -> ', ',').split(',')
    end_points.append([(int(coords[0]),int(coords[1])),(int(coords[2]),int(coords[3]))])

overlap_count = defaultdict(lambda: 0)

for pair in end_points:

    start = pair[0]
    end = pair[1]

    if start[0] == end[0]:

        if start[1] > end[1]:
            start,end = end,start

        for k in range(start[1],end[1]+1):
            overlap_count[(start[0],k)] +=1
    
    elif start[1] == end[1]:

        if start[0] > end[0]:
            start,end = end,start

        for k in range(start[0],end[0]+1):
            overlap_count[(k,start[1])] +=1

    else:
        pass

count =0 
for value in overlap_count.values():
    if value>1:
        count += 1

print(count)
