"""
Kathryn Egan

Prints the absolute path to each file in the cwd.
"""
import os


for f in os.listdir('.'):
    if os.path.isdir(f):
        continue
    print os.path.abspath(f)
