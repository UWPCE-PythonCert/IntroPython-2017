#!/usr/bin/env python

# Data
donors_and_donations = ['Steve Jobs', [5, 10, 15], 'Bill Gates', [
    30, 40, 50], 'Barak Obama', [50], 'Donald Trump', [
    1, 2, 3], 'Melinda Gates', [10, 20, 30]]
#
# “Send a Thank You”, “Create a Report” or “quit”
#


def create_a_report():
    """ Print out a report of donors, total given number of donations
     and average donation
    """
    donor_name = []
    donor_total_given = []
    donor_total_num_of_gifts = []
    total_given = 0.0
    average_gift = []
    list_of_donations = []
    average_of_gifts = 0
    print('{:<20}|{:^15}|{:^15}|{:^15}'.format(
        'Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-' * 65)
    # Separate the individual donors and donations into separate lists
    i = 0
    while i < len(donors_and_donations):
        donor_name.append(donors_and_donations[i])
        list_of_donations.append(donors_and_donations[i + 1])
        i += 2
    # Calculate the sum of the gifts, the number of gifts, avg gift amount
    # for each donor, (each in a separate list)
    for donations in list_of_donations:
        # print(donations)
        # print(len(donations))
        i = 0
        total_given = 0
        # calculate the total given
        while i < len(donations):
            # print(donations[i])
            total_given += donations[i]
            i += 1
        average_of_gifts = total_given / len(donations)
        average_gift.append(average_of_gifts)
        donor_total_given.append(total_given)
        donor_total_num_of_gifts.append(len(donations))
    i = 0
    while i < len(donors_and_donations) // 2:
        print('{:<20}${:^15}${:^15}${:8.2f}'.format(
            donor_name[i], donor_total_given[i], donor_total_num_of_gifts[i],
            average_gift[i]))
        i += 1


def compose_email(answer, answer1):
    """ Generate a one line email with donor name and amount contributed
    """
    print('Thank you, {} for your generous donation of {}'.format
          (answer, answer1))


def print_menu():
    """Prompt the user to choose from a menu of 3 actions,
    'Send a Thank You', 'Create a Report' or 'quit'
    """
    print("Menu\n1. Send a Thank You\n2. Create a Report\n3. Quit")
    answer = input("Enter a number between 1 and 3 (e.g 3) > ")
    answer = answer.strip()
    return answer


def menu_thank_you():
    """Prompt the user for a full list of donors or to update the current list
    """
    # print(donors_and_donations)
    answer = input('Enter the full name of the donor or enter "list" for \
the list of donors, or "quit" for main menu')
    return answer


def send_a_thank_you():
    """Update the donor list with donor name and amount donated.
    or print the list out
    """
    answer = menu_thank_you()
    answer = answer.strip()
    answer1 = 0
    while True:
        if answer.lower() == 'list':
            print("The list of donors is: ")
            print(donors_and_donations[::2])
            answer = menu_thank_you()
        elif answer.lower() == 'quit':
            break
        # If donor is in the list, add the donation
        else:
            i = 0
            flag = 0
            for x in donors_and_donations:
                if x == answer:
                    print('answer is ', answer)
                    flag = 1
                    answer1 = int(
                        input("Enter the amount {} donated".format(x)))
                    donors_and_donations[i + 1].append(answer1)
                    print('donors_and_donations =', donors_and_donations)
                i += 1
            # donor not in the list
            if flag == 0:
                answer1 = int(
                    input("Enter the amount {} donated".format(answer)))
                donors_and_donations.append(answer)
                donors_and_donations.append([answer1])
            compose_email(answer, answer1)
            answer = menu_thank_you()


if __name__ == '__main__':
    answer = print_menu()
    while True:
        if answer == '3':
            break
        elif answer == '1':
            send_a_thank_you()
            answer = print_menu()
        elif answer == '2':
            create_a_report()
            answer = print_menu()
        else:
            print("You entered {}".format(answer))
            print("Menu\n1. Send a Thank You\n2. Create a Report\n3. Quit")
            answer = input("Enter a number between 1 and 3 (e.g 3) > ")
