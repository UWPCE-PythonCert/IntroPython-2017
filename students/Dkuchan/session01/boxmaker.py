# BOXMAKER - Dan Kuchan 10-2017
#im sure this should be in a loop or something
while True:
	try:
		boxWidthraw=input("Please enter an odd number for box width: ")
		boxWidth = int(boxWidthraw)
	except ValueError:
	   print("Please enter an odd NUMBER for the box width")
	   boxWidthraw=input()
	   continue

	if boxWidth%2==0 or boxWidth==0:
		print("Box width is even, please enter an ODD number")
		continue 
	else:
	    break

boxWidth=int(boxWidthraw)-1	#cast the string value as an int removes one for 0-1 error

print("Please enter an odd number for box height:")
boxHeightraw=input()

while True:
	try:
	   boxHeight = int(boxHeightraw)
	except ValueError:
	   print("Please enter an odd NUMBER for the box height")
	   boxHeightraw=input()
	   continue
	else:
	    break
while True:
	if boxHeight%2==0 or boxHeight==0:
		print("Box height is even, please enter an ODD number")
		continue 
	else:
	    break	
boxHeight=int(boxHeightraw)-1	#cast the string value as an int (which should be doable because we checked if it was an int already)



def makebox():	#Takes input and makes the box thingy
	widthCenterline=boxWidth/2	#deviding an int will drop the remainder.  so add 1.
	heightCenterline=boxHeight/2
	i=0
	j=0

	while i<=boxHeight and j<=boxWidth+5: 
	    if i==0 or i==boxHeight or i==heightCenterline:	#are we in the first, middle, or last line?
		    print('+',end="")
		    j=j+1
		    while j <= boxWidth: 
		        if j==widthCenterline or j==boxWidth: #are we in the center or the right edge?
		            print('+',end="")
		        else: 
		        	print('-',end="")
		        j=j+1
	    else:
		    print('|',end="")
		    j=j+1 #incriment line counter
		    while j<=boxWidth:		
			    if j==widthCenterline or j==boxWidth:		#are we in the center or the right edge?
			        print('|',end="")
			    else:
			    	print(' ',end="")
			    j=j+1
	    j=0	#return to horizontal start
	    i=i+1
	    print()
	i=0
	

makebox()
print()
print("Wubba Lubba Dub Dub")