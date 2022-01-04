import sys
from collections import defaultdict

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

def decode(signal):
    decoder = defaultdict(lambda: '.')
    segs = defaultdict(lambda: [])

    for x in signal:
        segs[len(x)].append(frozenset(x))
        if len(x) == 2:
            decoder[frozenset(x)] = '1'
                
        elif len(x) == 4:
            decoder[frozenset(x)] = '4'
                
        elif len(x) == 3:
            decoder[frozenset(x)] = '7'

        elif len(x) == 7:
            decoder[frozenset(x)] = '8'

    for y in segs[5]:
        overlap_with_7 = len(y.intersection(segs[3][0]))

        overlap_with_4 = len(y.intersection(segs[4][0]))

        if overlap_with_7 == 3:
            decoder[y] = '3'
        
        elif overlap_with_4 == 3:
            decoder[y] = '5'
        
        else:
            decoder[y] = '2'

    for z in segs[6]:
        overlap_with_7 = len(z.intersection(segs[3][0]))

        overlap_with_4 = len(z.intersection(segs[4][0]))

        if overlap_with_7 == 2:
            decoder[z] = '6'
            
        elif overlap_with_4 == 4:
            decoder[z] = '9'
            
        else:
            decoder[z] = '0'
        
    
    return decoder



def decode_outputs(signals,outputs):

    decoded_outputs=[]
    for signal,output in zip(signals,outputs):
        decoder = decode(signal)
        decoded_output = ''

        for x in output:
            decoded_output += decoder[frozenset(x)]
        
        decoded_outputs.append(int(decoded_output))
        
    
    return decoded_outputs

print(sum(decode_outputs(signals,outputs)))
