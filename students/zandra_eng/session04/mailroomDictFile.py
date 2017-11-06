#!/usr/bin/env python3

"""
Making changes to original mailroom assignment.
Changes are:
changing list of donor names from a list to a dictionary,
adding new menu option (Send letters to everyone),
printing letters for new and existing donors,
and creating a txt file for each letter with donor's name as file's name
"""

# creating global list so it can be accessed from different functions
# donor_list is not a diction
donor_dict = {'Albert White': [1254.45, 8966.70],
              'Susan Smith': [9856.94, 1245.78],
              'Daniel Motoko': [5897.85, 20000.48],
              'Alison Dempsey': [2565.44, 500.32],
              'Patrick Johnson': [6578.55, 4879.23, 5879.99]}


def menu():
    """ print menu for user to select from """
    question = input("\nPlease select options 1, 2, or 3, 4 from the menu "
                         "or 'list' to view donor names: \n"
                         "1. Send a Thank you letter\n"
                         "2. Create a Report\n"
                         "3. Send letters to everyone\n"
                         "4. Quit\n"
                         "What's your choice?\n")
    return question

def print_donor_list():
    """ printing 0th element from dict (printing only donors' name)"""
    print("Donor Name:\n")
    for name in donor_dict:
        print(name)

def find_donor(name):
    """ finding donor's name in donor_dict and printing their information """
    for donor in donor_dict:
        # case-insenstive compare
        if name.lower() == donor.lower():
            return donor
    return None

def sort_key(item):
    """ key function used to sort the list by first (not zeroth) item"""
    return item       #removed item[1] and replaced it to 'item' for dictionary. item[1] is for list.


def print_letter(name, amount):
    """ writing a thank you letter to donor """
    print("\nDear {},\n\nThank you for your kind donation of ${}."
          "\n\nSincerely,\n\nA Team".format(name, amount))

# def letters_for_everyone():
#     """ writing a thank you letter to all donor """
#     for name, amounts in donor_list.items():
#         print("\nDear {},\n\nThank you for your kind donation of ${}."
#           "\n\nSincerely,\n\nA Team".format(name, amounts))

def letters_for_everyone():    #need to go back and put letters in txt file.
    """ writing a thank you letter to all donor """
    for name, amounts in donor_dict.items():
        new_amounts = []
        for i in amounts:
            new_amounts.append('$' + str(i))
        all_amounts = ", ".join(new_amounts)
        with open(name + ".txt", 'w') as this_file:
            this_file.write("\nDear {},\n\nThank you for your kind donation of ${} ({})."
                  "\n\nSincerely,\n\nA Team".format(name, round(sum(amounts), 2), all_amounts))


def print_report():
    """ printing a report that includes donor names, contribution amounts, sum, and average """
    report = []
    for (name, amount) in donor_dict.items():
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
    # could use while True:
    answer = input("\nPlease enter a donor's name."
                   "\nOr 'list for list of donors' names ")
    if answer == "list":
        print_donor_list()
    else:
        amounts = float(input("Enter donation amount "))
        donor = find_donor(answer)
        if donor is None:
            donor_dict[answer] = [amounts]   # code on the left is correct (incorrect: donor = (answer, [float(amounts)]))
        else:
            donor_dict[donor].append(amounts)   # import pdb; pdb.set_trace()--checking to see why can't use append

        # print a letter to thanks the donor
        print(print_letter(answer, float(amounts)))

if __name__ == "__main__":
    while True:
        select = menu()
        if select == 'list':
            print_donor_list()
        elif select == "1":
            send_thank_you()
        elif select == "2":
            print_report()
        elif select == "3":
            letters_for_everyone()
        elif select == "4":
            break
        else:
            print("Invalid entry! Select from the menu ")


