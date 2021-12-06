import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

end_points = []

for line in data:
    coords = line.replace(' -> ', ',').split(',')
    end_points.append([(int(coords[0]),int(coords[1])),(int(coords[2]),int(coords[3]))])

overlap_count = defaultdict(lambda: 0)

dx,dy = 0,0

for pair in end_points:
    start = pair[0]
    end = pair[1]

    if start[0] == end[0]:

        if start[1] > end[1]:
            start,end = end,start
        
        dx,dy = 0,1

    elif start[1] == end[1]:

        if start[0] > end[0]:
            start,end = end,start
        
        dx,dy = 1,0

    else:
        if start[0] > end[0]:
            start,end = end,start
        
        dx = 1
        dy = int((end[1]-start[1])/(end[0]-start[0]))
    
    overlap_count[start] += 1
    (x,y) = start

    while (x,y) != end:
        x,y = x+dx,y+dy
        overlap_count[(x,y)] +=1

count =0 
for value in overlap_count.values():
    if value>1:
        count += 1

print(count)


