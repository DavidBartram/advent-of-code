import sys
import re


with open(sys.argv[1]) as file:
    rules = [line.rstrip('\n') for line in file]

outers = set()

def bagfind(colour):
    for rule in rules:
        if colour in rule and not rule.startswith(colour) :
            outer = ' '.join(rule.split()[0:2])
            outers.add(outer)
            bagfind(outer)

bagfind('shiny gold')

print(len(outers))
