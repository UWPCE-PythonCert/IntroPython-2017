
def string_times(string=""):
    string_len=len(string)
    outstring=""
    for chunk in range(1, string_len+1):
        outstring=outstring+string[0:chunk]
    return outstring

print(string_times("Code"))
print(string_times("abc"))
print(string_times("ab"))

