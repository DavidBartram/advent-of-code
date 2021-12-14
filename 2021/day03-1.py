import sys
from math import ceil

with open(sys.argv[1]) as file:
    values = file.read().splitlines()

length = len(values[0]) #length of each binary number

ones = [sum([value[i]=='1' for value in values]) for i in range(length)] #number of ones in each column as a list

threshold = ceil(len(values)/2) 

gamma = int(''.join(['1' if x>threshold else '0' for x in ones]), base=2)

epsilon = 2**length - 1 - gamma #subtracting from 2^(length) - 1 is equivalent to flipping all bits in the binary representation

print(gamma*epsilon)
