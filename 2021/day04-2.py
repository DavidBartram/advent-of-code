import sys

with open(sys.argv[1]) as file:
    data = file.read().split('\n\n')

    win_nums = data[0].split(',')

    grids = [x.split('\n') for x in data[1:]]

    newgrids = []

    for grid in grids:
        stripped_grid = [x.strip() for x in grid]
        newgrids.append([x.replace('  ', ' ').split(' ') for x in stripped_grid])
        
    
    grids = newgrids

    grids[-1].remove([''])

    transposed_grids = []
    for grid in grids:
        transposed_grids.append(list(map(list, zip(*grid))))

def check(card,nums):
    for row in card:
        if set(row).issubset(set(nums)):
            return True

def score(card,nums):
    flat_card = set([val for row in card for val in row])
    scores = flat_card - set(nums)
    scores = [int(score) for score in scores]
    return sum(scores)

def part2_play(cards,transposed_cards, nums):

    nums_so_far = []
    remaining_cards = list(range(len(cards)))

    for num in nums:

        nums_so_far.append(num)
        for i in remaining_cards:
            if check(cards[i],nums_so_far) == True or check(transposed_cards[i],nums_so_far) == True :
                if i in remaining_cards:
                    remaining_cards.remove(i)

                    if len(remaining_cards) ==0:
                        final_card = cards[i]
                        return score(final_card,nums_so_far)*int(num)                
        

        


print(part2_play(grids,transposed_grids,win_nums))

