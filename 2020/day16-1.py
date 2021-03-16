import sys
import re

with open(sys.argv[1]) as file:
    notes = file.read()

field_pattern = r'([a-zA-Z]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'

fields = re.findall(field_pattern, notes)

field_dict = {}

for field in fields:
    values = set()
    a = int(field[1])
    b = int(field[2])+1
    values = values.union(set(range(a,b)))

    c = int(field[3])
    d = int(field[4])+1

    values = values.union(set(range(c,d)))

    field_dict[field[0]] = values

all_valid_values = set()

for field, values in field_dict.items():
    all_valid_values = all_valid_values.union(values)

my_ticket_pattern = r'your ticket:\n(.+)'

my_ticket = re.findall(my_ticket_pattern, notes)

tickets_pattern = r'(?:nearby tickets:)(\n(?:.+\n)+)'

tickets = re.findall(tickets_pattern, notes)[0]

tickets = re.split('\n', tickets)

tickets = [x for x in tickets if x]

tickets = [x.split(',') for x in tickets]

invalid_nums = []

for ticket in tickets:
    allvalid = False
    for num in ticket:
        num = int(num)
        if num not in all_valid_values:
            invalid_nums.append(num)
        

print(sum(invalid_nums))

print(tickets)
