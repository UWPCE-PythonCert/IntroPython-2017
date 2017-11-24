#!/usr/bin/python
 
import time

'''
These are hard-coded values to build out the donor dictionary.
'''
donor_fnames = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donor_lnames = ['Gates', 'Smith', 'Jones', 'Doe', 'Whatever']
donations = [[200, 500], [2000.00, 3000.50, 3000.00], [1500.00, 500.25], [400.00], [2000.12, 3000, 4000]]

'''
The next few lines essentially builds out the donor dictionary.
'''
keys = ['f_name', 'l_name', 'don_amt', 'don_num']
donor_dict = dict.fromkeys(keys, None)
donor_dict['f_name'] = donor_fnames
donor_dict['l_name'] = donor_lnames
donor_dict['don_amt'] = donations
donor_dict['don_num'] = []

for i in donor_dict['don_amt']:
	donor_dict['don_num'].append(len(i))

# This line creates a menu dictionary
menu = {'1': ['Enter New Donation', 'List Donors'], '2': ['Run Donor Report', 'Enter Donation'], '3': ['Quit Program', 'Go Back']}

'''
This function inputs a new donation. First it prints off a menu and allows the 
user to select from one of three options. Option one just print out a list of 
existing donors in the dictionary. The second option takes in a new donation. 
The third sends the user back to the previous menu.
'''
def ent_don():
	# Prints off basis input menu
	print('\n#########################\n#  Enter New Donation   #\n#########################\n')
	for k, v in menu.items():
		print('%s: %s' % (k,v[1]))
	nd_value = int(input('\nEnter your number choice: '))
	# Creates a donor list if the user selects that option from the menu
	if nd_value == 1:
		q = 0
		print('\nDONOR LIST:')
		for k in range(len(donor_dict['l_name'])):
			print(donor_dict['f_name'][q], donor_dict['l_name'][q])
			q += 1
		ent_don()

	# This conditional enters a new donation if the user selects that option from the menu
	elif nd_value == 2:
#		counter = 0
		new_don = 1
		f_name, l_name = input("Please enter the donor's name: \n").split()

		'''
		This next for loop goes through the dictionary to see if the donor is already 
		in it. If so, it will call the add_value function to record the existing donor's 
		new contribution. Otherwise, it calls the add_name function to add the new donor.
		'''

		for i in range(len(donor_dict['l_name'])):
#			print("The value of i is: ", i)
			if l_name == donor_dict['l_name'][i] and f_name == donor_dict['f_name'][i]:
				print('\n', donor_dict['f_name'][i], donor_dict['l_name'][i], 'is in the list.\n')
				add_value(i)
				return True
		add_name(f_name, l_name)
		i = len(donor_dict['f_name'])
		add_value(i)
		return True

	elif nd_value == 3:
		return True

#This function adds a new donor name into the donor dictionary.
def add_name(fn_val, ln_val):
	print('The name', fn_val, ln_val, 'is not in the donor list. Adding them as a new donor.\n')
	donor_dict['f_name'].append(fn_val)
	donor_dict['l_name'].append(ln_val)
	return True

#This function adds a donation value to the corresponding donor.
def add_value(counter):
	d_amt = float(input('Please enter the donation amount: '))

	if counter <= len(donor_dict['don_amt']):
		donor_dict['don_amt'][counter].append(d_amt)
		print_letter(counter, d_amt)		
	else:
		d_amt_list = [d_amt]
		donor_dict['don_amt'].append(d_amt_list)
		print_letter(counter-1, d_amt)
	return True

# This function generates a "thank you" letter in a text document
def print_letter(i, d_amt):
	file_name = str(donor_dict['l_name'][i]) + '_' + str(donor_dict['f_name'][i]) + '_' + time.strftime("%d") + time.strftime("%b") + time.strftime("%y") + '.txt'
	print('\nGenerating "Thank You" Letter:', file_name)
	f = open(file_name, "w+")
	f.write(time.strftime("%B") + ' ' + time.strftime("%d") + ',' + time.strftime("%Y") + '\n\nDear ' + donor_dict['f_name'][i] + ',\n\n' + 
	'Thank you so much for your generous donation of $' '%.2f' % d_amt + '. This contribution is so important to the work our organization does and we express our deepest appreciation of your support to our important cause.')
	f.close()
	return True

# This is the function that prints off the donor report
def run_report():
	print('\n######################  Donor Report ######################\n')
	print('Donor Name         | Total Given | Num Gifts | Average Gift')
	print('-----------------------------------------------------------')

	j = 0
	for i in donor_dict['don_amt']:
		tot_don = round(sum(i))
		avg_don = tot_don/len(donor_dict['don_amt'][j])
		num_dons = len(donor_dict['don_amt'][j])
		spacer1 = 17-(len(donor_dict['f_name'][j])+len(donor_dict['l_name'][j])+1)
		spacer2 = 5-len(str(tot_don))
		spacer3 = 8-len(str(num_dons))
		print(donor_dict['f_name'][j], donor_dict['l_name'][j], ' '*spacer1, '|', '$', '%.2f' % tot_don, ' '*spacer2, '|', num_dons, ' '*spacer3, '|', '$', '%.2f' % avg_don)
		j += 1

def mainloop():

	while True:
		# This creates the initial program menu
		print('\n###########################\n#    Mail Room Program    #\n###########################\n')
		for k, v in menu.items():
			print('%s: %s' % (k,v[0]))

		try:
			m_value = int(input('\nEnter your number choice: '))
		except (ValueError, UnboundLocalError):
 			print('Input must be an integer, try again.')

		if m_value == 3:
			print('\nQuitting Program\n')
			break
		elif m_value == 2:
			run_report()
		elif m_value == 1:
			ent_don()
		else:
			print('\n! - Please select option 1, 2, or 3 - !')

if __name__ == '__main__':
	mainloop()