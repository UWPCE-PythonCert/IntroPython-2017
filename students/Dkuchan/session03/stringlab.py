#stringlab.py

inputtuple=( 2, 123.4567, 10000, 12345.67)

def reformatter(inputtuple):
   # filenumber=str(inputtuple[0])
    #outputstring='file_{:0>3d}'.format(inputtuple[0]) + ', ' + '{:.2f}'.format(inputtuple[1]) + ', ' + '{:.2e}'.format(inputtuple[2]) + ', ' + '{:.2e}'.format(inputtuple[3])
    #print(outputstring)

    #outputstringv2='file_'
    length=len(inputtuple)
   # print(length)
    separator=' , '
    #I should convert data types into formats and then add them to string maybe?


    outputstringv2={:0>3d},{:.2f},{:.2e},{:.2e}.format(inputtuple[0],inputtuple[1],inputtuple[2],inputtuple[3])
    


    print(outputstringv2)
reformatter(inputtuple)


#I need to look at this string formatting stuff in more depth.