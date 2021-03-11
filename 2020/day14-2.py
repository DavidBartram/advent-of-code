import sys

with open(sys.argv[1]) as file:
    lines = [line.rstrip('\n').split() for line in file]

mask = ''

mem = {}  

def keyversions(keylist,value):
    if 'X' not in keylist:
        key = ''.join(keylist)
        mem[key] = value
    else:
        keycopy = keylist.copy()
        for i,char in enumerate(keylist):
            if char == 'X':
                keycopy[i] = '0'
                keyversions(keycopy,value)
                keycopy[i] = '1'
                keyversions(keycopy,value)

for line in lines:
    if line[0].startswith('mask'):
        mask = line[2]
    else:
        key = line[0].replace('mem[','').replace(']','')
        key = format(int(key),'036b')
        keylist = []

        for i, x in enumerate(key):
            if mask[i] == '0':
                keylist.append(x)
            elif mask[i] == '1':
                keylist.append('1')
            elif mask[i] == 'X':
                keylist.append('X')

        value = int(line[2])

        keyversions(keylist,value)


sum = 0

for key,val in mem.items():
    sum += val

print(sum)
