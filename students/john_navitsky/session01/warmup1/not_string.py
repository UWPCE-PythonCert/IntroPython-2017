
def not_string(string):
    if "not" in string:
        return string
    else:
        return "not " + string

print(not_string("candy"))
print(not_string("x"))
print(not_string("not bad"))

