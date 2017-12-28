
def string_match(string1="", string2=""):
    occurances=0
    for s1loop in range(0, len(string1)-1):
        s1sub=string1[s1loop:s1loop+2]
        occurances=occurances+string2.count(s1sub)
    return occurances

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc','abc'))
print(string_match('abc','axc'))
