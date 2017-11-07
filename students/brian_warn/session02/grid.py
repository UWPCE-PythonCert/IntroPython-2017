#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python

'''
Grid exercise
'''

def grid_print():
	line1="+ "+"- "*3+"| "+"- "*3+"+"
	line2="+ "+" "*6+"| "+" "*6+"+"+"\n"
	#line1=line1.strip()
	print(line1+"\n"+line2*3+line1+"\n"+line2*3+line1)

	
#main
grid_print()