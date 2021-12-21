from collections import defaultdict
from itertools import product
from functools import lru_cache
import sys

dice_results = list(product({1,2,3},repeat=3))

dice_results = [sum(result) for result in dice_results]
print(dice_results)

memo = {}

@lru_cache(maxsize=10**5)
def play_dirac_dice(pos1, score1, pos2, score2, whoseTurn):

    #print(pos1, score1, pos2, score2, whoseTurn)

    if score1>=21:
        return 1
    
    elif score2>=21:
        return 0
    
    if whoseTurn == 1:
        newpos = [(pos1+result-1)%10 + 1 for result in dice_results]
        subgame_results = [play_dirac_dice(pos,score1+pos,pos2,score2,2) for pos in newpos]
        return sum(subgame_results)

    else:
        newpos = [(pos2+result-1)%10 + 1 for result in dice_results]
        subgame_results = [play_dirac_dice(pos1,score1,pos,score2+pos,1) for pos in newpos]
        return sum(subgame_results)

start1 = 7
start2 = 5

wins = (play_dirac_dice(start1,0,start2,0,1), play_dirac_dice(start2,0,start1,0,2))

print(max(wins))
    





