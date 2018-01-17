
""" Print fizz or buzz if the value is a multiple of 3 or five, respectively. """

for i in range(1, 101):

    message=""

    # is the number a multiple of three?
    if int( i / 3 ) == float( i / 3 ):
        message=message+"Fizz"

    # is the number a multiple of five?
    if int( i / 5 ) == float( i / 5 ):
        message=message+"Buzz"
     
    if not message:
        print(i)
    else:
        print(message)
        #print(message,"(",i,")")

