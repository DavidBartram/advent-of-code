import sys

with open(sys.argv[1]) as file:
    data = file.read().splitlines()

    signals = []
    outputs = []
    
for line in data:
    line = line.split('|')

    signal = line[0].split(' ')
    signal.remove('')

    output = line[1].split(' ')
    output.remove('')

    signals.append(signal)
    outputs.append(output)

count=0

for output in outputs:
    for x in output:
        if len(x) in {2,4,3,7}:
            count += 1

print(count)
