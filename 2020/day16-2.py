import sys
import re


# (A) PROCESS THE INPUT

with open(sys.argv[1]) as file:
    notes = file.read()

field_pattern = r'([a-zA-Z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'

fields = re.findall(field_pattern, notes)

field_dict = {}

#translate the information about each field into a set of allowed values for each field
for field in fields:
    values = set()
    a = int(field[1])
    b = int(field[2])+1
    values = values.union(set(range(a,b)))

    c = int(field[3])
    d = int(field[4])+1

    values = values.union(set(range(c,d)))

    field_dict[field[0]] = values

#create a set holding all the valid values for any field
all_valid_values = set()

for field, values in field_dict.items():
    all_valid_values = all_valid_values.union(values)

#process my ticket into a list of integers
my_ticket_pattern = r'your ticket:\n(.+)'

my_ticket = re.findall(my_ticket_pattern, notes)

my_ticket =[int(x) for x in my_ticket[0].split(',') ]

#process the nearby tickets into lists of integers
tickets_pattern = r'(?:nearby tickets:)(\n(?:.+\n)+)'

tickets = re.findall(tickets_pattern, notes)[0]

tickets = re.split('\n', tickets)

tickets = [x for x in tickets if x]

tickets = [x.split(',') for x in tickets]

# (B) IDENTIFY VALID TICKETS

#determmine which tickets are valid in the sense of containing only values which are valid for SOME field
validtickets = tickets.copy()

for ticket in tickets:
    for num in ticket:
        num = int(num)
        if num not in all_valid_values:
            validtickets.remove(ticket)

# (C) FIND BIPARTITE MATCHING OF FIELD NAMES TO POSITIONS ON TICKET

#create a dictionary called 'possibility' to represent the bipartite graph of possible positions to fields
#keys = field names  values = list of 0s and 1s representing which positions the field could match to
#e.g. if possibility['foo'] = [0,1,0,1,0,0,1] then the 'foo' field could match to position 1, 3 or 6
#initialise such that any field could match to any position, so all values are lists of 1s
#later the matchings which aren't possible will be set to zero
w=len(validtickets[0])
possibility = {y:[1 for x in range(w)] for y in field_dict}

#set impossible matchings to have value zero in the possibility dictionary
for ticket in validtickets:
    for field in field_dict:
        for j, x in enumerate(ticket):
            x = int(x)
            if x not in field_dict[field]:
                possibility[field][j] = 0   #if the value in this position on any valid ticket is not valid for this field, then the match is not possible


def match(possibility,field, matchR, seen):
    #takes the possibility dictionary, a particular field, the current assignment of fields to positions, and a list to keep track of which positions have been visited
    #if the conditions are met, assigns the field to a particular position in matchR and returns True
    #otherwise returns False


    #iterate over the possible positions the field could be assigned to
    for j in range(len(possibility)): 
  
        # If the matching of the field to this position is possible 
        # and position j has not yet been visited
        if possibility[field][j] and seen[j] == False: 
                  
            # Mark position j as visited
            seen[j] = True 
  
            #If position j is not currently assigned to a field (matchR[j] == -1)
            # OR the previously assigned field for position j (matchR[j]) has an alternate position available
            # since position j is marked as visited in the above line, the recursive call will not visit position j again
            if matchR[j] == -1 or match(possibility,matchR[j], matchR, seen): 
                matchR[j] = field #assign position j to the field we are considering
                return True

    return False

def maxmatch(possibility, field_dict): 
    # matchR is a list of fields assigned to each position
    # here we use a convention where if matchR[k] == -1, then position k has not yet been assigned to a field
    matchR = [-1] * len(possibility) #initialise with no positions assigned to fields
    
    #iterate over fields
    for field in field_dict: 
        seen = [False] * len(possibility) #before considering a new field, reset the visited positions
        match(possibility, field, matchR, seen)

    return matchR

matchR = maxmatch(possibility, field_dict)

#(D) CALCULATE PUZZLE SOLUTION

#build up the product of values in my ticket for fields beginning with 'departure', as required to get the puzzle solution
product = 1

for i,field in enumerate(matchR):
    if field.startswith('departure'):
        product = product*my_ticket[i]

print(product)
