from collections import defaultdict, Counter
from itertools import product
from functools import lru_cache
import sys

dice_results = list(product({1,2,3},repeat=3))

dice_results = [sum(result) for result in dice_results]

dice_freq = dict(Counter(dice_results))

print(dice_freq)

@lru_cache(maxsize=50000)
def play_dirac_dice(pos1, score1, pos2, score2, whoseTurn):

    #print(pos1, score1, pos2, score2, whoseTurn)

    if score1>=21:
        return 1
    
    elif score2>=21:
        return 0
    
    subgame_total = 0

    if whoseTurn == 1:
        for dice in dice_freq:
            newpos = (pos1+dice-1)%10 + 1
            subgame_total += dice_freq[dice]*play_dirac_dice(newpos,score1+newpos,pos2,score2,2)

    else:
        for dice in dice_freq:
            newpos = (pos2+dice-1)%10 + 1
            subgame_total += dice_freq[dice]*play_dirac_dice(pos1,score1,newpos,score2+newpos,1)

    return subgame_total

start1 = 7
start2 = 5

wins = (play_dirac_dice(start1,0,start2,0,1), play_dirac_dice(start2,0,start1,0,2))

print(play_dirac_dice.cache_info())

print(max(wins))





