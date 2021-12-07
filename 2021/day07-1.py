import sys
from statistics import median

with open(sys.argv[1]) as file:
    data = file.read().split(',')
    data = [int(val) for val in data]

def sum_fuel_costs(positions, x):
    sum = 0
    for position in positions:
        sum += abs(position - x)
    
    return int(sum)

min_cost = sum_fuel_costs(data,0)

#brute force solution
for x in range(min(data),max(data)):
    cost = sum_fuel_costs(data,x)
    if cost < min_cost:
        min_cost = cost

print(min_cost)
