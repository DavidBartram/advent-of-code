from math import ceil, floor
import sys
from functools import reduce

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

    while i <= len(snail)-2:
        #print('max_depth',max_depth)
        #print('i',i)
        #print(snail)
        if snail[i][1]==max_depth:
            snail[i] = (3*snail[i][0] + 2*snail[i+1][0],max_depth-1)
            snail.pop(i+1)
            i += 1
        else:
            i +=1 

    return magnitude(snail)

#snail1 = read('[[[[4,3],4],4],[7,[[8,4],9]]]')

#snail2 = read('[1,1]')

#snail = add_and_snail_reduce(snail1,snail2)

#snail1 = read('[[[5,[2,8]],4],[5,[[9,9],0]]]')

#snail2 = read('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')

#snail = add_and_snail_reduce(snail1,snail2)

#print('1st mag',magnitude(snail))

with open(sys.argv[1]) as file:
    raw = [line.strip() for line in file]
    snails = [read(line.strip()) for line in file]

#print(magnitude(reduce(add_and_snail_reduce, snails)))

#snail = read('[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]')

#print(magnitude(snail))
    
def part_two(raw):
    maglist =[]
    for i in range(len(raw)):
        for j in range(len(raw)):
            #print(i,j)
            snail1 = read(raw[i])

            snail2 = read(raw[j])

            snail = add_and_snail_reduce(snail1,snail2)

            maglist.append(magnitude(snail))

            snail1 = read(raw[j])

            snail2 = read(raw[i])

            snail = add_and_snail_reduce(snail1,snail2)

            maglist.append(magnitude(snail))

    return max(maglist)

            
print(part_two(raw))
