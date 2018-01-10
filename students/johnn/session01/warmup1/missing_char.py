def missing_char(word, index):
    if word:
        wordlength=len(word)
        start=0
        return word[start:index]+word[index+1:wordlength]
        
print(missing_char("kitten", 1))
print(missing_char("kitten", 0))
print(missing_char("kitten", 4))
