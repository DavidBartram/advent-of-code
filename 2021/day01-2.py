import sys


with open(sys.argv[1]) as f:
    depths = [int(l.rstrip('\n')) for l in f]

#non-pythonic way with indexing
count = 0

sums = []

window_size = 3

for i in range(len(depths)-window_size+1):
    sums.append(sum(depths[i:i+window_size]))

#non-pythonic way with indexing
count = 0

for i in range(1,len(sums)):
    if sums[i] > sums[i-1]:
        count += 1

print(count)


#more pythonic way with list comprehension

increase = [x<y for x,y in zip(sums,sums[1:])]

print(sum(increase))
