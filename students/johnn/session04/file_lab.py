#!/usr/bin/env python

import os

# list files in current directory
cur_dir=os.getcwd()
files=os.listdir(cur_dir)
for file in files:
    print(os.path.join(cur_dir,file))

# copy arbitrary file content
in_data = open("file.input", "rb")
out_data = open("file.output", "wb")
blob_size=4096
print("copying file",end="")
while True:
    blob = in_data.read(blob_size)
    if not blob:
        break
    print(".",end="")
    out_data.write(blob)
print("\n")
in_data.close()
out_data.close()

