words = "I wish may I wish I might".split()

print("The approach from class")

trigrams = {}

for i in range(len(words)-2):
    pair = tuple(words[i:i+2])
    follower = words[i+2]
    print(pair, follower)
    if pair in trigrams:
        trigrams[pair].append(follower)
    else:
        trigrams[pair] = [follower] #key:pair

print(trigrams)

# .item :

print("The approach with .item()")

words = "I wish may I wish I might".split()

trigrams = {}

for i in range(len(words)-2):
    pair = tuple(words[i:i+2])
    follower = words[i+2]
    print(pair, follower)
    trigrams[pair] = follower

print(trigrams.items())


# .setdefault :

print("THe approach with .setdefault")

words = "I wish may I wish I might".split()

trigrams = {}

for i in range(len(words)-2):
    pair = tuple(words[i:i+2])
    follower = words[i+2]
    print(pair, follower)
    if pair not in trigrams:
        trigrams.setdefault(pair, follower)        
    # else:
    #     trigrams[pair].append(follower)        
print(trigrams)
