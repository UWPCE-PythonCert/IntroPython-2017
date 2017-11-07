def sleep_in(weekday, vacation):
    return(not weekday or vacation)

def monkey_trouble(a_smile, b_smile):
    return(not(a_smile ^ b_smile))

def sum_double(a, b):
    if a == b:
        return (a+b)*2
    else:
        return a+b

def diff21(n):
    m = n - 21
    if m > 0:
        m *= 2
    else:
        m = 21 - n
    return m

def parrot_trouble(talking, hour):
    if talking and ((hour < 7) or (hour > 20)):
        return True
    else:
        return False

def makes10(a, b):
    return((a == 10) or (b == 10) or (a + b == 10))

def near_hundred(n):
    return((abs(n-100) <= 10) or (abs(n-200) <= 10))

def pos_neg(a, b, negative):
    if negative:
        return (a<0 and b<0)
    else:
        return(((a<0) ^ (b<0)))

def not_string(str):
    if str.startswith("not"):
        return(str)
    else:
        return("not "+str)

def missing_char(str, n):
    return((str[:n]) + (str[n+1:]))

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return(str[-1:] + str[1:-1] + str[0])

def front3(str):
    return(str[:3]*3)

