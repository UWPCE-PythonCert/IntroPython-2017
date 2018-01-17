
def front_times(string="",times=0):
    string_len=len(string)
    last=3
    if string_len < 3:
        last = string_len
    return string[0:last] * times


print(front_times("Chocolate",2))
print(front_times("Chocolate",3))
print(front_times("Abc",3))
