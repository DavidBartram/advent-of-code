import sys

with open(sys.argv[1]) as file:
    ports = file.read().split("\n\n")

ports = [port.replace("\n"," ") for port in ports]

countvalid = 0

fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

valid = True

for port in ports:
    print(port)
    for field in fields:
        if field not in port:
            valid = False
        print("valid:",valid)


    if valid == True:
        countvalid += 1
    
    elif valid == False:
        valid = True
    
    print("countvalid:", countvalid)



print(countvalid)
