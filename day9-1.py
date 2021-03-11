import sys

with open(sys.argv[1]) as file:
    l = [int(line) for line in file]

k=25

m = [(l[i+k], set(l[i:i+k])) for i in range(len(l)-k)]


for (x,y) in m:
    haspair=False
    for val in y:
        goal = x - val
        if goal in y:
          haspair=True
          
    if haspair==False:
        print(x)
        break
