"""
Kathryn Egan

In the class repo, in:

Examples/Session01/students.txt

You will find the list I generated in the first class
of all the students in the class, and what programming
languages they have used in the past.

Write a little script that reads that file, and generates
a list of all the languages that have been used.

Extra credit: keep track of how many students specified each language.
"""


def main():
    path_to_file = '/Users/kathryn/Desktop/Programming in Python/IntroPython-2017/examples/Session01/students.txt'

    languages = {}

    with open(path_to_file, 'r') as f:
        f.readline()
        for line in f.readlines():
            langs = line.split(':')[1].split(',')
            langs = [
                l.strip() for l in langs
                if l.strip() and l.strip().islower()]
            for lang in langs:
                languages.setdefault(lang, 0)
                languages[lang] += 1

    for lang, count in sorted(languages.items(), key=get, reverse=True):
        print('{} ({} students)'.format(lang, count))


def get(item):
    return (item[1], item[0])


if __name__ == '__main__':
    main()
