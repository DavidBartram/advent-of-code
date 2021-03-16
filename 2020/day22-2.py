import sys
import re
import collections

#(A) Process the Input

with open(sys.argv[1]) as file:
    decks = file.read()

decks = decks.split('Player')

decks.remove('')

decks = [x[3:].split('\n')for x in decks]

decks = [[int(y) for y in x if y] for x in decks ]

decks = [collections.deque(x) for x in decks]

deck_p1 = decks[0] #player 1 deck

deck_p2 = decks[1] #player 2 deck

#(B) Play Recursive Crab Combat

#helper function to adjust decks based on the winner of a round
def win(deck_p1, deck_p2, winner):
    card_p1 = deck_p1.popleft()
    card_p2 = deck_p2.popleft()

    if winner == 'P1':
        deck_p1.append(card_p1)
        deck_p1.append(card_p2)
    
    else:
        deck_p2.append(card_p2)
        deck_p2.append(card_p1)
    
    return deck_p1, deck_p2

#function to play crab combat and output the winner and both final decks
def play(deck_p1, deck_p2):

    decks_seen = set()

    while True:

        len1 = len(deck_p1)
        len2 = len(deck_p2)

        try:
            card1 = deck_p1[0]
            card2 = deck_p2[0]
        except IndexError:
            pass
        
        if len1 == 0: #if P1's deck is empty, P2 wins
            return 'P2', deck_p1, deck_p2

        elif len2 == 0: #if P2's deck is empty, P2 wins
            return 'P1', deck_p1, deck_p2
        
        elif len1 - 1 < card1 or len2 - 1 < card2:
            #if at least one player doesn't have enough cards to recurse
            #then we play the round normally
            dtup = (tuple(deck_p1), tuple(deck_p2)) #current configuration as a tuple of tuples
            if dtup in decks_seen:
                #if the configuration has been seen before in this game
                #P1 wins, per the rules
                return 'P1', deck_p1, deck_p2

            else:
                decks_seen.add(dtup) #add the current configuration to decks_seen
            
                if card1 > card2:
                    #P1 wins the round
                    deck_p1, deck_p2 = win(deck_p1, deck_p2, 'P1')
                
                else:
                    #P2 wins the round
                    deck_p1, deck_p2 = win(deck_p1, deck_p2, 'P2')

        else:
            #both players have enough cards to recurse
            #so we recurse!
            new_deck_p1 = collections.deque(list(deck_p1)[1:card1 + 1])
            new_deck_p2 = collections.deque(list(deck_p2)[1:card2 + 1])
            winner, _, _ = play(new_deck_p1, new_deck_p2)

            
            deck_p1, deck_p2 = win(deck_p1, deck_p2, winner)
    
    return winner, deck_p1, deck_p2

#(C) Calculate the Puzzle Answer

winner, deck_p1, deck_p2 = play(deck_p1,deck_p2)

final_deck = deck_p1

if winner == 'P2':
    final_deck = deck_p2
    
points = reversed(range(1,len(final_deck)+1))

score = sum([a*b for a,b in zip(final_deck,points)])
    
print(score)
