
#doodles.py

r = lambda x, y: x**2 + y**2

print(r(3, 2))


xlen=13
gapfnc=int((xlen-3)/2)
ylen=11
yleni=int(ylen)
half=int(ylen/2)+1
outputbox="+" + "-" * gapfnc + "+" + "-" * gapfnc + "+"
noncenter="|" + " " * gapfnc + "|" + " " * gapfnc + "|"
for i in range(0,ylen+1):
    if i==0 or i==half or i==yleni:
        print(outputbox)
    else:
        print(noncenter)


#danstring="Hello my name is dan"*3 + "what do you think of that?"
#print(outputbox)