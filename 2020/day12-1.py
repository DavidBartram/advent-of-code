import sys
import re

with open(sys.argv[1]) as file:
    cmds = [line.rstrip('\n') for line in file]

heading = 'E'

bearings = {'N':{'dx':0,'dy':1}, 'S':{'dx':0,'dy':-1}, 'E':{'dx':1,'dy':0}, 'W':{'dx':-1,'dy':0}}

rotations = {'R90':1,'R180':2,'R270':-1,'L90':-1,'L180':-2,'L270':1}

newbearings = ['N','E','S','W']

(x,y) = (0,0)

for cmd in cmds:
    m = re.match(r'(\w)(\d+)',cmd)
    op = m.group(1)
    arg = int(m.group(2))

    if op == 'F':
            dx, dy = bearings[heading]['dx'] , bearings[heading]['dy']
            (x,y) = (x+arg*dx,y+arg*dy)

    if op in bearings:
        dx, dy = bearings[op]['dx'] , bearings[op]['dy']
        (x,y) = (x+arg*dx,y+arg*dy)
    
    if cmd in rotations:
        k = rotations[cmd]
        i = (newbearings.index(heading) + k)%4
        heading = newbearings[i]

print((x,y,heading))

print(abs(x)+abs(y))
