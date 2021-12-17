import sys
import binascii


class Message:
    def __init__(self, file):
        hex_data = file.read().strip()
        print(hex_data)

        bin_data = binascii.a2b_hex(hex_data)
        #bin_data = bytes.fromhex(hex_data)

        self.pos = 0
        self.bits = ''

        for byte in bin_data:
            self.bits += '{:08b}'.format(byte)
    
    def integer_value(self, n_bits):
        result = int(self.bits[self.pos:self.pos+n_bits], 2)
        self.pos += n_bits
        return result
    
    def parse_one_packet(self):
        version = self.integer_value(3)
        id = self.integer_value(3)
        data = self.read_packet_data(id)
        return (version, id, data)

    def read_packet_data(self,id):
        if id == 4:
            val = ''
            go = 1
            while go == 1:
                go = self.integer_value(1)
                val += "{:08b}".format(self.integer_value(4))

            return int(val,2)

        else:
            length_type = self.integer_value(1)

            if length_type == 1:
                n_packets = self.integer_value(11)

                return [self.parse_one_packet() for _ in range(n_packets)]
            
            if length_type == 0:
                x = self.integer_value(15) ##need to do this separately as it changes self.pos
                end = self.pos + x #end = self.pos + self.integer_value(15) would be bad as it would depend on the order that pos and integer_value are evaluated
                output=[]
                while self.pos < end:
                    output.append(self.parse_one_packet())

                return output

def sum_versions(packet, vsum=0):
    (version, id, data) = packet

    if id==4:
        vsum += version
        return vsum

    else:
        vsum += version
        for subpacket in data:
            vsum = sum_versions(subpacket,vsum)
        return vsum

def apply_operators(packet):
    (version, id, data) = packet

    if id==0:
        total = 0
        for subpacket in data:
            total += apply_operators(subpacket)
        return total

    if id==1:
        total = 1
        for subpacket in data:
            total = total * apply_operators(subpacket)
        return total

    if id == 2:
        total = apply_operators(data[0])
        for subpacket in data[1:]:
            val = apply_operators(subpacket)
            if val<total:
                total = val
        return total

    if id == 3:
        total = apply_operators(data[0])
        for subpacket in data[1:]:
            val = apply_operators(subpacket)
            if val>total:
                total = val
        return total

    if id==4:
        total = data
        return total

    if id==5:
        total = 0
        if apply_operators(data[0]) > apply_operators(data[1]):
            total = 1
        return total
    
    if id==6:
        total = 1
        if apply_operators(data[0]) > apply_operators(data[1]):
            total = 0
        return total

    if id==7:
        total = 0
        if apply_operators(data[0]) == apply_operators(data[1]):
            total = 1
        return total
    
    

    
with open(sys.argv[1]) as file:
    message = Message(file)

packet = message.parse_one_packet()

print(packet)

print(apply_operators(packet))



