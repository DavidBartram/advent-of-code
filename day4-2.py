import sys
import re

with open(sys.argv[1]) as file:
    ports = file.read().split('\n\n')

ports = [re.findall(r'\S*:\S*', port) for port in ports]

countvalid = 0

req = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}

for port in ports:

    portvalid = True
    present = set()

    for field in port:
        valid = True
        present.add(field[:3])
        x = field.partition(':')[2]

        if field.startswith('byr'):
            valid = 1920 <= int(x) <= 2002

        elif field.startswith('iyr'):
            x = int(x)

            valid = 2010 <= int(x) <= 2020

        elif field.startswith('eyr'):
            valid = 2020 <= int(x) <= 2030

        elif field.startswith('hgt'):
            
            if field.endswith('cm'):
                x = x.replace('cm', '')
                valid = 150 <= int(x) <= 193
            
            elif field.endswith('in'):
                x = x.replace('in', '')
                valid = 59 <= int(x) <= 76
            
            else:
                valid = False

        elif field.startswith('hcl'):
            valid = bool(re.fullmatch(r'#[0-9a-f]{6}', x))

        elif field.startswith('ecl'):
            valid = bool(re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', x))

        elif field.startswith('pid'):
            valid = bool(re.fullmatch(r'[0-9]{9}', x))

        portvalid = portvalid and valid
        #print(field, valid)

    present.discard('cid')
    if present != req:
        portvalid = False

    if portvalid:
        countvalid += 1

print(countvalid)
