#! /usr/bin/env python
from textwrap import dedent



# Making this a global, so it can be accessed from various functions
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]



def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    # detent is helpful here so you can use a triple quoted string
    selection = input(dedent('''
      Choose an action:

      't' - Send a Thank You
      'r' - Create a Report
      'q' - Quit

      > '''))
    return selection.strip()

def donor_list():
    print("Printing donor list...")
    for donor in donor_db:
        print(donor[0])


def find_donor(name):
    for donor in donor_db:
        if name.lower().strip() == donor[0].lower().strip():
            return donor
    return None

def send_thank_you():

    while True:
        d_name = input("Enter donor's name" 
            "(or 'list' for list the donors)"
            "(or menu for exit)>").strip()
        if d_name.lower() == 'list':
            print(donor_list)
        elif d_name.lower() == 'menu':
            return
        else:
            break
    while True:
        donation = input("Enter donation amount or menu for exit>").strip()
        if donation == 'menu':
            return
        try:
            amount = float(donation)
        except:
            print("Donation is invalid")
        else:
            break

    donor = find_donor(d_name)

    if donor is None:
        donor = (d_name, [])
        donor_db.append(donor)

    donor[1].append(amount)

    print(dedent('''
          Dear {}

          Thank you for your very kind donation of ${:.2f}.
          It will be put to very good use.

          Sincerely,
           -The Team
          '''.format(donor[0],donor[1][-1])))

def create_report():
    row_list = []

    for (name, gifts) in donor_db:
        total = sum(gifts)
        num_gifts = len(gifts)
        avg_gifts = total / num_gifts
        row_list.append((name, total, num_gifts, avg_gifts))

    print("{:26s} | {:13s} | {:9s} | {:13s}".format("Donor name", "Total Donation", "Num Gifts", "Avg Gifts"))
    print("-"*70)
    for row in row_list:
        print("{:26s} | {:13.2f} | {:9d} | {:13.2f}".format(*row))

if __name__ == "__main__":
    run = "True"
    while run:
        choice = main_menu_selection()
        if choice == 't':
            send_thank_you()
        elif choice == 'r':
            create_report()
        elif choice == 'q':
            run = False
        else:
            print("error: menu selection is invalid!")



