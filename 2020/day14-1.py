import sys

with open(sys.argv[1]) as file:
    lines = [line.rstrip('\n').split() for line in file]

mask = ''

mem = {}

for line in lines:
    if line[0].startswith('mask'):
        mask = line[2]
    else:
        key = line[0].replace('mem[','').replace(']','')
        value = format(int(line[2]),'036b')
        newvalue = ''

        for i, x in enumerate(value):
            if mask[i] != 'X':
                newvalue += mask[i]
            else:
                newvalue += x
        
        value = int(newvalue,2)

        mem[int(key)] = value

#print(mem)

sum = 0

for key,val in mem.items():
    sum += val

print(sum)





