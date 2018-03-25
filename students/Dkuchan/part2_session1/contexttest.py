# contexttest.py
# This script looks through files and adds a file using contextmanagers
import os
from contextlib import contextmanager

crudlist = []
refinedlist = []
targetlist = []

inittarget = '/Users/Kuchan/Documents/TestDirDir/TargetDir'
@contextmanager
def place_file(target):
    print("Attempting to Place Packet")
    try:
        cwd = os.getcwd()
        os.chdir(target)
        yield
    finally:
        os.chdir(cwd)


def mapdrives(depth):
    ''' This function maps drives and
    returns a list of paths for file placement.
    '''
    for i in range(1, depth):
        crudlist = [os.listdir(x) for x in targetlist]
        refinedlist = [x for x in crudlist if '.' not in x]
        targetlist = [inittarget + '/' + str(x) for x in refinedlist if inittarget + '/' + str(x) not in x]



def findinittarget():
    '''This is supposed to navigate to the initial target drive.
    '''
   # initdir = os.chdir('C:\') #for windows
   # initdir = os.chdir('/Users') #for mac

   targetlist.append(initialtarget)


currentloc = os.getcwd()
print(currentloc)
print()
print()
with place_file(inittarget):
    
    
'''


    for i in range(0, 35):
        filename = "DanRocks" + str(i) + ".txt"
        with open(filename, 'w+') as packet:
            packet.write("Dan Definitely Rocks")
#    for i in crudlist:
 #       if os.path.isfile():
'''
print(crudlist)
print(refinedlist)
print(targetlist)
print('File Placed')
