#1/usr/bin/env python

infile = 'students.txt'

all_langs = []
with open(infile) as students:
    students.readline()
    for line in students:
        line = line.strip()
        langs = line.split(":")[1].split(",")
        if langs[0].strip()[0].isupper():
            langs = langs[1:]
        all_langs.extend(langs)
        print(langs)

# new_langs = []
# for lang in all_langs:
#     if lang.strip():
#         new_langs.append(lang.strip())

new_langs = [lang.strip() for lang in all_langs if lang.strip()]

all_langs = set(new_langs)
print(all_langs)

input('')



'''sherlock holmes thing
leave in the punctuation and create a minor subset of punctuation
loop through massive array. get a pair and the follower, store that off in a new structure.
randomly start with a pair of words, pull a random option from the matching subset
'''