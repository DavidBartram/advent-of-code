import sys

with open(sys.argv[1]) as file:
    values = file.read().splitlines()
    newvalues = []
    for value in values:
        newvalues.append(list(value))
    values = newvalues

columns = [[int(values[j][i]) for j in range(len(values))] for i in range(len(values[0]))]

averages = ''

flipped = ''

for column in columns:
    average_bit = int(round(sum(column)/len(column)))
    averages += str(average_bit)
    if average_bit == 1:
        flipped += '0'
    else:
        flipped += '1'

gamma = int(averages,2)

epsilon = int(flipped,2)

print(gamma*epsilon)
