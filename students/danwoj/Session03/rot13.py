def rot13(string):
	cipher = ''
# This function begins by going through each character and determining its Unicode value
	for i in range(len(string)):
		y = ord(string[i:i+1])
		# This conditional is triggered if a capital letter is identified
		if y >= 65 and y <= 90:
			# This conditional converts the letter to ROT13
			if (y+13) <= 90:
				z = chr(y+13)
				cipher = cipher + z
			# This else statement essentially 'resets' the ROT13 substitution if the letter goes over the bounds of capitals in Unicode
			else:
				z = chr(y-13)
				cipher = cipher + z
		# This conditional is triggered if a lowercase letter is identified
		elif y >= 97 and y <= 122:
			# This conditional converts the letter to ROT13
			if (y+13) <= 122:
				z = chr(y+13)
				cipher = cipher + z
			# This else statement essentially 'resets' the ROT13 substitution if the letter goes over the bounds of lowercases in Unicode
			else:
				z = chr(y-13)
				cipher = cipher + z
		# This final else statement ignores any characters that are neither capital nor lowercase letters. This allows for puncuation to persist in the ROT13 substitution
		else:
			cipher = cipher + string[i:i+1]
	return cipher

def mainloop():
	i_value1 = 'Zntargvp sebz bhgfvqr arne pbeare.'
	i_value2 = 'Magnetic from outside near corner!'

	assert rot13(i_value1) == 'Magnetic from outside near corner.'
	assert rot13(i_value2) == 'Zntargvp sebz bhgfvqr arne pbeare!'


if __name__ == '__main__':
	mainloop()


