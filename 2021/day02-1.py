import sys

with open(sys.argv[1]) as file:
    moves = [line.rstrip('\n') for line in file]

(x,y) = (0,0)

for move in moves:
    dir, value = move.split()

    value = int(value)
    
    if dir == 'forward':
        x += value
    
    elif dir == 'up':
        y -= value
    
    elif dir == 'down':
        y += value

print(x*y)
