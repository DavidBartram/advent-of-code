position = {1:7, 2:5}
score = {1:0, 2:0}

def play_one_round(n):
    
    die = [3*n-2, 3*n-1, 3*n]

    die = [(x-1)%100 + 1 for x in die]

    player = (n-1)%2 + 1

    space = (position[player] + sum(die) -1)%10 + 1
    position[player] = space
    score[player] += space


def play():

    n = 1

    while True:
        play_one_round(n)
        #print(n, position, score)
        if max(score.values()) >= 1000:
            return min(score.values())*n*3
        n += 1



print(play())


