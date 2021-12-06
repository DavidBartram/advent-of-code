import sys

with open(sys.argv[1]) as file:
    moves = [line.rstrip('\n') for line in file]

(x,y, aim) = (0,0,0)

for move in moves:
    dir, value = move.split()

    value = int(value)
    
    if dir == 'forward':
        x += value
        y += aim*value
    
    elif dir == 'up':
        aim -= value
    
    elif dir == 'down':
        aim += value

print(x*y)
