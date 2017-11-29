"""
File LAB (session03)
A bit of practice with files
Goal:

Get a little bit of practice with handling files and parsing simple text.
Paths and File Processing

    1. write a program which prints the full path to all files in the current directory, one per line
    2. write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
        advanced: make it work for any size file: i.e. don’t read the entire contents of the file into memory at once.
        This should work for any kind of file, so you need to open the files in binary mode: open(filename, 'rb')
        (or 'wb' for writing). Note that for binary files, you can’t use readline() – lines don’t have any meaning for binary files.
        Test it with both text and binrary files (maybe jpeg or??)

"""

import os

def fileNames():
    """ Goal 1: prints the full path to all files in the current directory, one per line """
    for name in os.listdir():
        print(os.path.join(os.getcwd(), name))

fileNames()


#TODO: This didn't work. Need to go back
# def copyfileobj_example(source, dest, buffer_size=1024*1024):
#     """
#
#     Copy a file from source to dest. source and dest
#     must be file-like objects, i.e. any object with a read or
#     write method, like for example StringIO.
#     """
#     while 1:
#         copy_buffer = source.read(buffer_size)
#         if not copy_buffer:
#             break
#         dest.write(copy_buffer)
#
# #If you want to copy by filename you could do something like this:
#
# def copyfile_example(source, dest):
#     # Beware, this example does not handle any edge cases!
#     with open(source, 'rb') as src, open(dest, 'wb') as dst:
#         copyfileobj_example(src, dst)

#TODO: Need to create_stego_zip_jpg.py - Hide a zip file inside a JPEG
# def copyFile():
#     """Trying to work on Goal 2, but wasn't too successful"""
#     with open('text20.txt', 'rb') as src, open('text21.txt', 'wb') as dst:
#         jpg_data = src.read()
#         dst.write(jpg_data)




