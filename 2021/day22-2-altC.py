import sys
import intervals as I
import re
from collections import defaultdict
from statistics import median

def initialise():
    #read the input file
    #output instructions, a list of tuples (op, (ix,iy,iz))
    #op is either 'on' or 'off', representing the operation for that instruction
    #ix, iy, iz are intervals defining the cuboid for that instruction

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
    #calculate the number of cubes contained in a cuboid
    #cubes on the boundary of a cuboid count as contained within that cuboid

    ix, iy, iz = cuboid

    a = ix.upper - ix.lower + 1
    b = iy.upper - iy.lower + 1
    c = iz.upper - iz.lower + 1

    return a*b*c


def intersect(cuboid1,cuboid2):
    #calculate the cuboid of intersection between two cuboids
    #return the cuboid of intersection, or False if the input cuboids do not intersect

    ix1,iy1,iz1 = cuboid1
    ix2, iy2, iz2 = cuboid2

    ix = ix1 & ix2 #interval intersection
    iy = iy1 & iy2
    iz = iz1 & iz2

    if ix.is_empty() or iy.is_empty() or iz.is_empty():
        return False
    
    return (ix,iy,iz)

def apply_one_instruction(cuboids,newcuboid, onoff):
    #apply a single instruction

    new = cuboids.copy()

    if onoff == 'on':
        new[newcuboid] = 1

    for cuboid, sign in cuboids.items():
        overlap = intersect(newcuboid,cuboid)
        if overlap:
            new[overlap] -= sign

    return new

def apply_instructions(instructions):
    #apply all the instructions in the input file
    #return the total number of 'on' cubes after all instructions are applied
    cuboids = defaultdict(lambda: 0)

    for instruction in instructions:
        onoff = instruction[0]
        newcuboid = instruction[1]
        cuboids = apply_one_instruction(cuboids,newcuboid,onoff)
    
    total = 0

    for cuboid, sign in cuboids.items():
        total += sign*volume(cuboid)


    return total

instructions = initialise()

print(apply_instructions(instructions))


