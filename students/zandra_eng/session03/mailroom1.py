#!/usr/bin/env python3



# creating global list so it can be accessed from different functions
donor_list = [('Albert White', [1254.45, 8966.70]),
              ('Susan Smith', [9856.94, 1245.78]),
              ('Daniel Motoko', [5897.85, 20000.48]),
              ('Alison Dempsey', [2565.44, 500.32]),
              ('Patrick Johnson', [6578.55, 4879, 5879.99])]


def menu():
    """ print menu for user to select from """
    question = input("\nPlease select options 1, 2, or 3 from the menu "
                         "or 'list' to view donor names: \n"
                         "1. Send a Thank you letter\n"
                         "2. Create a Report\n"
                         "3. Quit\n"
                         "What's your choice? ")
    return question

def print_donor_list():
    """ printing 0th element from list (printing only donors' name)"""
    print("Donor Name:\n")
    for name in donor_list:
        print(name[0])

def find_donor(name):
    """ finding donor name in donor_list and printing their information """
    for donor in donor_list:
        # case-insenstive compare
        if name.lower() == donor[0].lower():
            return donor
    return None

def sort_key(item):
    """ key function used to sort the list by first (not zeroth) item"""
    return item[1]

def print_letter(name, amount):
    """ writing a thank you letter to donor """
    print("\nDear {},\n\nThank you for your kind donation of ${}."
          "\n\nSincerely,\n\nA Team".format(name, amount))

def print_report():
    """ printing a report that includes donor names, contribution amounts, sum, and average """
    report = []
    for (name, amount) in donor_list:
        total_amount = sum(amount)
        number_gifts = len(amount)
        avg_gift = total_amount / number_gifts
        report.append((name, total_amount, number_gifts, avg_gift))

    # sorting report data A-Z
    report.sort(key=sort_key)
    # printing report in a nicer format
    print("{:25s} | {:11s} | {:9s} | {:12s}".format(
        "\nDonor Name", "Total amount", "# of Gifts", "Average amount"))
    print("-" * 70)
    for row in report:
        print("{:25s}   {:11.2f}   {:9d}   {:12.2f}".format(*row))

def send_thank_you():
    """" Asking user to select from the following options: Send a Thank You, "Create a report" or "quit" """
 #   while True:
    answer = input("\nPlease enter a donor's name."
                   "\nOr 'list for list of donors' names ")
    if answer == "list":
        print_donor_list()
    else:
        amount = input("Enter donation amount ")
        donor = find_donor(answer)
        if donor is None:
            donor = (answer, [float(amount)])
            donor_list.append(donor)
        else:
            donor[1].append(float(amount))

    # print a letter to thanks the donor
    print(print_letter(answer, amount))

if __name__ == "__main__":
    run = True
    while run:
        select = menu()
        if select == 'list':
            print_donor_list()
        elif select == "1":
            send_thank_you()
        elif select == "2":
            print_report()
        elif select == "3":
            run = False
        else:
            print("Invalid entry! Select from the menu ")


