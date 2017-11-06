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



def langlist():
    """ From students.txt, generates a list of all the languages that have been used, and how many students on each language """

    # Create a empty dictionary
    langcount = {}

    with open('students.txt','r') as slist:
        slist.readline()
        for line in slist:
            langonly = line.split(':')[1].strip()
            # Remove empty entries
            if langonly:
                langsplit = langonly.split(',')
                for lang in langsplit:
                    # split the individual language, and again, make sure no empty entries
                    if lang and lang.split()[0].islower():
                        lang = lang.split()[0]
                        # If language is new in dict, put 1 as value
                        if lang not in langcount:
                            langcount[lang] = 1
                        # If language is not new, value + 1
                        else:
                            langcount[lang] += 1
                        #print(lang)
    print(langcount)


if __name__ == '__main__':
    """ Main function """

    pdir()
    # Test copy for both text and binary files
    copyf('students.txt', 'students_backup.txt')
    copyf('spongebob.jpg', 'spongebob_backup.jpg')
    langlist()
