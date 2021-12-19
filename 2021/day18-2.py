from math import ceil, floor
import sys
from functools import reduce
from itertools import permutations

def read(snail_string): #assume no values above 9 in input
    snail = []
    depth = 0

    for char in snail_string:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char != ',':
            snail.append((int(char),depth))

    return snail

def explode(snail):

    newsnail = snail[:]

    for i, (val,depth) in enumerate(snail):
        if depth==5:
            if i-1>=0:
                newsnail[i-1] = (snail[i-1][0]+val,snail[i-1][1])
            if i+2<=len(snail)-1:
                newsnail[i+2] = (snail[i+2][0]+snail[i+1][0],snail[i+2][1])
            
            newsnail.pop(i+1)

            newsnail[i] = (0,depth-1)
    
            return newsnail
    
    return False

def split(snail):
    newsnail = snail[:]

    for i, (val,depth) in enumerate(snail):
        if val > 9:
            leftval = int(floor(val/2))
            rightval = int(ceil(val/2))
            newsnail[i] = (leftval,depth+1)
            newsnail.insert(i+1, (rightval,depth+1) )
            return newsnail
    
    return False

def add(snail1, snail2):
    snail1.extend(snail2)
    

    snail1 = [(val,depth+1) for (val,depth) in snail1]

    return snail1

def snail_reduce(snail):
    while explode(snail) or split(snail):
        ex = explode(snail)
        spl = split(snail)

        if ex:
            snail = ex

        elif spl:
            snail = spl
        
    return snail

def add_and_snail_reduce(snail1,snail2):

    res = add(snail1,snail2)

    res = snail_reduce(res)

    return res

def magnitude(snail):

    if len(snail) == 2:
        return 3*snail[0][0] + 2*snail[1][0]

    max_depth = max([d for _,d in snail])

    i = 0

    while i <= len(snail)-1:
        #print('max_depth',max_depth)
        #print('i',i)
        #print(snail)
        if snail[i][1]==max_depth:
            if i+1 <= len(snail) - 1:
                snail[i] = (3*snail[i][0] + 2*snail[i+1][0],max_depth-1)
                snail.pop(i+1)
            else: snail[i] = (snail[i][0],max_depth-1)
            i += 1
        else:
            i +=1 

    return magnitude(snail)

#snail1 = read('[[[[4,3],4],4],[7,[[8,4],9]]]')

#snail2 = read('[1,1]')

#snail = add_and_snail_reduce(snail1,snail2)

#snail1 = read('[[[[4,3],4],4],[7,[[8,4],9]]]')

#snail2 = read('[1,1]')

#snail = add_and_snail_reduce(snail1,snail2)

#print(snail)

with open(sys.argv[1]) as file:
    snails = [read(line.strip()) for line in file]


#print(magnitude(reduce(add_and_snail_reduce, snails)))


def part_two(snails):
    max_mag = 0
    for i in range(len(snails)):
        for j in range(len(snails)):
            print(i,j)
            if i==j:
                continue
            else:
                res = magnitude(add_and_snail_reduce(snails[i],snails[j]))
                if res > max_mag:
                    max_mag = res
                res = magnitude(add_and_snail_reduce(snails[j],snails[i]))
                if res > max_mag:
                    max_mag = res
                print(max_mag)

    return max_mag

#snail = read('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')

print(part_two(snails))
    

