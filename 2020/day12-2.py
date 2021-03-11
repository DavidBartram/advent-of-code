import sys
import re
from math import radians, sin, cos

with open(sys.argv[1]) as file:
    cmds = [line.rstrip('\n') for line in file]

heading = 'E'

bearings = {'N':{'dx':0,'dy':1}, 'S':{'dx':0,'dy':-1}, 'E':{'dx':1,'dy':0}, 'W':{'dx':-1,'dy':0}}

def rotation(wp, arg):
    c = int(cos(radians(arg))) #safe to cast to int as arg is always an element of {-270,-180,-90,90,180,270}
    s = int(sin(radians(arg))) #safe to cast to int as arg is always an element of {-270,-180,-90,90,180,270}
    wp['x'], wp['y'] = c*wp['x'] - s*wp['y'] , s*wp['x'] + c*wp['y']

newbearings = ['N','E','S','W']

ship = {'x':0, 'y':0}

wp = {'x':10,'y':1}

for cmd in cmds:
    m = re.match(r'(\w)(\d+)',cmd)
    op = m.group(1)
    arg = int(m.group(2))

    if op == 'F':
            ship['x'] += arg*wp['x']
            ship['y'] += arg*wp['y']

    if op in bearings:
        dx, dy = bearings[op]['dx'] , bearings[op]['dy']
        wp['x'] += arg*dx
        wp['y'] += arg*dy
    
    if op == 'L':
        rotation(wp,arg)
    
    if op == 'R':
        rotation(wp,-1*arg)

print((ship['x'],ship['y'],heading))

print(abs(ship['x'])+abs(ship['y']))
