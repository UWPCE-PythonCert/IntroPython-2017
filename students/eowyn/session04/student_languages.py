#!/usr/bin/env python

''' 
    Read and parse a text file containing student names and languages known. 
    Print all the languages known, collectively, and the number of students
    who know each language. 
    '''
infile = "students.txt"
all_langs = []
with open(infile) as students:
    students.readline() # read one line from file and discard
    for line in students: # file object is an iterable which will deliver one line at a time like this
       line = line.strip()
      # line.split(":") # produces a list with two elements, a name and a list of comma sep languages
       langs = line.split(":")[1].split(',')
       if langs[0].strip()[0].isupper():
        # remove the nicknames which are all capitalized
        langs = langs[1:]
       all_langs.extend(langs)

# still have white space and an empty string in our list
### Python list comprehensions fix this in a nifty way:
new_lang = [lang.strip() for lang in all_langs if lang.strip()]

### another approach is map, which in most cases is easier with list comprehensions

### determine frequency of each language
lang_frequency= {x:new_lang.count(x) for x in new_lang}

new_lang = set(new_lang)
print(new_lang)
print(lang_frequency)

