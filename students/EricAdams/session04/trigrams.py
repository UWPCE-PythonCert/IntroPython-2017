words = "I wish I may I wish I might".split()

print(words)


trigrams = {}
for i in range(len(words)-2):
    pair = tuple(words[i:i+2])
    follower = words[i+2]
    print(pair, follower)
    if pair in trigrams:
        trigrams[pair].append(follower)
    else:
        trigrams[pair] = [follower]

print(trigrams)
