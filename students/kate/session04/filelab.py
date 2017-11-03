#!/usr/bin/env python3

"""
path lab, parse students.txt
"""
# file = "kmarguerite/MontyPython/IntroPython-2017/examples/Session01/students.txt"
file = "students.txt"

all_langs = []
with open(file) as students:
    students.readline()
    for line in students:
    # go to file and read line by line using for loop
        line = line.strip()
        langs = line.split(":")[1].split(",")
        if langs[0].strip()[0].isupper():
            langs = langs[1:]
        all_langs.extend(langs)
        # print(langs)

new_langs = [lang.strip() for lang in all_langs if lang.strip()]
all_langs = set(all_langs)

# display new text on screen, write new file to save text
print("Here are all the langs!")
print(all_langs)
x = open("langs.txt", "w+")
x.write(" ".join(all_langs))
