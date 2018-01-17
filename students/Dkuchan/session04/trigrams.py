#trigrams.py

import os, random
processedContent = []
numsentances = 0


def processFiles(filename):
    """Imports a file and processes out garbage"""

    #f = open('sherlock_small.txt')
    #content = f.read()
    #f.close()
    content = 'I wish I may I wish I might'
    content = content.split(' ')

    for i in range(0, len(content)):
        content[i] = content[i].strip(' ')

    #print(content[17:31])
    #print(content.punctuation())
    #print()
   # print()
  #  print(os.path.abspath('sherlock_small.txt'))
    return content


def dictmaker(processedContent):
    """Takes a processed input and creates a trigram output"""
    trigramDict = {}
    
    for i in range(len(processedContent) - 2):  # scans through data (-2 for pairs)
        trigramkey = tuple(processedContent[i:i + 2])   # identifies pairs for keys remember that when getting infor between locations the last number is not included hence i+2
        trigramVal = processedContent[i + 2]    # Identifies 3rd word for vals in dict
        trigramDict.setdefault(trigramkey, []).append(trigramVal)

    return trigramDict

def constructTrigram(trigraminput,slings):

    ''' Takes and input Dict and creates a trigram output'''

    for i in range(0, slings):
        trigramVallist = list(trigraminput)
        trigramKeylist = list(trigraminput.keys())
        trigramOutput = list(random.choice(trigramKeylist))
        for j in range(random.randint(2, slings)):
            pair = tuple(trigramOutput[-2:])  # the next word pair is the last two words
            trigramOutput.append(random.choice(trigramKeylist[pair]))



    print(trigramOutput)


def primeuserform():
    ''' Presents user with a way to select how many trigrams
    they want to make.
    '''
    while True:
        try:
            response = input("How many trigram sentences would you like to create?: ")
            response = int(response)
        except ValueError:
            print("Please enter a number.")
            print()
            print()
            continue
        else:
            break
    return response

# FUNCTION CALLS


numsentances = primeuserform()
outputdict = dict()
outputdict = dictmaker(processFiles('sherlock_small.txt'))
constructTrigram(outputdict, numsentances)

