from itertools import permutations
import sys

def initialise():
    #read the input file and set up
    #scanners is a set of sets of beacon coordinates
    #perms is the set of permutations of the indices (0,1,2)

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

    scanners = [set(scanner) for scanner in scanners]

    perms = set(permutations((0,1,2)))

    return scanners, perms

def parity(perms):
    #returns a dictionary from permutations of (0,1,2) to the set of signatures (axis inversion) such that the total operation is parity preserving
    #for example, since the permutation (1,0,2) is odd, we must choose the odd signatures (-1,1,1), (1,-1,1),(1,1,-1) and (-1,-1,-1)}
    # so correct_sigs[(1,0,2)] == {(-1,1,1), (1,-1,1),(1,1,-1),(-1,-1,-1)}

    correct_sigs = {}

    for perm in perms:
        parity = sum(1 for (x,px) in enumerate(perm) for (y,py) in enumerate(perm) if x<y and px>py)%2  #calculate parity of the permutation


        if parity == 0:
            correct_sigs[perm] = {(1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)}

        if parity == 1:
            correct_sigs[perm] = {(-1,1,1), (1,-1,1),(1,1,-1),(-1,-1,-1)}
    
    return correct_sigs

scanners, perms = initialise()

correct_sigs = parity(perms)

def reorient(scanner,perm,sig):
    #reorients a scanner using a particular permutation and signature
    #returns the reoriented scanner (a new set of beacon coordinates)
    newscanner = set()

    for beacon in scanner:
        newbeacon = (beacon[perm[0]]*sig[0], beacon[perm[1]]*sig[1], beacon[perm[2]]*sig[2])
        newscanner.add(newbeacon)

    return newscanner

def translate(scanner,offset):
    #translates a scanner by a particular offset, where the offset is a tuple (dx,dy,dz) representing the translation vector
    #returns the reoriented scanner (a new set of beacon coordinates)
    newscanner = set()
    dx,dy,dz = offset

    for beacon in scanner:
        x,y,z = beacon
        newbeacon = (x+dx,y+dy,z+dz)
        newscanner.add(newbeacon)

    return newscanner

def match12(scannerA, scannerB):
    #Returns True if scannerA and scannerB have 12 or more beacon coordinates in common
    #otherwise returns False
    common_points = scannerA.intersection(scannerB)

    if len(common_points) >= 12:
        return True
    
    return False

def compare(scannerA,scannerB):
    #brute force to determine if two scanners match
    #check every parity preserving orientation of scanner B (permutation + signature)
    #and every translation (offset) of scanner B that brings a beacon from scanner B into alignment with a beacon from scanner A
    #if a match is found, return the offset, permutation and signature that matches the two scanners
    #return None if no match is found
    for perm in perms:
        for sig in correct_sigs[perm]:
            rotB = reorient(scannerB,perm,sig)
            for beaconA in scannerA:
                for beaconB in rotB:
                    xa,ya,za = beaconA
                    xb,yb,zb = beaconB
                    offset = (xa-xb,ya-yb,za-zb)
                    transB = translate(rotB,offset)
                    
                    if match12(scannerA,transB):
                        return offset, perm, sig

                    offset = (xb-xa,yb-ya,zb-za)
                    transB = translate(rotB,offset)

                    if match12(scannerA,transB):
                        return offset, perm, sig



def part_two(scanners):

    #the "base scanner" is a set of coordinates of beacons from the point of view of scanner 0
    #when a new scanner is correctly aligned and translated, its beacons are added to the "base scanner" set
    base_scanner = scanners[0]
    #a list of scanners which have been incorporated into the "base scanner"
    visited = [0]
    #list of the offsets (translation vectors) of the other scanners from scanner 0's position
    offsets = []

    while len(visited) < len(scanners):
        for i,scanner in enumerate(scanners):
                if i in visited:
                    continue

                result = compare(base_scanner, scanner)
            
                if result:
                    offset, perm, sig = result
                    offsets.append(offset)
                    #reorient and translate the scanner into scanner 0's coordinate system
                    new_scanner = reorient(scanner,perm,sig)
                    new_scanner = translate(new_scanner,offset)
                    visited.append(i)
                    print(len(visited))
                    base_scanner = base_scanner | new_scanner #incorporate the scanner's beacons into the base scanner
    
    #calculate the manhattan distance between every pair of scanners
    #return the maximum manhattan distance (the puzzle solution)
    manhattans = []
    for off1 in offsets:
        for off2 in offsets:
            x1,y1,z1 = off1
            x2,y2,z2 = off2
            manhattans.append(abs(x2-x1) + abs(y2-y1) + abs(z2-z1))
                
    return max(manhattans)

print(part_two(scanners))


