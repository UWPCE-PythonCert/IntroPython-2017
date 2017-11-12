#trigrams.py

import os
processedContent = []
trigramDict = {}

def processFiles(filename):
    """Imports a file and processes out garbage"""

    f = open('sherlock_small.txt')
    content = f.read()
    f.close()
    content = content.split(' ')
    for i in range(0, len(content)):
        content[i] = content[i].strip(' ')
    #print(content[17:31])
    #print(content.punctuation())
    #print()
   # print()
  #  print(os.path.abspath('sherlock_small.txt'))
    return content

processedContent = processFiles('sherlock_small.txt')
print(processedContent)
