#!/usr/bin/env python3
import os

my_path = os.path.abspath(__file__)
proj_dir = "/".join(my_path.split("/")[:-4])
text_file_path = os.path.join(proj_dir, "examples", "Session01", "students.txt")

languages = set()
with open(text_file_path) as students:
    for line in students:
        try:
            langs = line.strip().split(":")[1].replace(" ","").split(",")
            if langs[0].strip()[0].isupper():
                langs = langs[1:]
            for lang in langs:
                if len(lang) > 0:
                    languages.add(lang)
        except IndexError:
            print("WARN: No languages listed for line" \
                  "'{}'".format(line.strip()))

print(languages)
