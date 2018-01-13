#Mailroom Object Oriented Programming - Classes

import sys

#-----------------------------------------------------------------
# Class - Donor
#-----------------------------------------------------------------

class Donor():

	_any_donor_name = None


	def __init__(self, name = None):
		self.donations = []
		self.donor_name = name

	@property
	def donor_name(self):
		return self._any_donor_name

	@donor_name.setter
	def donor_name(self, value):
		self._any_donor_name = value

	def get_donations(self):
		return self.donations

	def initialize_donation(self, value):
		self.donations.extend(value)

	def add_donation(self, value):
		self.donations.append(value)

	def get_total_donations(self):
		return sum(self.donations)

	def get_count_of_donations(self):
		return len(self.donations)

	def get_average_donation(self):
		if self.get_total_donations()/self.get_count_of_donations() != 0:
			return self.get_total_donations()/self.get_count_of_donations()
		return 0



	
#-----------------------------------------------------------------
# Class - Mailroom
#-----------------------------------------------------------------

class Mailroom():


#-----------------------------------------------------------------
# Method - __init__
#-----------------------------------------------------------------

	def __init__(self, optional_dict=None):
		self.initial_donors = []
		if optional_dict is not None:
			for k, v in optional_dict.items():
				temp = Donor(k)
				temp.initialize_donation(v)
				self.initial_donors.append(temp)
		
#-----------------------------------------------------------------
# Method - Choices
#-----------------------------------------------------------------

	def choices(self):
		choice = input('\n(1) Send a Thank You\n(2) Create a Report\n(3) Send Letters to Everyone\n(4) Search for a Specific Donor\n(5) Quit\n\nWhat would you like to do?\n')
		dictswitch = {'1':self.list_add,
					 '2':self.report,
					 '3':self.send_letters_to_everyone,
					 '4':self.searched_donor,
					 '5':self.quit
					}
		try:
			dictswitch[choice]()
		except KeyError:
			print('\nPlease select a value between 1 and 5.')
		self.choices()

#-----------------------------------------------------------------
# Methods - Send a Thank You
#-----------------------------------------------------------------

	def list_add(self):
		clist = input("Would you like to see the dict of donars? (type 'dict' to observe)\n")
		if clist == 'dict':
			print()
			self.check_dict()
			pass
		name_checked, donated_value = self.create_new_donor()
		self.add_donation(name_checked, donated_value)
		self.send_thank_you(name_checked, donated_value)

	def add_donation(self, name_checked, donated_value):
		name_exist = False
		for p in self.initial_donors:
			if p.donor_name == name_checked:
				p.add_donation(donated_value)
				name_exist = True
		if not name_exist:		
			temp = Donor(name_checked)
			temp.add_donation(donated_value)
			self.initial_donors.append(temp)
	
	   
	def check_dict(self):
		[print(i.donor_name) for i in self.initial_donors]
		print()

	#break out values for individuals testing
	def create_new_donor(self):
		name_checked = input('\nWho is donating to our charity?\n').strip()
		donated_value = input('\nHow much are they donating?\n').strip()
		try:
			donated_value = float(donated_value)
		except ValueError:
			print('\nPlease provide an numeric value.')
		return name_checked, donated_value
		

	def send_thank_you(self, name_checked, donated_value):
			email =('\nThank you! {} has donated ${} to a great cause!\n'.format(name_checked, donated_value))
			print(email)
			return email

#-----------------------------------------------------------------
# Method - Create a Report
#-----------------------------------------------------------------

	def report(self):
		header = (('\n{:<25} {:<15}  {:<15}   {:<15}\n'.format('Donor','Total ($)','AVG ($)','# of Donations')))
		line_break = ('-' * 75 + '\n')
		report_data = []
		for p in sorted(self.initial_donors,key=lambda i:i.get_total_donations(),reverse=True):
			report_data.append('{:<25} ${:<15.2f} ${:<15.2f}  {:<15}\n'.format(p.donor_name,
																				p.get_total_donations(),
																				p.get_average_donation(),
																				p.get_count_of_donations()))
		full_report = header + line_break + ''.join(report_data)
		print(full_report)


#-----------------------------------------------------------------
# Methods - Send Letters to Everyone
#-----------------------------------------------------------------

	def send_letters_to_everyone(self):
		for l in self.initial_donors:
			if l.get_count_of_donations() > 1:
				s= 's'
			else:
				s = ''
			self.letter_output(l.donor_name, l.get_total_donations(), l.get_count_of_donations(), s)
		print('\nDonors have recieved their letter of total donations and thanks.')


	def letter_output(self, donor, total_donations, number_of_donations, s):
		import os
		letter= f'\nDear {donor},'+f'\n\nThank you for your very kind donation of ${total_donations} over {number_of_donations} donation{s}.'+f'\nYour generiosity has been put to very good use.'+f'\n\nSincerely,'+f'\nThe Team'
		if not os.path.exists('Donation_Letters'):
			os.mkdir('Donation_Letters')
		with open(os.path.join('Donation_Letters', donor + ".txt"), "w") as text_file:
			text_file.write(letter)
		return letter



#-----------------------------------------------------------------
# Methods - Search for a Given Donor
#-----------------------------------------------------------------


	def searched_donor(self):
		searched = input('Who would you like specific information on?\n').strip()
		self.scan_donors(searched)

	def scan_donors(self, searched):
		name_exist = False
		for p in self.initial_donors:
			if p.donor_name == searched:
				print('\n{} has donated ${} over the course of {} donations.\n'.format(p.donor_name, p.get_total_donations(), p.get_count_of_donations()))
				name_exist = True
		if not name_exist:
			print('\nThere is not a donor named {} in the list of current donors.\n'.format(searched))

#-----------------------------------------------------------------
# Method - Quit
#-----------------------------------------------------------------

	def quit(self):
		"""quits the program"""
		sys.exit()


#-----------------------------------------------------------------
# Program - Mailroom OOP
#-----------------------------------------------------------------


if __name__ == '__main__':
	dict_of_initial_donors = {'William Gates':[10000], 'Mark Zuckerberg':[6000], 'Jeff Bezos':[8000], 'Paul Allen':[1300], 'Satya Nadella':[20000]}
	my_mailroom = Mailroom(dict_of_initial_donors)
	print('\nIntializing your choices!')
	my_mailroom.choices()

	I

	
	

  
	






