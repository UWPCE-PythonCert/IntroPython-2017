# contexttest.py
# This script looks through files and adds a file using contextmanagers
import os
from contextlib import contextmanager

crudlist = []


@contextmanager
def place_file(target):
    print("Attempting to Place Packet")
    try:
        cwd = os.getcwd()
        os.chdir(target)
        yield
    finally:
        os.chdir(cwd)


currentloc = os.getcwd()
print(currentloc)
print()
print()
with place_file('/Users/Kuchan/Documents/TestDirDir/TargetDir'):
    crudlist = os.listdir()
    for i in range(0, 35):
        filename = "DanRocks" + str(i) + ".txt"
        with open(filename, 'w+') as packet:
            packet.write("Dan Definitely Rocks")
    for i in crudlist:
        if os.path.isfile()
print(crudlist)
print('File Placed')
