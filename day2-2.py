import sys

with open(sys.argv[1]) as file:
    lines = list()
    for line in file:
        line = line.replace(":", "")
        line = line.replace("-", " ")
        lines = lines + [line.strip().split()]

validcount = 0
for line in lines:
    pos1 = int(line[0]) - 1
    pos2 = int(line[1]) - 1
    char = line[2]
    password = line[3]

    if password[pos1] == char:

        if password[pos2] != char:
            validcount += 1

    elif password[pos2] == char:
        validcount += 1

print(validcount)
