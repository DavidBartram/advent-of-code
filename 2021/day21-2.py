from collections import defaultdict, Counter
from itertools import product
from functools import lru_cache
import sys


#calculate the frequency of each possible sum of 3 rolls of a 3-sided die with sides labelled 1, 2 and 3
dice_results = list(product({1,2,3},repeat=3))

dice_results = [sum(result) for result in dice_results]

dice_freq = dict(Counter(dice_results))

@lru_cache(maxsize=200000) #caching
def play_dirac_dice(pos1, score1, pos2, score2, whoseTurn):
    #given the position and score of each player, and a marker for whose turn is next
    #return the number of universes arising from this game state in which player 1 wins

    #print(pos1, score1, pos2, score2, whoseTurn)

    if score1>=21: #player 1 wins
        return 1
    
    elif score2>=21: #player 2 wins
        return 0
    
    subgame_total = 0

    if whoseTurn == 1: #player 1 takes a turn next
        for dice in dice_freq:
            newpos = (pos1+dice-1)%10 + 1 #update player 1's position

            #recursively call the function for the updated game state
            #multiply by dice_freq[dice] because each total on the dice has a different frequency
            #e.g. there are 3 universes in which dice==3 but 7 universes in which dice==6
            subgame_total += dice_freq[dice]*play_dirac_dice(newpos,score1+newpos,pos2,score2,2)

    else: #player 2 takes a turn next
        for dice in dice_freq:
            newpos = (pos2+dice-1)%10 + 1 #update player 1's position

            #as above, recursively call the function for the updated game state
            subgame_total += dice_freq[dice]*play_dirac_dice(pos1,score1,newpos,score2+newpos,1)

    return subgame_total

#starting positions hard-coded from the input
start1 = 7 
start2 = 5 

wins = (play_dirac_dice(start1,0,start2,0,1), play_dirac_dice(start2,0,start1,0,2))

print(max(wins))





