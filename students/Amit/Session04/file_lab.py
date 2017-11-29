#!/usr/bin/env python3

import os


current_dir = os.getcwd()
file_list = os.listdir(current_dir)

print("Current working directory:- {}".format(current_dir))
print("-"*60)
print("List of files in the current directory:- {}".format(file_list))
print("-"*60)
print("Below are absolute path for the files")
for file in file_list:
    print(os.path.abspath(file))





