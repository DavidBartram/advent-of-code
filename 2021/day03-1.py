import sys
from math import ceil

with open(sys.argv[1]) as file:
    values = file.read().splitlines()

length = len(values[0])

ones = [0]*length

for value in values:
    for i in range(length):
        if value[i] == '1':
            ones[i] += 1

gamma=''
epsilon=''

for x in ones:
    if x > ceil(len(values)/2):
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma,2)*int(epsilon,2))
