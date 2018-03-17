#!/usr/bin/env python
import winrm
from pexpect import pxssh

s = pxssh.pxssh()

if not s.login ('192.168.36.131', 'dlpscan.svc', 'L!ghtning26'):
    print("SSH session failed on login.")
    print(str(s))
else:
    print("SSH session login successful")
#    s.send("grep -H -o '[0-9]\{16\}' *.txt\n")
    s.send("cd / | grep -r --include='*.txt' -o '[0-9]\{16\}' ${PWD}\n")
#    s.sendline ('find / | grep *.h')
    s.prompt()         # match the prompt
    print(str(s.before, "utf8"))
#    print(s.before)     # print everything before the prompt.
    s.logout()

#s.sendline

#username='MALUM8\dlpscanwin.svc'
#password='L!ghtining26666'

#s = winrm.Session('http://192.168.36.207:5985/wsman', auth=(username, password))
#r = s.run_cmd('ipconfig', ['/all'])

#print(r.status_code)
#print(r.std_out)