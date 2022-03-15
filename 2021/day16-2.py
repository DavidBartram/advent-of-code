import sys
import binascii
import math


class Message:
    def __init__(self, file):
        hex_data = file.read().strip()

        #convert transmission from hexadecimal to binary
        bin_data = binascii.a2b_hex(hex_data)
        
        #pos is an integer attribute representing the current position of the parser in parsing the message
        self.pos = 0

        #bits is a string attribute containing the bits in the message
        self.bits = ''

        #add the bits from the input file into the bits attribute of the Message object
        for byte in bin_data:
            self.bits += '{:08b}'.format(byte)
    
    def integer_value(self, n_bits):
        #returns the integer value, in decimal, of the next n_bits bits of the message

        #convert to decimal and store as int
        result = int(self.bits[self.pos:self.pos+n_bits], 2)
        #advance the position
        self.pos += n_bits
        return result
    
    def parse_one_packet(self):
        #parse the next packet of the message
        #return the packet as a tuple of (packet version, type id, packet content)
        #content is either a decimal integer (for literal value packets), or a list of subpackets (for operator packets)
        version = self.integer_value(3)
        id = self.integer_value(3)
        content = self.read_packet_content(id)
        return (version, id, content)

    def read_packet_content(self,id):
        #interpret the contents of a packet
        if id == 4: #the packet is a literal value, return the decimal integer value
            val = ''
            go = 1
            while go == 1:
                go = self.integer_value(1)
                val += "{:04b}".format(self.integer_value(4))

            return int(val,2)

        else: #the packet is an operator packet, return a list of subpackets
            length_type = self.integer_value(1)

            if length_type == 1: #the next 11 binary digits give the number of subpackets
                n_packets = self.integer_value(11)

                return [self.parse_one_packet() for _ in range(n_packets)]
            
            if length_type == 0: #the next 15 binary digits give the total number of bits in the subpackets
                x = self.integer_value(15) #need to do this on a separate line as it changes self.pos
                end = self.pos + x #end = self.pos + self.integer_value(15) one one line would be bad as it would depend on the order that pos and integer_value are evaluated
                output=[]
                while self.pos < end: #parse packets until the end position is reached
                    output.append(self.parse_one_packet())

                return output

def apply_operators(packet):
    #recursive function to calculate the value of a packet (which may contain more packets, which may contain more packets etc.)
    (version, id, content) = packet

    if id==0: #sum packet, calculates the sum of all subpackets
        total = 0
        for subpacket in content:
            total += apply_operators(subpacket)
        return total

    if id==1: #product packet, calculates the product of all subpackets
        total = 1
        for subpacket in content:
            total = total * apply_operators(subpacket)
        return total

    if id == 2: #minimum packet, calculates the minimum value of all subpackets
        total = math.inf
        for subpacket in content:
            val = apply_operators(subpacket)
            if val<total:
                total = val
        return total

    if id == 3: #maximum packet, calculates the maximum value of all subpackets
        total = -math.inf
        for subpacket in content:
            val = apply_operators(subpacket)
            if val>total:
                total = val
        return total

    if id==4: #literal value packet, the value in content is the integer the packet represents
        total = content
        return total

    if id==5: # > packet. contains exactly two subpackets, if the first has a value greater than the second, return 1. Otherwise return 0.
        total = 0
        if apply_operators(content[0]) > apply_operators(content[1]):
            total = 1
        return total
    
    if id==6: # < packet. contains exactly two subpackets, if the first has a value less than the second, return 1. Otherwise return 0.
        total = 0
        if apply_operators(content[0]) < apply_operators(content[1]):
            total = 1
        return total

    if id==7: # == packet. contains exactly two subpackets, if the first has a value equal to the second, return 1. Otherwise return 0.
        total = 0
        if apply_operators(content[0]) == apply_operators(content[1]):
            total = 1
        return total
    

#initialise a Message object from the input file
with open(sys.argv[1]) as file:
    message = Message(file)

#parse the outer packet of the message into a tuple of (version number, type ID, content)
packet = message.parse_one_packet()

#calculate the value of the outer packet of the message
print(apply_operators(packet))



