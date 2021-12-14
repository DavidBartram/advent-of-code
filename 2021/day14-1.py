import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    data = file.readlines()

polymer = data[0].replace('\n','')

rules = [tuple(x.replace('\n','').replace(' -> ','')) for x in data[2:]]

def initialise(data):

    polymer = data[0].replace('\n','')

    rules = [tuple(x.replace('\n','').replace(' -> ','')) for x in data[2:]] #AB -> N  becomes (A,B,N)

    elements = defaultdict(lambda: 0)

    pairs = defaultdict(lambda: 0)
    
    for (x,y) in zip(polymer,polymer[1:]):
        elements[x] += 1
        pairs[(x,y)] += 1

    elements[polymer[-1]] +=1 #the last element in the zip object above will be (polymer[n-1],polymer[n]) so the last element won't be counted
    
    return elements, pairs, rules

def apply_rules(rules, elements, pairs):
    
    newelements = elements.copy()
    newpairs = pairs.copy()

    for rule in rules:
        (x,y,z) = rule

        count = pairs[(x,y)]

        if count > 0:
            newpairs[(x,y)] -= count #pairs are removed when new char inserted

            newelements[z] += count #new char inserted for each pair
            newpairs[(x,z)] += count #new pair created for each pair
            newpairs[(z,y)] += count #new pair created for each pair
    
    return newelements, newpairs

def apply_rules_n_times(n, rules, elements,pairs):

    for i in range(n):
        elements, pairs = apply_rules(rules, elements, pairs)

    freqs = elements.values()

    return max(freqs) - min(freqs)

elements, pairs, rules = initialise(data)

print(apply_rules_n_times(10, rules,elements,pairs))

print(apply_rules_n_times(40, rules,elements,pairs))





