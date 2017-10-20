# Write a format string that will take the tuple:
# ( 2, 123.4567, 10000, 12345.67)
# and produce:
# 'file_002 :   123.46, 1.00e+04, 1.23e+04'

def tuple_format(t):
    print('file_{:03d}:    {:02f}'.format(t[0],t[1]))

tuple_format(( 2, 123.4567, 10000, 12345.67))