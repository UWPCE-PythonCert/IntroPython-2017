
def format_string(tuple):
	a, b, c, d = tuple
	print( "file_{0:0>3} :   {1:.2f}, {2:.2e}, {3:.2e}".format(a, b, c, d) )

def arbitrary(tuple):
	tuple_length=len(tuple)
	format_list=[]
	for entries in range(tuple_length):
		format_list.append("{:d}")
	format_string="The {} numbers are: "+", ".join(format_list)
	print( format_string.format(tuple_length,*tuple) )


format_string( (2, 123.4567, 10000, 12345.67) )
arbitrary( (1,2,3) )
arbitrary( (1,2,3,4) )
