import sys

sum_ = 2020

with open(sys.argv[1]) as f:
    lines = [l.rstrip('\n') for l in f]

print(lines)
