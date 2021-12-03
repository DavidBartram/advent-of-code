import sys

with open(sys.argv[1]) as file:
    values = file.read().splitlines()
    newvalues = []
    for value in values:
        newvalues.append(list(value))
    values = newvalues

columns = [[int(values[j][i]) for j in range(len(values))] for i in range(len(values[0]))]

averages = ''

flipped = ''

for column in columns:
    average_bit = int(round(sum(column)/len(column)))
    averages += str(average_bit)
    if average_bit == 1:
        flipped += '0'
    else:
        flipped += '1'

values = [''.join(value) for value in values]

def get_rating(comparator, numbers, i):
        if len(numbers) == 1:
            return numbers[0]
        
        else:
            filtered = []
            for number in numbers:
                if number[i] == comparator[i]:
                    filtered.append(number)
            numbers = filtered
            
            return get_rating(comparator, numbers, i+1)

print(int(get_rating(averages, values, 0),2))
print(int(get_rating(flipped, values, 0),2))





