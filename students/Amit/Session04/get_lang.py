#!/usr/bin/env python3
from collections import defaultdict

def list_langs():

    with open('students.txt', 'r') as file:
        file.readline()
        languages = [lang.capitalize() for line in file for lang in line.strip().split(':')[1].replace(",", " ").strip().split() if not lang[0].isupper()]
    return languages

print(list_langs())
def main():
    dict_lang = {}
    for language in list_langs():
        if language not in dict_lang.keys():
            dict_lang[language] = 0
        dict_lang[language] += 1
    return dict_lang

def main2():
    dict_lang = defaultdict(int)
    for language in list_langs():
        dict_lang[language] += 1
    return dict(dict_lang)



print(main2())
print(main())
print(main2() == main())