#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python
# mailroom1.py
# Display summary donor information: name, number of gifts, total amount for all gifts, average gift amount

# Donor names
# Note: Done with dictionary because I couldn't figure out how to do this using lists.
donor_gifts = {
    'William Gates': [100000, 23456, 891234],
    'Jeff Bezos': [654321, 56754],
    'Oscar Muñoz': [908765, 8796],
    'Mark Zuckerberg': [2000000]
}


def main():
# thank_you -->
    def thank_you(donor_gifts):
        ''' Send a thank you note using the following criteria:
            If the user types ‘list’, show them a list of the donor names and re-prompt
            If the user types a name not in the list, add that name to the data structure and use it.
            If the user types a name in the list, use it.
            Once a name has been selected, prompt for a donation amount.
            Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
            Once an amount has been given, add that amount to the donation history of the selected user.
            Use string formatting to compose an email thanking the donor for their generous donation.
            Print the email to the terminal and return to the original prompt. 
        '''

        # Get the name
        ty_name = None
        while (True):
            ty_name = str(input("Please enter the donor's name or type 'list' to see donor names. (Enter 'menu' to return to the original menu.) --> ")).strip()
            if ty_name == 'list':
                print("List of Donors:")
                for ty_name in donor_gifts:
                    print(ty_name)
            elif ty_name == 'menu':
                return
            else:
                break

        # Enter the donation amount. Input taken as an integer-only value
        while(True):
            donation_amount = int(input("Please enter the donation amount (Enter 'menu' to return to the original menu.) --> "))
            if donation_amount == 'menu':
                return
            else:
                break

        # Create an entry for a new name
        if ty_name not in donor_gifts:
            donor_gifts[ty_name] = []

        # Store the donation and send a thank you
        donor_gifts[ty_name].append(donation_amount)
        # Generate thank you note.  Format placeholders don't have any padding in order to produce a clean message.
        print("\nDear {d:}, \nThank you for your generous donation of ${t:<,.2f}.".format(d=ty_name, t=donation_amount))


# create_report() -->

    def create_report():
        ''' Create the report of donors and amounts. Present in formatted output. '''
        donor_report = []
        # Perform calculations for the number of gifts, total amount given by a donor, and a donor's average gift.
        for name,gifts in donor_gifts.items():
            total = sum(gifts)
            number_gifts = len(gifts)
            average_gift = total / number_gifts
            donor_report.append((name, total, number_gifts, average_gift))

        # Print the Report
        print("{: <30s} {: >19s}{: >14s}{: >15s}".format("Donor Name", "Amount Donated", "Total Gifts", "Average Gift"))
        print("-"*30, "+ ", "-"*16, "+", "-"*11, "+", "-"*12)
        for (name, total, number_gifts, average_gift) in donor_report:
            print("{d: <30} ${t: 18.2f}{n: >14d}{a: >15.2f}".format(
                d=name,
                t=total,
                n=number_gifts,
                a=average_gift))

# show_menu -->
    def show_menu():
        '''
        description: Present a menu of the choices to add an item, show current items, or exit the program.
        :rtype: string
        :return: string type
        '''
        while (True):
            print("""
                Menu of Options
                1) Send a Thank You
                2) Create a Report
                3) Quit
                """)
            strUserChoice = str(input("Which option would you like to perform? [1 to 3] - "))

            if strUserChoice == '1':  # send thank you note
                print("Choice 1: send thank you note")
                thank_you(donor_gifts)
            elif strUserChoice == '2':  # create report
                create_report()
            elif strUserChoice == '3':  # exit
                print("Choice 3: Quitting")
                break
        return strUserChoice


    show_menu()

if __name__ == "__main__":
    main()
