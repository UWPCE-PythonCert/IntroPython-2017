#!/usr/bin/env python
# Description: This script will accomplish the following goals:
# (1) It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
# This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
# You can store that data structure in the global namespace.
# (2) The script should prompt the user (you) to chooose from a menu of 3 actions:
# Send a Thank You", "Create a Report" or "Quit".
# Comments: Remember to use verbs for function names and nouns for variables.
# In addition, you can use a dictionary; however try to use list and tuples for this assignment
# Last modified on 10/22/2017 by David Kan


# Define global varables and data structure
donors = []
donor_name = ['david', 'brian', 'larry', 'mary', 'tyler']
donor_cost = [[100, 200], [150, 200], [100], [400], [100, 200, 300]]
donors = list(zip(donor_name, donor_cost))


def show_donor_list():
    """
    Function will show all of the names in the donor list data structure
    :return: None
    """
    print()
    # List all names in the donor list data structure
    for index in range(len(donors)):
        print(''.join([str(index + 1),'. ', '{}'.format(donors[index][0])]))


def add_donor(full_name):
    """
    Function will add a username to the donor list data structure if it does not already exist
    :param full_name: username in lowercase
    :return: None
    """
    print()
    # If username not in list, then add that name to the data structure and use it
    donors.append(('{}'.format(full_name), []))


def get_donors_index(full_name):
    """
    Function will get the index location of the donor in the donor list data structure
    :param full_name: username in lowercase
    :return: donor_name_index - the index location of the donor
    """
    # If user types a name in the list, then use it
    donor_name_index = [row[0] for row in donors].index(full_name)

    return donor_name_index


def get_donation_amount():
    """
    Function will prompt the user for a donation amount
    :return: donation_amount - the amount donated by the donor
    """
    print()
    try:
        # Once a name has been selected, prompt for a donation amount.
        # Turn the amount into a number – it is OK at this point for the
        # program to crash if someone types a bogus amount
        donation_amount = int(input("Please specify the donation amount:\n"
                                    "\n> "))
    except (ValueError, UnboundLocalError) as e:
        print("Please type only integers.")

    return donation_amount


def add_donation_to_user(donor_name_index, donation_amount):
    """
    Function will add the amount given to the donation history of the selected user
    :param donor_name_index: the index location of the donor
    :param donation_amount: the amount the donor donated
    :return: None
    """
    # Append the donation amount to the donor's name in the donor list data structure
    donors[donor_name_index][1].append(donation_amount)


def print_email_to_terminal(full_name, donation_amount):
    """
    Function will print the thank you email to the donor on the terminal
    :param full_name: username in lowercase
    :param donation_amount: the amount the donor donated
    :return: None
    """
    print()
    # Finally, use string formatting to compose an email thanking the donor for their generous donation.
    # Print the email to the terminal and return to the original prompt
    print("Dear {0},\n\n"
          "Thank you very much for your recent donation of ${1} to the local mailing room at our local charity.\n"
          "I would like to now invite you to subscribe to our mailing room group, so that you can learn more\n"
          "about how your support is helping us. Again, thank you very much for your support, we greatly\n"
          "appreciate it.\n\n"
          "Best regards,\n\n"
          "Mailing Group Association\n".format(full_name.title(), donation_amount))


def send_thank_you():
    """
    Function will send a thank you email and print it to the terminal
    :return: None
    """
    while True:
        resuts = input("\nFull Name:\n"
                       "\n> ")
        full_name = resuts.lower()

        if 'list' in full_name:
            show_donor_list()
            continue

        if full_name not in [row[0] for row in donors]:
            add_donor(full_name)

        donor_name_index = get_donors_index(full_name)
        donation_amount = get_donation_amount()
        add_donation_to_user(donor_name_index, donation_amount)
        print_email_to_terminal(full_name, donation_amount)

        break


def create_report():
    """
    Function will print out the report in a tabular formatted view
    :return: None
    """
    # Create header for report
    print("\n{:<10} | {:>10} | {:>10} | {:>10}".format('Donor Name', 'Total Given', 'Num Gift', 'Average Gift'))
    print("{}".format(''.join(['-' * 52])))

    # Create list that includes donor name, total given, number of gifts, and average gift as values in each row
    donors_list = [(row[0], sum(row[1]), len(row[1]), int(sum(row[1]) / len(row[1]))) for row in donors]

    # Sort total given by descending order
    ordered_donors_list = sorted(donors_list, key=lambda x: (x[1],x[1]), reverse=True)

    # Iterate through the ordered donors list and print out the results
    for items in ordered_donors_list:
        print("{:<10} $ {:>11} $ {:>10} $ {:>11}".format(*items))

    print()


def main_loop():
    """
    Function will prompt the user to choose one of the following: send a thank you email, create a report, or quit
    :return: None
    """
    while True:
        try:
            answer = int(input("Select from one of these options:\n"
                  "\n(1) Send a thank you\n"
                  "(2) Create a report\n"
                  "(3) Quit\n"
                  "\n> "))
            if answer == 3:
                break
            elif answer == 1:
                send_thank_you()
            elif answer == 2:
                create_report()
            else:
                print("\nPlease type 1, 2, or 3 only!\n")
        except ValueError as v:
            print("\nPlease enter an integer only.\n")


if __name__ == '__main__':

    # Call the main_loop function to start the program
    main_loop()