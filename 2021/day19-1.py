from itertools import permutations
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

    scanners = [set(scanner) for scanner in scanners]

    perms = set(permutations((0,1,2)))

    #odd_sigs = {(-1,1,1), (1,-1,1),(1,1,-1),(-1,-1,-1)}

    #even_sigs = {(1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)}

    return scanners, perms

scanners, perms = initialise()

def parity(perm):
    parity = sum(1 for (x,px) in enumerate(perm) for (y,py) in enumerate(perm) if x<y and px>py)%2

    if parity == 0:
        return {(1,1,1), (-1,-1,1), (-1,1,-1), (1,-1,-1)}

    if parity == 1:
        return {(-1,1,1), (1,-1,1),(1,1,-1),(-1,-1,-1)}

def reorient(scanner,perm,sig):
    newscanner = set()

    for beacon in scanner:
        newbeacon = (beacon[perm[0]]*sig[0], beacon[perm[1]]*sig[1], beacon[perm[2]]*sig[2])
        newscanner.add(newbeacon)

    return newscanner

def translate(scanner,offset):
    newscanner = set()
    dx,dy,dz = offset

    for beacon in scanner:
        x,y,z = beacon
        newbeacon = (x+dx,y+dy,z+dz)
        newscanner.add(newbeacon)

    return newscanner

def match12(scannerA, scannerB):
    common_points = scannerA.intersection(scannerB)

    if len(common_points) >= 12:
        return True
    
    return False

def compare(scannerA,scannerB):
    for perm in perms:
        for sig in parity(perm):
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



def part_one(scanners):

    visited = [0]
    base_scanner = scanners[0]

    while len(visited) < len(scanners):
        for i,scanner in enumerate(scanners):
                if i in visited:
                    continue

                #print('checking', i)

                result = compare(base_scanner, scanner)
            
                if result:
                    print('match!')
                    print(i,result)
                    offset, perm, sig = result
                    new_scanner = reorient(scanner,perm,sig)
                    new_scanner = translate(new_scanner,offset)
                    visited.append(i)
                    base_scanner = base_scanner | new_scanner
                    #print(len(base_scanner))
                
    return len(base_scanner)

print(part_one(scanners))


