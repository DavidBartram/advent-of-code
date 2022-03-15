import sys

with open(sys.argv[1]) as file:
    data = file.readlines()

dots = set()

folds = []

for line in data:

    if ',' in line:
        #populate a set of tuples (x,y) with the coordinates of each dot on the paper
        #because it is a set, any dot that exactly overlaps with a previous dot will be ignored
        line = line.rstrip('\n').split(",")
        dots.add((int(line[0]), int(line[1])))
    
    if '=' in line:
        #populate a list of fold instructions, for example ('x',100) would mean fold along the line x=100
        line = line.rstrip('\n').replace('fold along ','').split("=") 
        folds.append((line[0],int(line[1])))

def perform_fold(dots,fold):

    newdots = dots.copy()

    if fold[0] == 'x':
        #perform a fold along a vertical line x=fold[1]
        for (x,y) in dots:
            if x > fold[1]:
                newdots.remove((x,y))
                newdots.add((2*fold[1]-x,y))
    
    if fold[0] == 'y':
            #perform a fold on a horizontal line y=fold[1]
            for (x,y) in dots:
                if y > fold[1]:
                    newdots.remove((x,y))
                    newdots.add((x,2*fold[1]-y))

    return newdots

def final_dots(dots, folds):
    #perform all the folds in the input
    for fold in folds:
        dots = perform_fold(dots,fold)

    return dots

def print_dots(dots):
    #print the final pattern of dots so that the puzzle solution
    #can ber read from 
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

print(' ')
print_dots(end_state)


