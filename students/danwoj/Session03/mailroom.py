#!/usr/bin/env python3.6

# This creates a statis donor table that does not retain values after this program runs
donor_names = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donations = [[200, 500], [2000.00, 3000.50, 3000.00], [1500.00, 500.25], [400.00], [2000.12, 3000, 4000]]

# This is the function that prints off the donor report
def print_report():
	print('\n#####################  Donor Report ####################\n')
	print('Donor Name      | Total Given | Num Gifts | Average Gift')
	print('--------------------------------------------------------')
	i = 0
	# This loop goes through each donor record in the dataset
	for i in range (len(donor_names)):
		j = 0
		tot_don = 0
		avg_don = 0
		# This loop creates the total and average donation values for each donor
		for j in range (len(donations[i])):
			tot_don = tot_don + donations[i][j]
			avg_don = avg_don + donations[i][j]
		avg_don = avg_don / (j+1)
		# This prints off each donor's row in the report
		print(donor_names[i], ' '*(14-len(donor_names[i])), '| $', '%.2f' % tot_don, ' '*(8-len('%.2f' % tot_don)), '|', j+1, ' '*(8-len(str(j+1))), '| $', '%.2f' % avg_don)
	return True

# This function prints out the 'thank you' message for a new donation
def ty_message(dn, da):
	print('\nDear', dn, ',\n\n'
	'Thank you so much for your generous donation of $', '%.2f' % da,'. This contribution is so important to the work our organization does and we express our deepest appreciation of your support to our important cause.')
	return True

# This is the function that prints off a thank you message for new donations
def thank_you():
	# Prints off basis input menu
	tym_value = int(input('\n#####################\n#  Send Thank You   #\n#####################\n'
		'1: List Donors\n'
		'2: Enter Donation\n'
		'3: Go Back\n'
		'Enter your number choice: '))
	# Creates a donor list if the user selects that option from the menu
	if tym_value == 1:
		i = 0
		print('\nDONOR LIST:')
		for i in range (len(donor_names)):
			print(donor_names[i])
		thank_you()
	# Enters a new donation if the user selects that option from the menu
	elif tym_value == 2:
		i = 0
		new_don = 1
		d_name = input("Please enter the donor's name: \n")
		# Loop searches for the donor's name in the existing data set
		for i in range (len(donor_names)):
			# If the donor is in the list, this adds to their existing record
			if d_name == donor_names[i]:
				# This counter is used to indicate whether or not the donor was in the list in subsequent logic
				new_don = 0
				print('Name ', donor_names[i], 'is in the list.\n')
				d_amt = float(input('Please enter the donation amount: '))
				donations[i].append(d_amt)
				ty_message(d_name, d_amt)
		# This statement checks to see if the counter was changed from the previous conditional. If it was not changed, then that indicates a new donor
		if (new_don == 1):
			# This adds a new donor and his or her donation to the data set
			print ('The name', d_name, 'is not in the donor list. Adding', d_name, 'as a new donor.\n')
			donor_names.append(d_name)
			d_amt = float(input('Please enter the donation amount: '))
			donations.append([d_amt])
			ty_message(d_name, d_amt)
			thank_you()
		return True
	elif tym_value == 3:
		return True

def mainloop():

	while True:
		# This creates the initial program menu
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