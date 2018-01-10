
def diff21(number):
    twentyone=21
    difference=twentyone-number
    absdiff=abs(difference)
    #print(twentyone,"-",number,"=",difference,"; abs = ",absdiff)
    if number>twentyone:
        return absdiff * 2
    else:
        return absdiff

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(22))
#print(diff21(24))
#print(diff21(0))
#print(diff21(-3))
