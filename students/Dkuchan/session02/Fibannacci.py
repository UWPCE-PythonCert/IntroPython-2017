#Fibannacci...
#I probably spelled that wrong...


while True:
    try:
        strnglngth=input("Please enter how many numbers you would like resolved: ")
        strnglngth=int(strnglngth)
    except ValueError:
        print("Please enter a Number for string length")
        continue
    else:
	   	break
	
def dofibs(strnglngth):
    print(1,end="")
    print(',',end="")
    for count in range(1,strnglngth):
        print(count+(count-1),end="")
        if count<strnglngth-1:
            print(',',end="")


dofibs(strnglngth)
print()

