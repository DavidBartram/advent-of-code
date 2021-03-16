import sys
import re
from collections import defaultdict
from itertools import combinations

with open(sys.argv[1]) as file:
    tiles = file.read().split('\n\n')

tiles = [tile.replace('Tile ', '').replace(':','').split('\n') for tile in tiles]

tiles = {int(tile[0]):tile[1:] for tile in tiles}

for tile in tiles.values():
        try:
            tile.remove('')
        except ValueError:
            pass

def flipV(tile):
    newtile = list(reversed(tile))

    return newtile

def flipH(tile):
    newtile = []
    for row in tile:
        newtile.append(row[-1::-1])
    
    return newtile

def rot90(tile):
    newtile = tile.copy()
    for i in range(len(tile[0])):
        newrow = ''
        for row in tile:
            newrow = ''.join([newrow,row[-(i+1)]])
        newtile[i] = newrow
    
    return newtile


def edge(tile,side):
    if side == 't':  #top
        return tile[0]
    
    if side == 'b': #base
        return tile[-1]
    
    if side == 'l': #left
        return ''.join([row[0] for row in tile])
    
    if side == 'r':
        return ''.join([row[-1] for row in tile])

def match(tiles):
    match_count = defaultdict(int)
    matches = defaultdict(list) 

    corners = []

    for num1, num2 in combinations(tiles,2):
        tile1, tile2 = tiles[num1], tiles[num2]

        for side1 in {'t','b','l','r'}:
            for side2 in {'t','b','l','r'}:
                edge1, edge2 = edge(tile1,side1), edge(tile2,side2)

                if edge1==edge2 or edge1 == edge2[::-1]:
                    match_count[num1] += 1
                    match_count[num2] += 1
                    matches[num1].append(num2)
                    matches[num2].append(num1)
    
    for num, num_sides in match_count.items():
        if num_sides == 2:
            corners.append(num)
    
    return corners, match_count, matches


corners, match_count, matches = match(tiles)
prod = 1

for corner in corners:
    prod = prod * corner

print(prod)
