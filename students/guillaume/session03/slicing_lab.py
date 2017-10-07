
def exch_first_last(seq):
	'''
	Exchange the first & last item of a sequence
	'''
	l = len(seq) - 1
	return  seq[-1:] + seq[1:l] + seq[0:1]
	

def every_other_rem(seq):
	'''
	Print a sequence with every other item of the initial sequence
	'''
	l = len(seq)
	seq_ret = seq[0:1]
	for i in range(2, l, 2):
		seq_ret = seq_ret + seq[i:i + 1]
	return seq_ret

def first_last_in_bet(seq):
	'''
	'''
	return every_other_rem(seq[4:len(seq) - 4])

def reverse_slic(seq):
	'''
	'''
	l = len(seq) + 2
	seq_ret = seq(l + 1:l)
	for l in range(0, l, -1):

	pass

if __name__ == '__main__':

	functions = [exch_first_last, every_other_rem, first_last_in_bet]
	test_lst = ['', 'tesu', 'ab',''.join(map(str,list(range(10)))), [1,2,3], list(range(25)), list(range(9))]

	for function in functions:
		print(repr(function.__name__))
		print(repr(function.__doc__))
		for seq in test_lst:
			print(seq)
			print(function(seq))
		print()
		

