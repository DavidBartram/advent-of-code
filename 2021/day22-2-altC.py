import sys
import intervals as I
import re
from collections import defaultdict
from statistics import median

def initialise():
    with open(sys.argv[1]) as file:
        data = file.readlines()

    instructions = []

    for line in data:
        op = line.split(' ')[0]
        ranges = ''.join(line.split(' ')[1:])
        values = [int(x) for x in re.findall(r'-{0,1}\d{1,10}', ranges)]
        ix = I.closed(values[0],values[1])
        iy = I.closed(values[2],values[3])
        iz = I.closed(values[4],values[5])
        instructions.append((op,(ix,iy,iz)))

    return instructions

def volume(cuboid):
    ix, iy, iz = cuboid

    a = ix.upper - ix.lower + 1
    b = iy.upper - iy.lower + 1
    c = iz.upper - iz.lower + 1

    return a*b*c


def intersect(cuboid1,cuboid2):
    ix1,iy1,iz1 = cuboid1
    ix2, iy2, iz2 = cuboid2

    ix = ix1 & ix2
    iy = iy1 & iy2
    iz = iz1 & iz2

    if ix.is_empty() or iy.is_empty() or iz.is_empty():
        return False
    
    return (ix,iy,iz)

def new_cuboid(cuboids,newcuboid, onoff):

    new = cuboids.copy()

    if onoff == 'on':
        new[newcuboid] += 1

    for cuboid, count in cuboids.items():
        overlap = intersect(newcuboid,cuboid)
        if overlap:
            new[overlap] -= count

    return new

def apply_instructions(instructions):
    cuboids = defaultdict(lambda: 0)

    i=0

    for instruction in instructions:
        i += 1
        if i%50 == 0:
            print(i, len(cuboids), min(cuboids.values()), max(cuboids.values()), sum(cuboids.values())/len(cuboids))
        onoff = instruction[0]
        newcuboid = instruction[1]
        cuboids = new_cuboid(cuboids,newcuboid,onoff)
    
    total = 0

    for cuboid, count in cuboids.items():
        total += count*volume(cuboid)


    return total

instructions = initialise()

print(apply_instructions(instructions))


