"""
Week4 Lab3
The file students.txt list I provided contains what programming languages students have used in the past.

Write script that reads that file, generates a list of all the languages that have been used, and display
a table showing how many students specified each language.

"""

#!/usr/bin/env python

infile = "students1.txt"

all_langs = []
with open(infile) as students:
    students.readline() #read one line in the file and throw it away because I haven't assign it to anything.
    for line in students:   #reading each line in file
        line = line.strip()   #stripping white spaces
        langs = line.split(":")[1].split(",")  #split after colon and commas
        if langs[0].strip()[0].isupper():
            langs = langs[1:]
        all_langs.extend(langs)  #collecting all the list

print("Programming Languages:", all_langs)

all_langs2 = all_langs[:]  #copying all_langs for later use

new_langs = []
for lang in all_langs:
    if lang.strip():
        new_langs.append(lang.strip())

all_langs = set(new_langs)
print("\nSet of languages spoken:", all_langs)

# # comprehension list for new_langs:
# new_langs = [lang.strip() for lang in all_langs if lang.strip()]


def numStudent(langList):
    """counting number of languages per student returning dictionary """
    d = dict()
    for c in langList:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print("\nNumber of languages per student (dict):", numStudent(all_langs2))


langs = []
for x in all_langs2:
    for index, each in enumerate(langs):
        if x in each:
            langs[index][1] += 1
    else:
        langs.append([x, 1])

print("\nNumber of languages per student (list):", langs)









