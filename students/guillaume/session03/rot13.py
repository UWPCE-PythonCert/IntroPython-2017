

from string import ascii_lowercase, ascii_uppercase, maketrans

n = 13
lower_case = ascii_lowercase
upper_case = ascii_uppercase
std_alphabet = lower_case + upper_case

rot_lower = lower_case[n:] + lower_case[:n] 
rot_upper = upper_case[n:] + upper_case[:n]
rot13_alphabet = rot_lower + rot_upper

def rot13(string):
	
	trans_table = maketrans(std_alphabet, rot13_alphabet)
	return string.translate(trans_table)

def rot13_reverse(string):
	
	trans_table = maketrans(rot13_alphabet, std_alphabet)
	return string.translate(trans_table)

if __name__ == '__main__':
	print(std_alphabet)
	print(rot13_alphabet)
	print(rot13('testo'))
	print(rot13_reverse('Zntargvp sebz bhgfvqr arne pbeare'))