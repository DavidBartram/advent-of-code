import sys
from collections import defaultdict
import re

def initialise():
    with open(sys.argv[1]) as file:
        data = file.readlines()

    cuboids = []

    for line in data:
        op = line.split(' ')[0]
        ranges = ''.join(line.split(' ')[1:])
        values = [int(x) for x in re.findall(r'-{0,1}\d{1,10}', ranges)]
        cuboids.append((op, tuple(values)))

    return cuboids



def apply_cuboids_to_point(coords, cuboids):
    x,y,z = coords

    result = False

    for cuboid in cuboids:
        op = cuboid[0]
        xmin, xmax, ymin, ymax, zmin, zmax = cuboid[1]

        if xmin <= x <= xmax and ymin <= y <= ymax and zmin <= z <= zmax:
            if op == 'on':
                result = True
            else:
                result = False
    
    return result

def iterate_over_points(cuboids):
    count=0
    
    bigcube = range(-50,51)

    for x in bigcube:
        for y in bigcube:
            for z in bigcube:
                if apply_cuboids_to_point((x,y,z), cuboids):
                    count += 1

    return count

cuboids = initialise()

print(cuboids)

answer = iterate_over_points(cuboids)

print(answer)


