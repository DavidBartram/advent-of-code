import sys
import re
from itertools import product


# (A) PROCESS THE INPUT

with open(sys.argv[1]) as file:
    text = file.read()
    allergen_pattern = r'\(contains (.+)\)'
    allergens = re.findall(allergen_pattern, text)

allergens = [x.split(',') for x in allergens]
allergens = [[y.replace(' ', '') for y in x] for x in allergens]

with open(sys.argv[1]) as file:
    text = file.read()
    ingredient_pattern = r'([a-z]+) '
    ingredients = re.findall(ingredient_pattern, text)

ingredients = ' '.join(ingredients).split('contains')

ingredients = [x.split() for x in ingredients]

ingredients.remove([])

#Construct a set of all allergens in the input
all_allergens = set()

for x in allergens:
    for y in x:
        all_allergens.add(y)

#Construct a set of all ingredients in the input
all_ingredients = set()

for x in ingredients:
    for y in x:
        all_ingredients.add(y)

# (B) MAXIMUM BIPARTITE MATCHING OF INGREDIENTS & ALLERGENS

#create a dict called possibility. the keys will be tuples of (ingredient,allergen) e.g. ('mfp','dairy')
#the value will be 1 if the ingredient may contain the allergen
#the value will be 0 if the ingredient definitely does not contain the allergen
possibility = {}

#initialise the dictionary with all matchings possible
for (ing,allerg) in product(all_ingredients, all_allergens):
    possibility[(ing,allerg)] = 1


#the only deduction we can make from the input is the following:
#IF an ingredient does not appear in a given row
#THEN that ingredient DOES NOT contain any of that row's listed allergens
for i, row in enumerate(ingredients):
    for ing in all_ingredients:
        if ing not in row:
            for allerg in allergens[i]:
                possibility[(ing,allerg)] = 0


def match(possibility,allerg,all_ingredients, matchR, seen):
    #takes the possibility dictionary, a particular allergen, the current assignment of ingredients to allergens, and a dict to keep track of which ingredients have been visited
    #if the conditions are met, assigns the allergen to a particular ingredient in matchR and returns True
    #otherwise returns False


    #iterate over the possible ingredients that could contain the allergen
    for ing in all_ingredients:
        
        # If the matching of the ingredient to the allergen is possible
        # and the ingredient has not yet been visited
        if possibility[(ing,allerg)] == 1 and seen[ing] == False: 
            # Mark the allergen as visited
            seen[ing] = True 
  
            #If the ingredient is not currently assigned to an allergen (matchR[ing] == -1)
            # OR the previously assigned allergen for the ingredient (matchR[ing]) has an alternate ingredient available
            if matchR[ing] == -1 or match(possibility,matchR[ing], all_ingredients, matchR, seen): 
                matchR[ing] = allerg #assign the allergen to the ingredient we are considering
                #print(matchR)
                return True

    return False

def maxmatch(possibility, all_allergens, all_ingredients): 
    # takes the possibility dict, the set of all allergens in the input, the set of all ingredients in the input
    # returns matchR for the maximum matching
    # matchR is a dict showing which ingredients have been assigned to which allergens
    # in matchR the keys is an ingredient, the value is an allergen, or -1 if the ingredient has not yet been assigned to an allergen
    matchR = {ing:-1 for ing in all_ingredients} #initialise with no allergens assigned to ingredients
    
    #iterate over ingredients
    for allergen in all_allergens: 
        seen = {ing: False for ing in all_ingredients} #before considering a new allergen, reset the visited ingredients
        match(possibility, allergen, all_ingredients, matchR, seen)

    return matchR


matchR = maxmatch(possibility, all_allergens, all_ingredients) #run the matching function

#construct a list of allergen-free ingredients
allerg_free_ings = []

for ing in matchR:
    if matchR[ing] == -1: #if the ingredient has no allergen assigned at this stage, then it contains no allergens
        allerg_free_ings.append(ing)


#Part 1
#count the number of times the allergen-free ingredients appear in the full list of recipes
count = 0
for row in ingredients:
    for ing in row:
        if ing in allerg_free_ings:
            count +=1

print(count) #part 1 answer


#Part 2

#remove the allergen-free ingredients from the match dictionary
for ing in allerg_free_ings:
    del matchR[ing]

#sort the (ingredient,allergen) tuples alphabetically by allergen
sorted_tuples = sorted(matchR.items(), key=lambda item: item[1])

#take the allergen-bearing ingredients and join into one comma-separated string
sorted_ings = ','.join( [x[0] for x in sorted_tuples] )

print(sorted_ings) #part_2 answer
