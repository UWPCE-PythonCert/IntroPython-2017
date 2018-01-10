#testscripts.py
roster=[['Dan',100,200,300,400],['Abbey',100,200,300],["Megan",100,200,300,100,100],['Spencer',100,200,300],['Marylee',100,200,300]]        #roster is a matrix containing names in column 0 and donations in 1,2,or 3

print(roster[2][0]) 
nameselection="Abbey"
if nameselection in roster:
    print("found!")
else:
    print("NOT FOUND")

'''
for i in range(0,len(roster)):
    print(i)
    if nameselection in roster[i]:
        print("found!")
    else:
        print("NOT FOUND")
'''


















#print(len(roster))

'''
searchfor='Dan'

if searchfor in roster[0]:
    print("Yes")
else:
    print("No")
'''
'''
i=0
for i in range(0,len(roster)):
    j=1
    numgifts=len(roster[i])-1
    totaldonations=0
    for j in range(1,numgifts+1):
        totaldonations+=roster[i][j]
    averagedonations=totaldonations/numgifts
    print(numgifts)
    print(totaldonations)
    print(averagedonations)
'''
 