import sys

with open(sys.argv[1]) as file:
    map_ = file.read().splitlines()

def  trees(dx, dy):
    x = 0
    y = 0
    xmax = len(map_[0])
    ymax = len(map_)
    count = 0

    if map_[x][y] == "#":
        count = 1

    while y < ymax:
        x = (x+dx)%(xmax)
        y = (y+dy)

        if y  >= ymax:
            break
        
        if map_[y][x] != "." and map_[y][x] !="#":
            print("error at x=",x, "y=",y)
            break

        elif map_[y][x] == "#":
            count += 1

    return count

#part 1
print(trees(3,1))


#part 2
print("product", trees(1,1)*trees(3,1)*trees(5,1)*trees(7,1)*trees(1,2) )
