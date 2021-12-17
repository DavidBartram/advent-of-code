import sys


class Message:
    def __init__(self, file):
        hex_data = file.read()
        bin_data = bytes.fromhex(hex_data)

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
                val += format(self.integer_value(4),'04b')

            return int(val,2)

        else:
            length_type = self.integer_value(1)

            if length_type == 1:
                n_packets = self.integer_value(11)
                output = []
                for _ in range(n_packets):
                    output.append(self.parse_one_packet())

                return output
            
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

with open(sys.argv[1]) as file:
    message = Message(file)

packet = message.parse_one_packet()

print(sum_versions(packet))

