import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

end_points = []

#Process each line to produce a list of lists of endpoints
#e.g. end_points = [ [(3,2),(4,2)], [(1,1), (5,5)], ....]

for line in data:
    coords = line.replace(' -> ', ',').split(',')
    end_points.append([(int(coords[0]),int(coords[1])),(int(coords[2]),int(coords[3]))])

#dictionary from coordinate tuples (x,y) to number of overlapping lines at that point
overlap_count = defaultdict(lambda: 0)

dx,dy = 0,0

for pair in end_points:
    start = pair[0]
    end = pair[1]

    #vertical lines need special treatment as their gradient is undefined
    if start[0] == end[0]:

        #for convenience the point with lower y-value will be used as the start
        if start[1] > end[1]:
            start,end = end,start
        
        
        dx,dy = 0,1
        #an integer step along a vertical line adds +0 to x and +1 to y

    #horizontal and diagonal lines
    else:
        #for convenience the point with lower x-value will be used as the start
        if start[0] > end[0]:
            start,end = end,start
        
        dx = 1
        dy = int((end[1]-start[1])/(end[0]-start[0])) #gradient

        #an integer step along the line adds +1 to x and +(gradient) to y
    
    overlap_count[start] += 1
    (x,y) = start

    #keep taking integer steps along the line
    #until we reach the end point
    while (x,y) != end:
        x,y = x+dx,y+dy
        overlap_count[(x,y)] +=1 #increment the count of lines crossing that point


count = sum([value>1 for value in overlap_count.values()])

print(count)


