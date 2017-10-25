# Slicing Lab

def firstlast(x):
    '''First and last items exchanged'''
    slice = x[-1] + x[0]
    return slice

def picketfence(x):
    '''Every other item removed'''
    picket = ""
    for i in range(len(x)):
        if i % 2 == 0:
            picket += x[i]
    return picket

def checkfour(x):
    '''first and last 4 items removed, and every other item in between'''
    check = x[3:-4]
    return check

def reverseit(x):
    '''Elements reversed (just with slicing)'''
    max = len(x)
    revstring = ""
    for i in range(max):
        revstring += x[(max-1)-i]
    return revstring

def thirdman(x):
    '''Middle third, then last third, then the first third in the new order'''
    max = len(x)
    third = int(max/3)
    sone = x[0:third]
    stwo = x[(third):(third*2)]
    sthree = x[(third*2):]
    rs = stwo + sthree + sone
    return rs

seq = "This is the monkey machine."
print ("firstlast: {}".format(firstlast(seq)))
print ("picket: {}".format(picketfence(seq)))
print ("checkfour: {}".format(checkfour(seq)))
print ("reverseit: {}".format(reverseit(seq)))
print ("thirdman: {}".format(thirdman(seq)))
