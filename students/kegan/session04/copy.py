"""
Kathryn Egan

Copies a file of any size from one location to another
without reading into memory
"""
import os

source_dir = 'InDir'
dest_dir = 'OutDir'
file = 'test_pic.jpg'  # 5 MB
# file = 'Skydive.mov'  # 2.5 GB

with open(os.path.join(source_dir, file), 'rb') as fin, \
        open(os.path.join(dest_dir, file), 'wb') as fout:
    block = fin.read(1024)
    while block:
        fout.write(block)
        block = fin.read(1024)
