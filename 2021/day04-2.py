import sys

with open(sys.argv[1]) as file:
    data = file.read().split('\n\n')

    win_nums = data[0].split(',')

    grids = [x.split('\n') for x in data[1:]]

    grids = [[x.strip().replace('  ', ' ').split(' ') for x in grid] for grid in grids]

    grids[-1].remove([''])

#append columns to each grid as if they were additional rows
grids = [grid + [[row[i] for row in grid] for i in range(len(grid))] for grid in grids] 

def check(card,nums):
    for row in card:
        if set(row).issubset(set(nums)):
            return True

def score(card,nums):
    nums_on_card = set([val for row in card for val in row])
    scores = nums_on_card - set(nums)
    total = sum([int(score) for score in scores])
    return total

def part2_play(cards,nums):

    nums_so_far = []

    #list of indices of cards still in play
    # e.g. if cards[3] is still in play, then 3 will be in remaining_cards
    remaining_cards = list(range(len(cards)))

    for num in nums:
        nums_so_far.append(num)

        for i in remaining_cards:
            
            if check(cards[i],nums_so_far) == True:
                remaining_cards.remove(i)

                if len(remaining_cards) ==0:
                    final_card = cards[i]
                    return score(final_card,nums_so_far)*int(num)                
        

        


print(part2_play(grids,win_nums))

