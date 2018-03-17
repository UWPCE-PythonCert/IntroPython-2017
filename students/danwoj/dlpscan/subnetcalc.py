ip_addr = '192.168.36.133'
subnet_mask = '255.255.255.0'

def ip_oct_bin(input):
# This function takes the octet list and turns those octet 
# values into their binary form, maintaining a list.
    bin_octet = []
    for i in input:
        bin_val = bin(int(i))[2:]
        # This condition tests to ensure each binary octet has
        # eight characters, if not, it will pad the value
        if (len(bin_val) < 8):
            zeros = 8 - len(bin_val)
            for i in range(zeros):
                bin_val = '0' + bin_val
        bin_octet.append(bin_val)
    return bin_octet

def sn_calculation(ipa_value, snm_value):
# This function takes the binary lists of both the subnet mask
# and the IP address and returns the subnet in CIDR notation
    cidr = 0
    bin_subnet_address = []
    final_subnet_address = ''
    octets = ['','','','']
    dec_octets = ['','','','']
    for i in range(4):
        for inum, snum in zip(ipa_value[i], snm_value[i]):
            if snum == '1':
                cidr += 1
                bin_subnet_address.append(inum)
                octets[i] += inum
            else:
                bin_subnet_address.append('0')
                octets[i] += '0'
            dec_octets[i] = int(octets[i], 2)
        final_subnet_address += str(dec_octets[i])
        if i < 3:
            final_subnet_address += '.'
    final_subnet_address += '/'
    final_subnet_address += str(cidr)
    return final_subnet_address

def subnet_calculator(ip_addr, subnet_mask):
# This function calculates a network subnet based on a valid IP 
# address and its subnet mask

    # These two lines take the IP address and subnet mask strings 
    # and turn them into an int list of octet values
    ip_addr_list = ip_addr.split('.')
    subnet_mask_list = subnet_mask.split('.')
    # This converts the IP address into binary form
    ipa_compare = ip_oct_bin(ip_addr_list)
    # This converts the subnet mask into binary form
    snm_compare = ip_oct_bin(subnet_mask_list)
    # This takes the two binary values and calculates the subnet
    subnet = sn_calculation(ipa_compare, snm_compare)
    return subnet

value = subnet_calculator(ip_addr, subnet_mask)

print('This is the final subnet: ', value)