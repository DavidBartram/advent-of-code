def findsize(subject, transformed):
    #find the loop size by brute force
    i = 1
    while i < 100000000:
        #python's built-in pow function calculates modular exponentiation
        if pow(subject, i, 20201227) == transformed:
            return i
        else:
            i += 1

subject = 7  #initial value, fixed in the puzzle rules
card_key = 5764801 #card's public key from puzzle input

loopsize = findsize(subject,card_key)

door_key = 17807724 #door's public key from puzzle input

print(pow(door_key, loopsize, 20201227))

thehrehththehehehe
    