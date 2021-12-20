import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.readlines()

algo = data[0].strip().replace('.','0').replace('#','1')
image = [line.strip().replace('.','0').replace('#','1') for line in data[2:]]

def update(point, image, algo, oob):

    xmax = len(image[0])-1
    ymax = len(image)-1

    (x,y) = point
    steps = [(-1,-1), (0,-1), (1,-1), (-1,0), (0,0),(1,0),(-1,1),(0,1),(1,1)]

    idx = ''

    for step in steps:
        (dx,dy) = step
        
        if 0 <= x+dx <= xmax and 0 <= y+dy <= ymax:
            idx += image[y+dy][x+dx]
        
        else:
            idx += oob
    
    idx = int(idx,2)

    return algo[idx]


def apply_algo(image,algo, oob):
    
    image2 = []

    xmax = len(image[0])-1
    ymax = len(image)-1

    for y in range(-1,ymax+2):
            new_row = ''
            for x in range(-1,xmax+2):
                new_row += update((x,y), image, algo, oob)

            image2.append(new_row)
    
    return image2

    
    

    
    
    return image2

def print_image(image):
    for row in image:
        print(row)

def part_one(image,algo,n):

    oob = '0'

    for _ in range(n):
        image = apply_algo(image,algo,oob)
        if algo[0]=='1' and algo[-1]=='0' and oob == '0':
            oob = '1'
        elif algo[0]=='1' and algo[-1]=='0' and oob == '1':
            oob = '0'

    count = 0

    for row in image:
        for x in row:
            count += int(x)

    return count, image

pix_sum, img = part_one(image,algo,2)
print(pix_sum)
#print_image(img)
