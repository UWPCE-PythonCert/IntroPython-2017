


"""
parse students.txt file to get languages used by students


infile = "students.txt"

all_langs =[]

with open(infile) as students:
	students.readline()
	for line in students:
		line = line.strip()
		lang = (line.split(':'))[1].split(',')
		if lang[0].strip()[0].upper():
			lang = lang[1:]
		all_langs.extend(lang)
#new_langs = []
#for lang in all_langs:
#	if lang.strip():
#		new_langs.append(lang.strip())


new_langs = [lang.strip() for lang in all_langs if lang.strip()]

all_langs = set(new_langs)
print(all_langs)


think about questions, periods, sentences. but have preposition.

build up random text

"""
#trigrams.py
import random
with open('copypasta.txt','r') as filename:
	content = filename.read()
#raw = "I wish, I may, I wish I might"
raw = content.lower().replace(',','').replace('.','').replace('!','').replace('?','').replace('"','').replace("'",'').replace('%','').replace('\n',' ').replace('\r','')
words = raw.split()
trigrams = {}
trigrams_output ={}
output_text = ""

#base key-value pairs
def base_dict():
	for i in range(len(words)-2):
		pair = tuple(words[i:i+2])
		follower = words[i+2]
		trigrams.setdefault(pair,[]).append(follower)

		#rand_gen()
	#print(trigrams)

#number of values
def rand_gen():
	for value_pair in trigrams.values():
		value_range=sum(1 for value in value_pair)
		ran_num=random.randrange(0,value_range)
		#print(ran_num)

#target key
#for key in trigrams.keys():
#	print([key[1]])

base_dict()

intialize = list(trigrams.keys())[random.randint(0,len(trigrams)-1)]
first_word = intialize[0]
second_word = intialize[1]

final = str(first_word + ' ' + second_word)

#print(final)

x = 0

while x < 200:
	key = (first_word, second_word)
	new_word = trigrams[key][random.randint(0,len(trigrams[key])-1)]
	final+=(' '+new_word)
	first_word = second_word
	second_word = new_word
	x+=1
print(final)



"""
while x< 10:
	key = first_word + ' ' + second_word
	new_word = temp[key][random.randint(0, len(temp[key])-1)]
	first_word = second_word
	second_word = new_word
	final+=new_word
"""
