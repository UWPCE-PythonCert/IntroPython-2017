
def string_bits(string):
    string_len=len(string)
    outstring=""
    for i in range(0, string_len, 2):
        outstring=outstring+string[i]
    return outstring

print(string_bits("Hello"))
print(string_bits("Hi"))
print(string_bits("Heeololeo"))
