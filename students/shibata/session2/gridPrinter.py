# gridPrinter.py session2 Using nest
"""
for i in (0, 2):
    for i in range (0, 2):
        print ('+','-','-','-','-', end=' ')
    print ('+')
    for i in range (0, 4):
        print ('|','       ','|','       ','|')
print ('+ - - - - + - - - - +')
"""

for i in range(0, 2):
    print ('+ - - - - + - - - - +')
    for i in range (0, 4):
        print ('|','       ','|','       ','|')
print ('+ - - - - + - - - - +')

