import sys
import re
from collections import defaultdict
from itertools import combinations

#process the input
with open(sys.argv[1]) as file:
    tiles = file.read().split('\n\n')

tiles = [tile.replace('Tile ', '').replace(':','').split('\n') for tile in tiles]

tiles = {int(tile[0]):tile[1:] for tile in tiles}

for tile in tiles.values():
        try:
            tile.remove('')
        except ValueError:
            pass


#helper functions for flipping and rotating tiles
def flipV(tile):
    #flip tile vertically
    newtile = list(reversed(tile))

    return newtile

def flipH(tile):
    #flip tile horizontally
    newtile = []
    for row in tile:
        newtile.append(row[-1::-1])
    
    return newtile

def rot90(tile):
    #rotate tile 90 degrees anticlockwise
    newtile = tile.copy()
    for i in range(len(tile[0])):
        newrow = ''
        for row in tile:
            newrow = ''.join([newrow,row[-(i+1)]])
        newtile[i] = newrow
    
    return newtile


def edge(tile,side):
    #helper function to find one edge of a tile 
    if side == 't':  #top
        return tile[0]
    
    if side == 'b': #base
        return tile[-1]
    
    if side == 'l': #left
        return ''.join([row[0] for row in tile])
    
    if side == 'r': #right
        return ''.join([row[-1] for row in tile])

def match(tiles):
    #determine how many edges of each tile match to another tile
    match_count = defaultdict(int)
    matches = defaultdict(list) 

    corners = []

    for num1, num2 in combinations(tiles,2):
        tile1, tile2 = tiles[num1], tiles[num2]

        for side1 in {'t','b','l','r'}:
            for side2 in {'t','b','l','r'}:
                edge1, edge2 = edge(tile1,side1), edge(tile2,side2)

                #at this point we're not concerned if the tiles need to be flipped or not,
                #so if edge1 is the reverse of edge2, that counts as a match
                if edge1==edge2 or edge1 == edge2[::-1]:
                    match_count[num1] += 1
                    match_count[num2] += 1
                    matches[num1].append(side1)
                    matches[num2].append(side2)

    for num, num_sides in match_count.items():
        #the all-important corner tiles are those with two matches
        if num_sides == 2:
            corners.append(num)
        
    return corners, match_count, matches

corners, match_count, matches = match(tiles)

#arbitrarily, select a corner tile which matches other tiles on the 'right' and 'base'
# to begin building up the image from
for corner in corners:
    if set(matches[corner]) == {'r','b'}:
        start = corner

start_tile = tiles[start]

def orientations(tile):
    #helper function to output all the 8 flipped and rotated versions of the input tile
    trot90 = rot90(tile)
    trot180 = rot90(trot90)
    trot270 = rot90(trot180)
    tflipH = flipH(tile)
    tflipV = flipV(tile)
    tflipD1 = rot90(tflipH) #diagonal flip -> combine flip and rotation
    tflipD2 = rot90(tflipV) #diagonal flip -> combine flip and rotation

    return [tile, trot90, trot180, trot270, tflipH, tflipV, tflipD1, tflipD2]
    

def match_tile(tile1,tiles,side1):
    #find the properly oriented tile which matches tile1 on the specified side1
    #this will be unique for the puzzle input
    for tile2 in tiles.values():

        if tile2 in orientations(tile1):
            continue

        if side1 == 't':
            side2 = 'b'
        if side1 == 'b':
            side2 = 't'
        if side1 == 'l':
            side2 = 'r'
        if side1 == 'r':
            side2 = 'l'
        
        for t2_orient in orientations(tile2):
            if edge(tile1,side1) == edge(t2_orient, side2):      
                return t2_orient

def build(start_tile, tiles, num_cols, num_rows):
    #build up the image by matching tiles
    rows = defaultdict(list)
    
    for i in range(num_rows):
        for j in range(num_cols):
            rows[i].append([])

    for i in range(num_rows):
        if i==0:
            rows[0][0] = start_tile #place the start tile in the top left
        else:
            #match the first tile in the row above to begin a new row
            rows[i][0] = match_tile(rows[i-1][0], tiles, 'b') 

        for j in range(1,num_cols):
            print(i,j)
            #match repeatedly to the right to fill out a row
            next_tile = match_tile(rows[i][j-1], tiles, 'r')
            rows[i][j] = next_tile
    
    return rows

def strip(tile):
    #strip the edges from a tile, as required by the puzzle
    return [row[1:-1] for row in tile[1:-1]]

#Build up the image into one large tile

#dimension of the image is the square root of the number of tiles,
# e.g. 9 tiles --> 3 tile x 3 tile image, 144 tiles --> 12 tile x 12 tile image
dimension = int(len(tiles)**(0.5))

rows = build(start_tile, tiles, dimension, dimension)

stripped_rows = defaultdict(list)

#strip the edges from all the tiles in the image
for row in rows:
    for tile in rows[row]:
        stripped_rows[row].append(strip(tile))

image = []

#combine the tiles in the image into one large tile
for row in stripped_rows:
    image.append([''.join(x) for x in zip(*stripped_rows[row])])

full_image = []

for row in image:
    full_image.extend(row)


#count the sea monsters in the image
def monster_count(image):
    #count the sea monsters in the image and return the monster count and water roughness score

    #hard-code the shape of a sea monster in terms of displacement from the corner character
    deltas = [(0,18), (1,0), (1,5), (1,6),(1,11),(1,12),(1,17),(1,18),(1,19),
    (2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]
    image_dim = len(image)
    mon_count = 0
    hash_count = 0

    #hard-coding the fact that a sea monster takes up a 20x3 grid of characters
    for x in range(image_dim - 3):
        for y in range(image_dim - 20): 

            #all of the characters must be hashes for a sea monster to be present
            if all(image[x+dx][y+dy] == '#' for dx, dy in deltas):
                mon_count += 1
    
    #count all the hashes in the image
    for x in range(image_dim):
        for y in range(image_dim):
            if image[x][y] == '#':
                hash_count += 1
    
    #calculate water roughness, quantity of hashes not part of a monster
    # (a monster contains 15 hashes, monsters do not overlap)
    water_roughness = hash_count - mon_count*15

    return mon_count, water_roughness

#take all 8 orientations of the full image and calculate the water roughness score
for orien in orientations(full_image):
    mon_count, water_roughness = monster_count(orien)

    #only one orientation will contain any monsters,
    # this is the orientation whose water roughness score we want
    if mon_count > 0:
        print(water_roughness)
