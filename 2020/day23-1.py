
input = '389125467' #puzzle input

input = [int(x) for x in input]

#initialise a list called nex_list
#in this list, nex_list[i] is the number of the cup immediately clockwise of cup i
#so if nex_list[5] == 2  then cup 2 is directly clockwise of cup 5
#this allows for efficiently moving cups from one position in the circle to another,
#without the reindexing that can slow down a circular data structure such as a Python deque

nex_list = [0]*(max(input) + 1)

#fill in nex_list based on the original order of the cups
for i,x in enumerate(input):

    #it's a circle, so the first cup is immediately clockwise of the last cup
    if i == len(input) - 1:
        nex_list[x] = input[0]
    
    #at the beginning each cup is followed by the subsequent cup in the input
    else:
        nex_list[x] =  input[i+1]

#this function will play one round of the game
def play(nex_list, current):
    pickup = [0,0,0]

    #current cup
    x = current

    #add the next three cups to the pickup list
    for i in range(3):
        pickup[i] = nex_list[x]
        x = nex_list[x]

    #choose the destination cup according to the rules
    dests = input.copy()
    dests.sort()
    for x in pickup:
        dests.remove(x)
    
    idx = dests.index(current)

    dest = dests[idx - 1]

    #update nex_list to reflect the new location of the picked up cups

    nex_list[current] = nex_list[pickup[2]]

    nex_list[pickup[0]] = pickup[1]

    nex_list[pickup[1]] = pickup[2]

    nex_list[pickup[2]] = nex_list[dest]

    nex_list[dest] = pickup[0]
    
    return nex_list, nex_list[current]

def make_list(nex_list, start):
    #helper function to create a list of cup numbers going clockwise from a starting cup
    #used only for debugging
    output = [start]
    seen = []
    current = start

    while nex_list[current] not in seen:
        seen.append(current)
        output.append(nex_list[current])
        current = nex_list[current]
    
    return output

#play the game for 100 tuens
turns = 100

current = input[0]

for i in range(turns):
    nex_list, current = play(nex_list,current)

#create the required output string
cup = 1
output_string = ''

for i in range(len(input)-1):
    cup = nex_list[cup]
    output_string += str(cup)

print(output_string)
