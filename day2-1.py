import sys

with open(sys.argv[1]) as file:
    lines = list()
    for line in file:
        line = line.replace(":","")
        line = line.replace("-"," ")
        lines = lines + [line.strip().split()]

validcount = 0
lettercount = 0

for line in lines:
    mincount = int(line[0])
    maxcount = int(line[1])
    char = line[2]
    password = line[3]

    lettercount = password.count(char)
    if mincount <= lettercount <= maxcount :
        validcount += 1
       
print(validcount)
