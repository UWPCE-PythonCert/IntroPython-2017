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
	


    #THIS IS WRONG!
def dofibs(strnglngth):
    for count in range(0,strnglngth):
        print(count+(count-1),end="")
        if count<strnglngth-1:
            print(',',end="")


dofibs(strnglngth)
print()

