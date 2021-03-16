import sys
import re

#Process the input into rules and words
with open(sys.argv[1]) as file:
    pattern = r'([0-9]+):(.+)'
    rules = {int(re.findall(pattern,x)[0][0]) : re.findall(pattern,x)[0][1]  for x in file.readlines() if re.match(pattern,x) }

with open(sys.argv[1]) as file:
    pattern = r'[a-z]+'
    words = [x.replace('\n','') for x in file.readlines() if re.match(pattern,x)]

#tidy up the rules into a more usable format, so that each rule is:
#a list containing a single character e.g. ['a']  OR
#a list of rule numbers e.g. [3,5,2]
#a list of lists of rule numbers, if the original rule contained a "|" meaning OR
#e.g. [[7,2,33], [6,7,10]]
newrules = rules.copy()

for key, val in rules.items():
    if re.match(r' "[a-z]"', val):
        newrules[key] = val.replace("\"", "").replace(" ", "")
    
    else:
        if "|" in val:
            newval = val.split("|")
            newval = [[int(y) for y in x.split()] for x in newval]
        else:
            newval = [[int(y) for y in val.split()]]
        
        newrules[key] = newval

rules = newrules

#recursive function to check a word against rule 0
def check(word, rules, rule_number=0):

    #if you're past the end of the word, return the empty list
    if word == '':
        return [] 

    #look up the rule in the rules dict
    rule = rules[rule_number]

    #if the rule is a string, it will be one character
    #this character should be matched to the first character of the word
    #then output a list containing the rest of the word if successful
    #or the empty list if unsuccessful
    if isinstance(rule,str):

        if word[0] == rule:
            return [word[1:]]
        else:
            return []

    matches = []

    #rules containing a single rule list or two options are both handled here
    for option in rule:
        #begin with the entire word
        opt_matches = [word] 

        for subrule_number in option: 
            new_matches = []
            for wd in opt_matches:
                #recursive function call
                new_matches += check(wd, rules, subrule_number)
            
            opt_matches = new_matches
        
        matches += opt_matches
    
    return matches

count = 0

for word in words:
    if '' in check(word,rules):
        count += 1

print(count)
