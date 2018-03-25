''' The intent behind this program was originally to create a way to perform an automated digital loss prevention (DLP) scanner
that could log on to machines in a network and scan the file system for any type of sensitive data they wasn't supppsed to be there. 
As I'm sure with other projects, this got to be a little ambitious and I wasn't able to complete that part. What I was able to accomplish 
was to create a program that, on ititialization, was able to make some determination of itself (e.g. what's my IP, what network am I on) 
and through several menu options perform a network discovery scan for other systems. I also got the Linux SSH function to work but didn't 
quite resolve the Windows RM issue. Had I had more time, I was also experimenting with PyNaCl to appropriate input and store my credentials 
I'd use to perform the remote login and save these passwords in an encrypted 'shadow' file. I found some success with this in iPython but it 
would have taken a lot more time to implement it here '''

#!/usr/bin/env python
import winrm, os, socket, csv, nacl.pwhash
import subprocess as sub
from pexpect import pxssh

s = pxssh.pxssh(timeout=60)
password = 'L!ghtning26'
account = 'dlpscan.svc'
ip_range_list = []

''' The next three functions are all related to my subnet calculator
the first one is used to convert the decimal IP octet values into binary, 
the second performs the actual binary subnet calculation and 
returns the final product, and the third function is the main 
function that is called by the rest of the program and binds 
the whole process together. Currently my program only supports 
IPv4 so let's not tell the IETF about this!  '''

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
# As I look at the next three variables I feel like I'm sort of 
# cheating by defining these empty values like this and setting 
# my range below that to four but I was in a pinch 
# and it seemed to work so ¯\_(ツ)_/¯.
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

class Net_data:
# This class defines the network data (IP, subnet mask, and default gateway) for the host running the application
    def __init__(self):
        self.ip
        self.subnet
        self.gateway

    def ip(self):
        ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

        return ip

    def subnet(self):
        Popen_command = ''
        subnet = sub.Popen("ifconfig | grep {} | awk -F 'Mask:' '{{print $2}}'".format(self.ip()), stdout = sub.PIPE, shell = True)
        (output, err) = subnet.communicate()
        subnet = (str(output, "utf8").split("\n")).pop(0)

        return subnet

    def gateway(self):
        default_gate = sub.Popen("ip route show | grep default | awk -F ' ' '{print $3}'", stdout = sub.PIPE, shell = True)
        (output, err) = default_gate.communicate()
        default_gate = (str(output, "utf8").split("\n")).pop(0)

        return default_gate

def sudo(s,password):
#    rootprompt = re.compile('.*[$#]')
#    s.sendline('sudo -s')
#    i = s.expect([rootprompt,'assword.*: '])
    i = s.expect('password')
    if i==1:
        print("Sending Password")
        s.sendline(password)
#    elif i==1:
#        print("sending password")
#        s.sendline(password)
#        j = s.expect([rootprompt,'Sorry, try again'])
#        if j == 0:
#            pass
#        elif j == 1:
#            raise Exception("bad password")
    else:
        raise Exception("unexpected output")
    s.set_unique_prompt

def scanner():
    paths = ['/home', '/usr', '/etc']
    slash16 = '{16\}'
    pwd = '{pwd}'
    path = '/home'
    for i in paths:
        var = r"cd {} && sudo grep -r -o '[0-9]\{}' ${}".format(path, slash16, pwd)
        s.sendline(var)
        s.sendline(password)
        s.prompt()         # match the prompt
        print(str(s.before, "utf8"))
        print('Completed search of {}'.format(i))

def ip_range(range, host_ip, default_gate):
    ip_range = sub.Popen("nmap " + range + " | grep 'Nmap scan report for' | awk -F 'report for' '{print $2}'", stdout = sub.PIPE, shell = True)
    (output, err) = ip_range.communicate()
    ip_range_list = str(output, "utf8").split("\n")
    # The output produces a 'blank' list item at the end so it's removed with a pop
    ip_range_list.pop()
    ip_range_list = [x.strip() for x in ip_range_list]
    print("\nAvailable Targets: ")
    for i in ip_range_list:
        if i == host_ip:
            ip_range_list.remove(host_ip)
        elif i == default_gate:
            print(i, ' (Gateway)')
        else:
            print(i)
    print('\n')
    return ip_range_list

def linux_login(target, account, password):
    if not s.login (target, account, password):
        print('SSH session failed on login.')
        print(str(s))
    else:
        print ('SSH session login successful')

def linux_logout():
    s.logout()
    print ('SSH session logout successful')

def win_login(target, account, password):
    s = winrm.Session('http://192.168.36.207:5985/wsman', auth=(username, password))

