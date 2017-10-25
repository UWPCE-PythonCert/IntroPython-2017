#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
import ast
'''
TASKS
Write a format string that will take the tuple:

( 2, 123.4567, 10000, 12345.67)

and produce:

'file_002 :   123.46, 1.00e+04, 1.23e+04'
'''

val_tuple = (2, 123.4567, 10000, 12345.67)
print("First one is: file_{:0>3d}".format(val_tuple[0]))
print("Second one is: {:.2f}".format(val_tuple[1]))
print("Third one is: {:.2e}".format(val_tuple[2]))
print("Second one is: {:.2e}".format(val_tuple[3]))

new_tuple = ('file_' + "{:0>3d}".format(val_tuple[0]) + ":", "{:.2f}".format(val_tuple[1]), "{:.2e}".format(val_tuple[2]), "{:.3g}".format(val_tuple[3]))
print(new_tuple)

# Take an arbitrary number of values

vals = ast.literal_eval(input("Enter the comma-separated values for this example: "))

print("vals is: ", vals)
placeholder = '{:} '*len(vals)

print("The",len(vals),"numbers are:",placeholder.format(*vals))
