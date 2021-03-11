import sys
from math import gcd

def lcm(x, y): #calculate lowest common denominator of two integers
    return x * y // gcd(x, y)

with open(sys.argv[1]) as file:
    notes = [line.rstrip('\n').split(",") for line in file]

buses = notes[1]

offsets = {}
buslist = []

for bus in buses:
    if bus != 'x':
        offsets[int(bus)] = buses.index(bus) % int(bus) #the modulus is really helpful if int(bus) < buses.index(bus)
        buslist.append(int(bus))

def find(k,i,increment):
    if k >= len(buslist):
        return i

    while True:
            target = buslist[k] - offsets[buslist[k]]

            if i % buslist[k] == target:
                new_inc = lcm(increment,buslist[k])
                return find(k+1,i,new_inc)
                
            else:
                i = i + increment
    
print(find(1,buslist[0],buslist[0])) 
