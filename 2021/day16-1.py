

from math import remainder


def parseLiteralValue(word, value='', consumed=0):

    if word[0] == '0':
        consumed += 5
        value += (word[1:5])
        word = word[5:]
        return value, consumed
    
    else:
        consumed += 5
        value += (word[1:5])
        word = word[5:]
        value, consumed = parseLiteralValue(word, value, consumed)
        return value, consumed

def parseLiteralPacket(word):

    value, consumed = parseLiteralValue(word)

    value = int(value,2)

    print('literal value ', value)

    return value, consumed

def parseOperatorPacket(word, consumed=0):

    length_type = word[0]
    word = word[1:]
    consumed += 1
    print('length_type', length_type)

    if length_type == '0':
        n_bits = int(word[:15],2)
        word = word[15:]
        consumed += 15

        more_consumed = 0
        while more_consumed < n_bits:
            x = parseAnyPacket(word)
            word = word[x:]
            more_consumed += x
            

        consumed += more_consumed

    else:
        n_packets = int(word[:11],2)
        word = word[11:]
        consumed += 11
        
        more_consumed = 0
        packets = 0
        while packets < n_packets:
            x = parseAnyPacket(word)
            word = word[x:]
            more_consumed += x
            packets += 1

        consumed += more_consumed

    return consumed


def parseAnyPacket(word, consumed=0):

    if len(word) <= 7:
        return consumed

    version = int(word[:3],2)
    print('version', version)
    word = word[3:]
    consumed +=3
    id = int(word[:3],2)
    print('id',id)
    word = word[3:]
    consumed += 3

    if id == 4:
        val,x = parseLiteralPacket(word)
        word = word[x:]
        consumed += x
    
    else:
        x = parseOperatorPacket(word)
        word = word[x:]
        consumed += x

    return consumed




parseAnyPacket('110100101111111000101000')

print('++++++++++')

parseAnyPacket('00111000000000000110111101000101001010010001001000000000')

print('++++++++++')

parseAnyPacket('11101110000000001101010000001100100000100011000001100000')


print('++++++++++')

parseAnyPacket("{0:08b}".format(int('8A004A801A8002F478', 16)))

print('++++++++++')

parseAnyPacket("{0:08b}".format(int('620080001611562C8802118E34', 16)))

