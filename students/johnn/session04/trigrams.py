#!/usr/bin/env python

import random

#text = "I wish I may I wish I might"
#text = "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers. His rooms were brilliantly lit, and, even as I looked up, I saw his tall, spare figure pass twice in a dark silhouette against the blind. He was pacing the room swiftly, eagerly, with his head sunk upon his chest and his hands clasped behind him. To me, who knew his every mood and habit, his attitude and manner told their own story. He was at work again. He had risen out of his drug-created dreams and was hot upon the scent of some new problem. I rang the bell and was shown up to the chamber which had formerly been in part my own."

input_file = open("boscombe_valley_mystery.txt","r")
text = input_file.read()
input_file.close()

#print("RAW_TEXT:",text)

# strip out most punctuation
text=text.replace("--", " ")
text=text.replace("-", " ")
text=text.replace(":", "")
text=text.replace("(", "")
text=text.replace(")", "")
text=text.replace("\"", "")
text=text.replace("\'", "")

# make a special placeholder for paragraphs
text=text.replace("\n\n", " __paragraph__ ")

# but make some punctuation into their own word
text=text.replace(".", " .")
text=text.replace(",", " ,")
text=text.replace("?", " ?")
text=text.replace("!", " !")

# build the input list
word_list = text.split()

# lower case words following periods because they 
# are probably not proper nouns
for index, word in enumerate(word_list):
    if word == "." and index < len(word_list)-1:
        word_list[index+1]=word_list[index+1].lower()

#print()
#print("PROCESSED_LIST:",word_list)

# index pairs
pairs={}
for item in range(2,len(word_list)):
    pair=( word_list[item-2],word_list[item-1] )
    follower=word_list[item]
    if pair not in pairs.keys():
        pairs[pair]=[]
    pairs[pair].append(follower)

#print()
#print("PAIRS:",pairs)

i=1
out_list=list(random.choice(list(pairs.keys())))
#print()
#print("SEED_PAIR:",out_list)

#print()
#print("writing the story",end="")
while True:
    cur_key=( out_list[i-1], out_list[i] )
    if cur_key in pairs.keys():
        next_word=random.choice(pairs[cur_key])
        out_list.append(next_word)
        i+=1
        #print(".",end="")
    else:
        break
    # don't let the output get too big
    if i > len(word_list) and next_word == ".":
        # break on period for continuity
        break

#print("GENERATED:",out_list)

# first word of sentence get capped
for index, word in enumerate(out_list):
    # careful not to walk off the end
    if word in [".", "?", "!"] and index < len(out_list)-1:
        out_list[index+1]=out_list[index+1].capitalize()

# capitalize the very first word
out_list[0]=out_list[0].capitalize()

# fixup the spacing for various stuff
out_text=" ".join(out_list)
out_text=out_text.replace(" .", ".")
out_text=out_text.replace(" ,", ",")
out_text=out_text.replace(" ?", "?")
out_text=out_text.replace(" !", "!")
out_text=out_text.replace("__paragraph__", "\n\n")
out_text=out_text.replace("  ", " ")
out_text=out_text.replace("\n ", "\n")

print()
print("OUT:",out_text)
print()

