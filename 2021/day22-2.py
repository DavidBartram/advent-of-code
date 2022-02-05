import sys
import intervals as I
import re

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

def new_cuboid(poscuboids,negcuboids,newcuboid, onoff):

    newpos = []
    newneg = []

    if onoff == 'on':
        newpos += [newcuboid]

    for poscuboid in poscuboids:
        overlap = intersect(newcuboid,poscuboid)
        if overlap:
            newneg += [overlap]
        
    for negcuboid in negcuboids:
        overlap = intersect(newcuboid,negcuboid)
        if overlap:
            newpos += [overlap]

    return poscuboids+newpos, negcuboids+newneg

def apply_instructions(instructions):
    poscuboids = []
    negcuboids = []

    for instruction in instructions:
        onoff = instruction[0]
        newcuboid = instruction[1]
        poscuboids, negcuboids = new_cuboid(poscuboids,negcuboids,newcuboid,onoff)
    
    posvol = sum([volume(x) for x in poscuboids])
    negvol = sum([volume(x) for x in negcuboids])

    return posvol-negvol

instructions = initialise()

final_vol = apply_instructions(instructions)

print(final_vol)


