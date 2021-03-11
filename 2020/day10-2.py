import sys

with open(sys.argv[1]) as file:
    ratings = [int(line) for line in file]

memo = {}

def cost(x):

    if x in memo:
        return memo[x]
    
    ways = 0

    if x == max(ratings):
        ways = 1
    if x+1 in ratings:
        ways += cost(x+1)
    if x+2 in ratings:
        ways += cost(x+2)
    if x+3 in ratings:
        ways += cost(x+3)

    memo[x] = ways
    return ways
    

print(cost(0))
