#!/usr/bin/env python3

import ntpath
import os


src = "/Users/achudasm/IntroPython-2017/students/Amit/Session04/IMG_5053.jpg"
src_file_dir, src_file_name = ntpath.split(src)
dst = "/Users/achudasm/IntroPython-2017/students/Amit/Session04"

dst = os.path.join(dst, "copy_{}".format(src_file_name))

print(dst)


chunk = 130
with open(src, 'rb') as input, open(dst, 'wb') as output:
    while True:
        data = input.read(chunk)
        if not data:
            break
        output.write(data)




