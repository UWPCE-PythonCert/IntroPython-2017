#!/usr/bin/env python

from paramiko import client

class ssh:
    client = None

    def __init__(self, address, username, password):
        # Let the user know we're connecting to the server
        print("Connecting to server.")
        # Create a new SSH client
        self.client = client.SSHClient()
        # The following line is required if you want the script to be able to access a server that's not yet in the known_hosts file
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        # Make the connection
        self.client.connect(address, username=username, password=password, look_for_keys=False)

    def sendCommand(self, command):
        # Check if connection is made previously
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
#            stdout.channel.setblocking(0)
            while not stdout.channel.exit_status_ready():
                # Print stdout data when available
                if stdout.channel.recv_ready():
                    # Retrieve the first 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve the next 1024 bytes
                        alldata += stdout.channel.recv(1024)

                    # Print as string with utf8 encoding
                    print(alldata)
#                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")

def mainloop():

    ip_address = '192.168.36.131'

    connection = ssh(ip_address, "dlpscan.svc", "L!ghtning26")
    connection.sendCommand("ifconfig | grep -o 'inet '{}".format(ip_address))
    connection.sendCommand('ls')

if __name__ == '__main__':
    mainloop()