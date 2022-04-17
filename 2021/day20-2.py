import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.readlines()

algo = data[0].strip().replace('.','0').replace('#','1') #algorithm string
image = [line.strip().replace('.','0').replace('#','1') for line in data[2:]] #image grid as list of strings

def update(point, image, algo, oob):
    #calculate the new value of a pixel based on its neighbours
    #and the algorithm

    xmax = len(image[0])-1
    ymax = len(image)-1

    (x,y) = point
    steps = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0),(1,0),(-1,1),(0,1),(1,1)]

    idx = ''

    for step in steps:
        (dx,dy) = step
        
        if 0 <= x+dx <= xmax and 0 <= y+dy <= ymax:
            #if in the bounds of the grid, return the value
            idx += image[y+dy][x+dx]
        
        else:
            #if out of bounds, return current value of oob
            idx += oob
    
    idx = int(idx,2)

    return algo[idx]


def apply_algo(image,algo, oob):
    #apply the enhancement algorithm once to the image grid
    #return the new image grid
    
    image2 = []

    xmax = len(image[0])-1
    ymax = len(image)-1

    for y in range(-1,ymax+2):
            new_row = ''
            for x in range(-1,xmax+2):
                new_row += update((x,y), image, algo, oob)

            image2.append(new_row)
    
    return image2

def print_image(image):
    #helper function to print image
    #only used for debugging
    for row in image:
        print(row)

def part_one(image,algo,n):
    #apply the enhancement algorithm n times to the initial image grid

    oob = '0'

    for _ in range(n):
        #apply the enhancement algorithm
        image = apply_algo(image,algo,oob)

        #update the value of oob
        if algo[0]=='1' and algo[-1]=='0' and oob == '0':
            oob = '1'
        elif algo[0]=='1' and algo[-1]=='0' and oob == '1':
            oob = '0'

    count = 0

    for row in image:
        for x in row:
            count += int(x)

    return count, image

pix_sum, img = part_one(image,algo,50)
print(pix_sum)
