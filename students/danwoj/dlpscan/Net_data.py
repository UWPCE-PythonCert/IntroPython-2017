#!/usr/bin/env python
import winrm, os, socket
import subprocess as sub

class Net_data:
    def __init__(self):
        self.ip
        self.subnet

    def ip(self):
        ip = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]

        return ip

    def subnet(self):
        Popen_command = ''
        subnet = sub.Popen("ifconfig | grep {} | awk -F 'Mask:' '{{print $2}}'".format(self.ip()), stdout = sub.PIPE, shell = True)
        (output, err) = subnet.communicate()
        subnet = (str(output, "utf8").split("\n")).pop(0)

        return subnet

x = Net_data()

print(x.ip())
print(x.subnet())