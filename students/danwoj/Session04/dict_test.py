donor_fnames = ['Bill', 'Melvin', 'Daphnie', 'Chauncey', 'Frieda']
donor_lnames = ['Gates', 'Smith', 'Jones', 'Doe', 'Whatever']
donations = [[200, 500], [2000.00, 3000.50, 3000.00], [1500.00, 500.25], [400.00], [2000.12, 3000, 4000]]

keys = ['f_name', 'l_name', 'don_amt', 'don_num']
donor_dict = dict.fromkeys(keys, None)
donor_dict['f_name'] = donor_fnames
donor_dict['l_name'] = donor_lnames
donor_dict['don_amt'] = donations
donor_dict['don_num'] = []

for i in donor_dict['don_amt']:
	donor_dict['don_num'].append(len(i))

menu = {'1': ['Enter New Donation', 'List Donors'], '2': ['Run Donor Report', 'Enter Donation'], '3': ['Quit Program', 'Go Back']}


# This is the function that prints off a thank you message for new donations
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

	# Enters a new donation if the user selects that option from the menu
	elif nd_value == 2:
		counter = 0
		new_don = 1
		f_name, l_name = input("Please enter the donor's name: \n").split()

		for i in donor_dict['l_name']:
			print('this is the first i value: ', i)
			if l_name == i:
				print('l_name is: ', l_name, 'i is:', i)
				for j in donor_dict['f_name'][counter]:
					print('f_name is: ', f_name, 'j is: ', j)
					counter += 1
					if f_name+l_name == j+i:
						print(f_name + l_name)
						print(j + i)
						print(donor_dict['f_name'][counter-1], donor_dict['l_name'][counter-1], 'is in the list.\n')
						add_value(counter)
				add_name(f_name, l_name)
				counter = len(donor_dict['l_name'])
				print('New Name #1. Counter value is: ', counter)
				add_value(counter)
				return True
			else:
				counter += 1
				print('No match')
		add_name(f_name, l_name)
		counter = len(donor_dict['l_name'])
		print('New Name #2. Counter value is: ', counter)
		add_value(counter)
		return True

		# Loop searches for the donor's name in the existing data set
#		for i in range (len(donor_names)):
#			# If the donor is in the list, this adds to their existing record
#			if d_name == donor_names[i]:
#				# This counter is used to indicate whether or not the donor was in the list in subsequent logic
#				new_don = 0
#				print('Name ', donor_names[i], 'is in the list.\n')
#				d_amt = float(input('Please enter the donation amount: '))
#				donations[i].append(d_amt)
#				ty_message(d_name, d_amt)
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
	elif nd_value == 3:
		return True

def add_name(fn_val, ln_val):
	print('This is the add_name funtion')
	donor_dict['f_name'].append(fn_val)
	donor_dict['l_name'].append(ln_val)
	print(donor_dict['f_name'], donor_dict['l_name'])
	return True

def add_value(counter):
	d_amt = float(input('Please enter the donation amount: '))
	print('d_amt is: ', d_amt)
	if counter == len(donor_dict['l_name']):
#		d_amt_list = []
#		d_amt_list.append(d_amt) 
#		print('d_amt_list: ', d_amt_list)
		donor_dict['don_amt'].append([d_amt])
		print('donor_dict[don_amt]: ', donor_dict['don_amt'])		
	else:
		donor_dict['don_amt'][counter-1].append(d_amt)
		print('Donor Amounts List: ', donor_dict['don_amt'])
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





#	i = 0
	# This loop goes through each donor record in the dataset
#	for i in range (len(donor_names)):
#		j = 0
#		tot_don = 0
#		avg_don = 0
		# This loop creates the total and average donation values for each donor
#		for j in range (len(donations[i])):
#			tot_don = tot_don + donations[i][j]
#			avg_don = avg_don + donations[i][j]
#		avg_don = avg_don / (j+1)
		# This prints off each donor's row in the report
#		print(donor_names[i], ' '*(14-len(donor_names[i])), '| $', '%.2f' % tot_don, ' '*(8-len('%.2f' % tot_don)), '|', j+1, ' '*(8-len(str(j+1))), '| $', '%.2f' % avg_don)
#	return True

def mainloop():

	while True:
		# This creates the initial program menu
		print('\n###########################\n#    Mail Room Program    #\n###########################\n')
		for k, v in menu.items():
			print('%s: %s' % (k,v[0]))
		m_value = int(input('\nEnter your number choice: '))
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