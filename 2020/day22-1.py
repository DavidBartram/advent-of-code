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

#(B) Play Crab Combat!

def play(decks):

    deck_p1 = decks[0] #Player 1's deck
    deck_p2 = decks[1] #Player 2's deck

    while len(deck_p1) > 0 and len(deck_p2) > 0:
        card_p1 = deck_p1.popleft()
        card_p2 = deck_p2.popleft()
        
        if card_p1 > card_p2:
            deck_p1.append(card_p1)
            deck_p1.append(card_p2)
        
        if card_p1 < card_p2:
            deck_p2.append(card_p2)
            deck_p2.append(card_p1)

    final_deck = deck_p1 #Let P1 win by default

    if len(deck_p1) == 0:
        #if P2 actually won, change the winning deck to P2's deck
        final_deck = deck_p2
    
    #calculate points according to the scoring system
    points = reversed(range(1,len(final_deck)+1))

    score = sum([a*b for a,b in zip(final_deck,points)])
    
    return score

#(C) Find and print the Puzzle Answer
print(play(decks))
