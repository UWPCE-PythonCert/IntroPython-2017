

#typeerror occurs when you try to do something to a type that cannot do it IE adding characters or strings 

#syntaxerror raises when an error in syntax is discovered, is this just like a missplaced semicolon?

#nameerror
import string

#attributeerror 

A='Dan Rocks'
B='Dan2 Rocks as well'

#FIRSTFUNTION EVER ----------
def dansfunction1():
	print("Dan is the best ever")
#FIRSTFUNTION EVER ----------

def testbreaktype():  #note that in this function using a '+' will concatenate the two strings
	
	C=A-B
	print(C)

#def testbreaksyntax():
#	print"Hello"	#syntax error is on this line.

#def testbreakname(): #calling this without defining instructions causes a name error


def testbreakattribute():
	string.random()		#random is not an attribute of the string class!


#dansfunction1()
#testbreaktype() #calling this causes a type error
#testbreaksyntax()
#testbreakname() #calling this without defining instructions causes a name error
#testbreakattribute()

print("Program Works")
