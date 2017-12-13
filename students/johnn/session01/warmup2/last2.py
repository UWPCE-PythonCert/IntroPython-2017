
def last2(string):
    string_len=len(string)
    matches=0
    #print("string:",string)
    if string_len >= 2:
        pattern=string[string_len-2:]
        for chunk in range(string_len-2):
            substring = string[chunk:chunk+2]
            if substring == pattern:
                matches += 1
            #print("substring:",substring,"pattern:",pattern,"matches:",matches)
        return matches
    else:
        return 0


print(last2("hixxhi"))
print(last2("xaxxaxaxx"))
print(last2("axxxaaxx"))

