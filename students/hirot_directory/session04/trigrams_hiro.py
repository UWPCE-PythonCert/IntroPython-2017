words = "I wish may I wish I might".split()
#print(words)


trigrams = {} #empty dict

for i in range(len(words)-2):
	pair = tuple(words[i:i+2])
	follower = words[i+2]
	print(pair, follower)
	if pair in trigrams:
		trigrams[pair].append(follower)
	else:
		trigrams[pair] = [follower] #key:pair

print(trigrams)

#this can be called by one dict method. Find the method.

#print dict.keys()
#print dict.values()
#print dict.items()

# .item() shows the same result. 

trigrams = {} #empty dict

for i in range(len(words)-2):
	pair = tuple(words[i:i+2])
	follower = words[i+2]
	print(pair, follower)
	trigrams[pair] = follower

#print(trigrams.keys())
#print(trigrams.values())
print(trigrams.items())