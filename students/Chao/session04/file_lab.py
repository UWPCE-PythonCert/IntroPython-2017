#!/usr/bin/env python

import os

def pdir():
    """ Write a program which prints the full path to all files in the current directory, one per line """
   
    for f in os.listdir('.'):
        # Check if item is a file (not a directory)
        if os.path.isfile(f):
            print(f)

def copyf(inputf, outputf):
    """ Write a program which copies a file from a source, to a destination """

    with open(inputf,'rb') as f_in, open(outputf,'wb') as f_out:
        while True:
            # Read to buffer, 1 byte at a time
            buf = f_in.read(1)
            if buf:
                f_out.write(buf)
            else:
                break

#def langlist():

#    with open(inputf,'r') as slist:


# infile = "students.txt"

# with open(infile) as students:
#     students.readlines()


if __name__ == '__main__':
    pdir()
    copyf('students.txt', 'students_backup.txt')
    copyf('spongebob.jpg', 'spongebob_backup.jpg')