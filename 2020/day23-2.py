input = '389125467' #puzzle input

input = [int(x) for x in input]

#fill in additional cups up to 1,000,000 cups

max_cup = 1000000

input.extend(list(range(max(input)+1, max_cup+1)))

#initialise a list called nex_list
#in this list, nex_list[i] is the number of the cup immediately clockwise of cup i
#so if nex_list[5] == 2  then cup 2 is directly clockwise of cup 5
#this allows for efficiently moving cups from one position in the circle to another,
#without the reindexing that can slow down a circular data structure such as a Python deque

nex_list = [0]*(1000001)

input_len = len(input)

#insert the initial values into nex_list
for i,x in enumerate(input):

    if i == input_len - 1:
        nex_list[x] = input[0]
    
    else:
        nex_list[x] =  input[i+1]


def play(nex_list, current):
    #play one round of the cup game
    
    pickup = [0,0,0]
    #current cup number
    x = current

    #"pick up" the next three cups by adding their values to the pickup list
    for i in range(3):
        pickup[i] = nex_list[x]
        x = nex_list[x]

    #calculate the destination cup according to the rules
    dest = current - 1

    
    while dest in pickup:
        dest = dest - 1
    
    if dest < 1:
        dest = max_cup
    
    while dest in pickup:
        dest = dest - 1

    
    #update nex_list to account for the new positions of the picked-up cups

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
    seen = set()
    current = start

    while nex_list[current] not in seen:
        seen.add(current)
        output.append(nex_list[current])
        current = nex_list[current]
    
    return output

#ten million turns
turns = 10000000

current = input[0]

for i in range(turns):
    nex_list, current = play(nex_list,current)


#construct required output for puzzle
cup = 1
output = 1

for i in range(2):
    cup = nex_list[cup]
    output *= cup

print(output)
