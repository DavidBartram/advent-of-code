import sys

#read input
with open(sys.argv[1]) as f:
    depths = [int(l.rstrip('\n')) for l in f]


#non-pythonic way with indexing
count = 0

for i in range(1,len(depths)):
    if depths[i] > depths[i-1]:
        count += 1

print(count)


#more pythonic way with list comprehension

increase = [x<y for x,y in zip(depths,depths[1:])]

print(sum(increase))

