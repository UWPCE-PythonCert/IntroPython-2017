#!/usr/bin/env python3

donor_names = ["William Gates III", "Mark Zuckerberg", "Jeff Bezos", "Paul Allen"]
donations = [[200,500], [2000,3000], [4000,5000], [100,150]]


def thank_you():

	while True:

		if (str(input("Do you want to see the donor list? if yes, type List: ")) == "list"):
			print(donor_names, donations)
		new_donor = str(input("Full Name: "))
		new_donation = int(input("How much do you want to donate?: "))
	
		if (new_donor not in donor_names):
			donor_names.append(new_donor)
			donations.append([new_donation])
			print("Thank you for donation, {}! Your donation amount is {}.".format(new_donor, new_donation))

		else:
			number = donor_names.index(new_donor) #4
			donations[number].append(new_donation)
			print("Thank you donation, {}! Your donation amount is {}.".format(new_donor, new_donation))
			
		for index, name in enumerate(donor_names):
			donation = donations[index]
			statement = '{} contributed ' + '{}, ' * len(donation)
			print(statement.format(name, *donation))

		if(input("Type 'exit' to end?").lower() == "exit"): break


def print_report():


	print("{msg1: <50}| {msg2: <12}| " \

      "{msg3:<10}| {msg4: <12}".format(msg1="Donor Name",

                                       msg2="Total Given",

                                       msg3="Num Gifts",

                                       msg4="Average Gift"))


	for i, d in enumerate(donor_names):
		t = sum(donations[i])
		n = len(donations[i]) #list.count() is to count inside of the list (i.e. # by blue)
		a = t/n

		print("{d: <50} ${t: 12.2f}{n: 12d}{a: 14.2f}".format(d=d, t=t, n=n, a=a))


def mainloop():
    # result = input("type something")
    # print("you typed: ", result)

    while True:

        answer = int(input("Select from one of these options:\n"
                           "(1) Send a Thank you\n"
                           "(2) Create a Report\n"
                           "(3) quit\n"
                           ))

        if answer == 3:
            break

        elif answer == 1:
            thank_you()

        elif answer == 2:
            print_report()

        else:
            print("please type 1, 2, or 3")


if __name__ == "__main__":
    print('starting...')
    mainloop()


