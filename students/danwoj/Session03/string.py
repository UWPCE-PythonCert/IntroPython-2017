def sorted(var):
#	print "%0d" % (1,)
	a = 'file' + '%03d' % values[0] + ' :   '
	b = '%.2f' % values[1] + ', '
	c = '%.2E' % values[2] + ', '
	d = '%.2E' % values[3]
	return a + b + c + d


values = (2, 123.4567, 10000, 12345.67)
sorted(values)

assert sorted(values) == 'file002 :   123.46, 1.00E+04, 1.23E+04'



def formatter(in_tuple):
	num = len(in_tuple)
	fs = 'The {} numbers are:'
	fs += (num * '{}, ')[:-2]
	print(fs.format(num, *t)

 #   return form_string.format(in_tuple)

t1 = (9)
t2 = (5, 18)
t3 = (3, 34, 90)
t4 = (2, 23, 400, 57)

formatter(values2)

assert formatter(t1) == 'the 1 numbers are: 9'
assert formatter(t2) == 'the 2 numbers are: 5, 18'
assert formatter(t3) == 'the 3 numbers are: 3, 34, 90'
assert formatter(t4) == 'the 4 numbers are: 2, 23, 400, 57'