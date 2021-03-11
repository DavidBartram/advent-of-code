import sys

initial_nums = [0,3,6] #puzzle input

def play(game,turns):
    past = [0]*turns
    x = game[-1] #when the game begins, this is the most recent number to consider
    i = 1 #this is the turn counter

    #enter the initial numbers (the list "game") into the "past" list
    while i < len(game):
        past[game[i-1]] = i
        i += 1
    
    #take the last number spoken, x, and update it to the next number spoken.
    #while ensuring that past[x] equals the last turn that the number x was spoken.
    while i < turns:
        j = past[x]
        past[x] = i
        
        if j == 0:
            x = 0
        else:
            x = i - j
        
        i += 1
        
    return x

#part 1
print(play(initial_nums,2020))


#part 2
print(play(initial_nums,30000000))
