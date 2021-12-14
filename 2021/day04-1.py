import sys

with open(sys.argv[1]) as file:
    data = file.read().split('\n\n')

    win_nums = data[0].split(',')

    grids = [x.split('\n') for x in data[1:]]

    grids = [[x.strip().replace('  ', ' ').split(' ') for x in grid] for grid in grids]

    grids[-1].remove(['']) #remove unwanted element created at end of file

    #append columns to each grid as if they were additional rows
    grids = [grid + [[row[i] for row in grid] for i in range(len(grid))] for grid in grids] 

def check(card,nums):
    for row in card:
        if set(row).issubset(set(nums)):
            return True

def score(card,nums):
    nums_on_card = set([val for row in card[:5] for val in row])
    scores = nums_on_card - set(nums)
    total = sum([int(score) for score in scores])
    return total

def play(cards,nums):

    nums_so_far = []

    for num in nums:
        nums_so_far.append(num)
        for card in cards:
            if check(card,nums_so_far) == True:
                return score(card,nums_so_far)*int(num)

print(play(grids,win_nums))




