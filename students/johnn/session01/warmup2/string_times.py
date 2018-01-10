
def string_times(string="",copies=1):
    outstring=""
    for time in range(1, copies+1):
        outstring=outstring+string
    return outstring

print(string_times("Hi",2))
print(string_times("Hi",3))
print(string_times("Hi",1))

