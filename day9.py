import sys

with open(sys.argv[1]) as file:
    l = [int(line) for line in file]


#Part 1 
k=25

# Set up a list of tuples, the first element of each tuple is a value from the list,
# the second element is the set of the k previous values
m = [(l[i+k], set(l[i:i+k])) for i in range(len(l)-k)]

#for each tuple, determine if the second element (the set) contains two values which sum to the first element (the value)
for (x,y) in m:
    haspair=False
    for val in y:
        goal = x - val
        if goal in y:
          haspair=True
          
    if haspair==False:
        s = x
        break

print(s)

#Part 2
#Find a sublist of any length which sums to the answer from Part 1

def findsub():
    for k in range(2,len(l)):
        sublists = [l[i:i+k] for i in range(len(l)-k+1)]
        for x in sublists:
            if sum(x) == s:
                return min(x)+max(x)

print(findsub())
