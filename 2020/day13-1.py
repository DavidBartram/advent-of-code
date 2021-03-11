import sys

with open(sys.argv[1]) as file:
    notes = [line.rstrip('\n').replace('x,','').split(",") for line in file]

start = int(notes[0][0])

nexttime = {}


for bus in notes[1]:
    bus = int(bus)
    i = start
    while i % bus != 0:
        i += 1
    nexttime[i] = bus

first_bus = nexttime[min(nexttime)]

wait_time = min(nexttime)- start

print(first_bus * wait_time)