# This doesn't work right now
#def linux_active_connections():
# This function shows the IPs this computer has active SSH 
# connections with.
#    active_connections = sub.Popen("sudo netstat -atp | grep 'ESTABLISHED.*ssh ' | awk '{{print $5}}'| sed 's/:ssh//'")
#    (output, err) = subnet.communicate()
#    active_connections = (str(output, "utf8").split("\n")).pop(0)
#    print('Active SSH Connections:')

def target_list_input(target_file):
# This function reads a CSV file input for scan targets 
# and populates the 'targets' list
    targets = []
    f = open(target_file)
    for row in csv.reader(f):
        targets.append(row[0])
    return(targets)

def print_targets(targets):
    if (len(targets) == 0):
        print('No targets identified!')
    else:
        print('{} targets currently identified: '.format(len(targets)))
        i = 1
        for j in targets:
            print('{}: {}'.format(i, j))
            i += 1

def mainloop():

    targets = []
    menu = {'1: Run Scanner': ['Run Scanner'], '2: Discover Targets': ['Discover Targets'], '3: Import Target List': ['Import Target List'], '4: Current Target List': [print_targets(targets)], '5: Quit Program': ['Quit Program'], '6: Linux Login': ['Linux Login'], '7: Linux Logout': ['Linux Logout']}

    while True:

#        if not s.login ('192.168.36.131', account, password):
#            print("SSH session failed on login.")
#            print(str(s))
#        else:
#            print("SSH session login successful")
#    s.sendline("cd / && pwd")f
#    s.sendline("cd / && sudo grep -r --include='*.txt' -o '[0-9]\{16\}' ${PWD}")


        host = Net_data()
        default_net = subnet_calculator(host.ip(), host.subnet())

        print('\n##########################\n#    DLP Scan Program    #\n##########################\n')

        print('Your IP is: ', host.ip())
        print('Your Subnet: ', default_net)
        print('Your Default Gateway: ', host.gateway(), '\n')

        for k, v in menu.items():
            print(k)
#        for i in menu.items():
#            print('%s' % (i))

#       try:
#           m_value = int(input('\nEnter your number choice: '))
#       except ValueError:
 #          print('Input must be an integer, try again.')


        m_value = int(input('\nEnter your number choice: '))
        if m_value == 8:
            value = str(input('\nSetup password: '))
            password_hash(value)
        elif m_value == 7:
#            linux_active_connections()
            linux_logout()
        elif m_value == 6:
            print_targets(targets)
            value = int(input('\nEnter the target you wish to log in to: '))
            value = value - 1
            print('value: ', value)
            print('targets[value]: ', targets[value])
#            target = '192.168.36.131'
            linux_login(targets[value], account, password)
        elif m_value == 5:
            print('\nQuitting Program\n') 
            break
        elif m_value == 4:
            print_targets(targets)
        elif m_value == 3:
            target_file = str(input('\nEnter the name of the target list file (CSV): '))
            targets = target_list_input(target_file)
        elif m_value == 2:
            query = str(input('\nDefault range is {}. Do you want to use this range? (Y/N) '.format(default_net)))
            if (query == 'Y' or query == 'y'):
                targets = ip_range(default_net, host.ip(), host.gateway())
            if (query == 'N' or query == 'n'):
                range = str(input('\nEnter the IP range in CIDR notation: '))
                targets = ip_range(range, host.ip(), host.gateway())
        elif m_value == 1:
            scanner()
        else:
            print('\n! - Please select option 1 thru 6 - !\n')
            print(targets)

#    s.sendline("pwd")
#    sudo(s, password)
#    s.expect('password for {}'.format(account))
#    print('sudo_prompt: ', sudo_prompt) 
#    s.sendline(password)
#    i = s.expect("[sudo] password for")
#    if i == 0:
#        print("Didn't need password")
#        pass
#    elif i == 1:
#        print('I give password')
#        s.sendline(password)
#        j = s.expect([rootprompt,'Sorry, try again'])
#        if j == 0:
#            pass
#        elif j == 1:
#            raise Exception("bad password")
#    else:
#        raise Exception("unexpected output")
#    s.set_unique_promp
#    s.send("grep -H -o '[0-9]\{16\}' *.txt\n")
#    s.sendline("cd / | sudo grep -r --include='*.txt' -o '[0-9]\{16\}' ${PWD}\n")
#    s.send("grep -r -C 2 'discover'")

#    s.sendline ('find / | grep *.h')
#    s.prompt()         # match the prompt
#    print(str(s.before, "utf8"))
#    print(s.before)     # print everything before the prompt.
#    s.logout()

#s.sendline

#username='MALUM8\dlpscanwin.svc'
#password='L!ghtining26666'

#s = winrm.Session('http://192.168.36.207:5985/wsman', auth=(username, password))
#r = s.run_cmd('ipconfig', ['/all'])

#print(r.status_code)
#print(r.std_out)

if __name__ == '__main__':
    mainloop()