import sys
import re


with open(sys.argv[1]) as file:
    rules = [line.rstrip('\n') for line in file]

count = 0

def bagcount(colour):
    nextcolour = ''
    global count
    for rule in rules:
        if rule.startswith(colour):
            for x in re.findall(r'\d+ \w+ \w+',rule):
                num = int(x.split()[0])
                nextcolour = ' '.join(x.split()[1:3])
                for i in range(num):
                        count += 1
                        bagcount(nextcolour)
            
            

bagcount('shiny gold')

print(count)
