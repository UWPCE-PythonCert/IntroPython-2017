strings = ( 2, 123.4567, 10000, 12345.67)
print ()

def padzero(x):
    nu = x * .001
    strnum = str(nu)
    outnum = strnum[2:]
    return outnum

def roundit(y):
    return round(123.4567, 2)

def exponentn(x):
    return "{:e}".format(x)

print("file{}".format(padzero(strings[0]))
#print("{}".format(roundit(strings[1]))
#print("{}".format(exponentn(strings[2]))
#print("{}".format(exponentn(strings[3]))
