import sys

sum_ = 2020

with open(sys.argv[1]) as f:
    lines = [int(l.rstrip('\n')) for l in f]
    trios = {}

    for line in lines:

        for line2 in lines:
            x = sum_ - line - line2

            if x in lines and len({x, line, line2}) == 3:
                trios[frozenset({x, line, line2})] = x*line*line2

    for key, val in trios.items():
        print(key, ":", val)

        
