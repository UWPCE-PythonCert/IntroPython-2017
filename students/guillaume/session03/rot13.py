

from string import ascii_lowercase, ascii_uppercase


def rot(n):
	'''
	Generate subsitution cypher table of value n
	'''
	lower_case = ascii_lowercase
	upper_case = ascii_uppercase
	rot_lower = lower_case[n:] + lower_case[:n] 
	rot_upper = upper_case[n:] + upper_case[:n]

	std_alphabet = lower_case + upper_case
	rot13_alphabet = rot_lower + rot_upper

	return std_alphabet, rot13_alphabet

def translation(string, n, boolean = True):
	'''
	Provide:
	- translation from natural to encoded by default
	- translation from encoded to natural when boolean == False
	'''
	from_t, to_t = rot(n)
	if boolean == False: from_t, to_t = to_t, from_t
	trans_table = str.maketrans(from_t, to_t)
	return string.translate(trans_table)

def rot13(string):
	'''
	Provide translation from natural to encoded
	'''
	return translation(string, 13)

def rot13_reverse(string):
	'''
	Provide translation from encoded to natural
	'''
	return translation(string, 13, False)

if __name__ == '__main__':
	print(rot(13))
	print(rot13('testo'))
	print(rot13_reverse('Zntargvp sebz bhgfvqr arne pbeare'))
	