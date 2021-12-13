import sys

with open(sys.argv[1]) as file:
    data = file.readlines()

dots = set()

folds = []

for line in data:

    if ',' in line:
        line = line.rstrip('\n').split(",")
        dots.add((int(line[0]), int(line[1])))
    
    if '=' in line:
        line = line.rstrip('\n').replace('fold along ','').split("=") 
        folds.append((line[0],int(line[1])))

def perform_fold(dots,fold):

    newdots = dots.copy()

    if fold[0] == 'x':
        for (x,y) in dots:
            if x > fold[1]:
                newdots.remove((x,y))
                newdots.add((2*fold[1]-x,y))
    
    if fold[0] == 'y':
            for (x,y) in dots:
                if y > fold[1]:
                    newdots.remove((x,y))
                    newdots.add((x,2*fold[1]-y))

    return newdots

def final_dots(dots, folds):
    for fold in folds:
        dots = perform_fold(dots,fold)

    return dots

def print_dots(dots):
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])

    for y in range(max_y+1):
        output = ''

        for x in range(max_x+1):
            if (x,y) in dots:
                output += '█'
            else:
                output += ' '
        
        print(output)

end_state = final_dots(dots,folds)

print_dots(end_state)


