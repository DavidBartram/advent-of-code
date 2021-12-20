from itertools import permutations, product
import sys

def initialise():

    with open(sys.argv[1]) as file:
        data = file.readlines()

    scanners = []
    scanner = []

    for line in data:
        if ',' in line:
            beacon = tuple([int(x) for x in line.strip().split(',')])
            scanner.append(beacon)
        
        elif line == '\n':
            scanners.append(scanner)
            scanner = []

    scanners.append(scanner)

    return scanners

scanners = initialise()


def rotations(point):

    (x,y,z) = point

    perm = permutations(point)

    rots = []

    for coord in perm:
        (x,y,z) = coord
        
        rots += [(x,y,z), (-x,-y,z), (x,-y,-z),(-x,y,-z)]

    return rots

def do_beacons_match(beacon1a, beacon2a,beacon1b,beacon2b):
    (x1a,y1a,z1a) = beacon1a
    (x2a,y2a,z2a) = beacon2a
    (x1b,y1b,z1b) = beacon1b
    (x2b,y2b,z2b) = beacon2b

    if (abs(x2a-x1a), abs(y2a-y1a), abs(z2a-z1a)) == (abs(x2b-x1b), abs(y2b-y1b), abs(z2b-z1b)):
        return True
    
    else:
        return False

def matched_beacons(scannerA,scannerB):
    A_matches = set()
    B_matches = set()
    possible_offsets = set()
    for beacon1a in scannerA:
        for beacon2a in scannerA:
            if beacon1a == beacon2a:
                continue
        for beacon1b in scannerB:
            for beacon2b in scannerB:
                if beacon1b == beacon2b:
                    continue
                #print(beacon1a, beacon2a, beacon1b, beacon2b)
                #print(do_beacons_match(beacon1a, beacon2a, beacon1b, beacon2b))
                if do_beacons_match(beacon1a, beacon2a, beacon1b, beacon2b):
                    A_matches = A_matches | {beacon1a,beacon2a}
                    B_matches = B_matches | {beacon1b,beacon2b}
                    
                    for rot1b in rotations(beacon1b):
                        for rot2b in rotations(beacon2b):
                            possible_offsets = possible_offsets | {tuple(p-q for p,q in zip(beacon1a,rot1b))}
                            possible_offsets = possible_offsets | {tuple(p-q for p,q in zip(beacon1a,rot2b))}
                    
    
    return A_matches, B_matches, possible_offsets

def find_correct_offset(matchesA, matchesB, possible_offsets):
    megamatchA = []
    for i in range(24):
        coords = set()
        for beacon in matchesA:
            coords = coords | {beacon}
        megamatchA.append(coords)

    for offset in possible_offsets:
        for i in range(24):
            coords = set()
            for beacon in matchesB:
                coords = coords | {tuple(p+q for p,q, in zip(rotations(beacon)[i], offset))}
            
            if coords in megamatchA:
                return offset, i


def reorient_scanner(scanner, offset, i):
    new_scanner = []
    for beacon in scanner:
        (x,y,z) = rotations(beacon)[i]
        (dx,dy,dz) = offset
        new_scanner.append((x+dx,y+dy,z+dz))
    
    return new_scanner

        

a = scanners[0]
b = scanners[1]

#print(A)
#print(B)

matchesA, matchesB, possible_offsets = matched_beacons(a,b)

offset, orientation = find_correct_offset(matchesA, matchesB, possible_offsets)

a = scanners[4]
b = reorient_scanner(b, offset, orientation)

matchesA, matchesB, possible_offsets = matched_beacons(a,b)

print(matched_beacons(a,b))

offset, orientation = find_correct_offset(matchesA, matchesB, possible_offsets)

print(offset, orientation)


