#!/usr/bin/env python3.6
donor_names = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donations = [[200, 500], [2000, 3000, 3000], [1500, 500], [400], [2000, 3000, 4000]]
donors = zip(donor_names, donations)
#for donor_names, donations in zip(donors):
#	print(donor_names, '...', donations)
#global donors
#
#print(donors)
#print(list(donors))

#donors = list(donor_names, donations)


# donors[0][1]

# This adds a donation to the donor in the 0th place, the [1] is the second field of the 0th value, in other words the list of donations
# donors[0][1].append(600)

# for donor in donors:
# if donor[0].lower() == 'fred':
# if donor[0] == 'fred'
def report():
	print('Donor Name                | Total Given | Num Gifts | Average Gift')
	print('------------------------------------------------------------------')
#	for len(donors)
	for donor_names, donations in list(donors):

		print(donor_names, '...', donations)
	return True

def thank_you():
	print('\n#####################\n#  Send Thank You   #\n#####################\n')
	d_value = int(input('\n#####################\n# Mail Room Program #\n#####################\n'
		'1: List Donors\n'
		'2: Enter Donation\n'
		'3: Quit\n'
		'Enter your number choice: '))
	d_name = input("Please enter the donor's name or type 'list' for list of donors or 'q' to go back: ")
	i = 0
	if d_name == 'list':
		for i in range (len(donor_names)):
			print(donor_names[i])
		thank_you()
	elif d_name == 'q':
		return False
	else:
		i = 0
		for i in range (len(donor_names)):
			if d_name == donor_names[i]:
				print('Name ', donor_names[i], 'is in the list.')
				d_amt = int(input('Please enter the donation amount:'))
				donations[i].append(d_amt)
				print(d_amt)
				print(donations[i])
				print('\nDear', d_name, ',\n\n'
					'Thank you so much for your generous donation of $',d_amt,'. This contribution is so important to the work our organization does and we express our deepest appreciation of your support to our important cause.')
				thank_you()
		print ('The name', d_name, 'is not in the donor list. Adding', d_name, 'as a new donor.')
		donor_names.append(d_name)
		donations.append([])
		print(donor_names)
		print(donations)
		thank_you()
		return True


def print_report():
	print('\nThis is the print report function')


def mainloop():

	while True:
		m_value = int(input('\n#####################\n# Mail Room Program #\n#####################\n'
		'1: Send a Thank You\n'
		'2: Create a Report\n'
		'3: Quit\n'
		'Enter your number choice: '))
		if m_value == 3:
			print('\nQuitting Program\n')
			break
		elif m_value == 2:
			print_report()
		elif m_value == 1:
			thank_you()
		else:
			print('\n! - Please select option 1, 2, or 3 - !')

if __name__ == '__main__':
	mainloop()