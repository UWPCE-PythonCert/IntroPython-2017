
def near_hundred(n):
    #if n >= 90 and n <= 110:
    #    return True
    #if n >= 190 and n <= 220:
    #    return True
    #return False
    if (( 100 - n ) <= 10 ) or (( 200 -n ) <= 10 ):
        return True
    else:
        return False

print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
#print(near_hundred(200))
#print(near_hundred(-100))
