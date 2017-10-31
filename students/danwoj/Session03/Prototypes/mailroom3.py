#!/usr/bin/env python3.6
donor_names = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donations = [[200, 500], [2000.00, 3000.50, 3000.00], [1500.00, 500.25], [400.00], [2000.12, 3000, 4000]]
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
def print_report():
	print('\n#####################  Donor Report #####################\n')
	print('Donor Name      | Total Given | Num Gifts | Average Gift')
	print('--------------------------------------------------------')
	i = 0
	for i in range (len(donor_names)):
		j = 0
		tot_don = 0
		avg_don = 0
		for j in range (len(donations[i])):
			tot_don = tot_don + donations[i][j]
			avg_don = avg_don + donations[i][j]
		avg_don = avg_don / (j+1)
		print(donor_names[i], ' '*(14-len(donor_names[i])), '| $', '%.2f' % tot_don, ' '*(8-len('%.2f' % tot_don)), '|', j+1, ' '*(8-len(str(j+1))), '| $', '%.2f' % avg_don)
	return True

def thank_you():
#	print('\n#####################\n#  Send Thank You   #\n#####################\n')
	tym_value = int(input('\n#####################\n#  Send Thank You   #\n#####################\n'
		'1: List Donors\n'
		'2: Enter Donation\n'
		'3: Go Back\n'
		'Enter your number choice: '))
	if tym_value == 1:
		i = 0
		print('\nDONOR LIST:')
		for i in range (len(donor_names)):
			print(donor_names[i])
		thank_you()
	elif tym_value == 2:
		i = 0
		new_don = 1
		d_name = input("Please enter the donor's name: ")
		for i in range (len(donor_names)):
			if d_name == donor_names[d_name, i]:
				print('Name ', donor_names[i], 'is in the list.')
				new_don = 0
				don_value(d_name, i)
			if new_don == 1:
				print ('The name', d_name, 'is not in the donor list. Adding', d_name, 'as a new donor.\n')
#				donor_names.append(d_name)
#				donations.append([])
#				don_value(d_name, i)
#				print(donor_names)
#				print(donations)
		thank_you()
		return True
	elif tym_value == 3:
		return True

def don_value(name, num):
	print('Name ', donor_names[i], 'is in the list.')
	d_amt = int(input('Please enter the donation amount:'))
	donations[num].append(d_amt)
	print(d_amt)
	print(donations[num])
	print('\nDear', name, ',\n\n'
	'Thank you so much for your generous donation of $',d_amt,'. This contribution is so important to the work our organization does and we express our deepest appreciation of your support to our important cause.')
	return True

#def print_report():
#	print('\nThis is the print report function')


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