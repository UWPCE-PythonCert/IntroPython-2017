#!/usr/bin/env python

donors = [("John Doe", [152.33, 700]), ('Jane Doe', [23.19, 50, 15.99])]

def main_loop():
    """ Main menu to call different functions """

    while True:
        print("\n========== Donation Management System Main Menu ==========")
        print("*                 1. Send a Thank You                    *")
        print("*                 2. Create a Report                     *")
        print("*                 3. Quit                                *")
        print("==========================================================")
        result = input("Please select a menu item: ")
        if result == '1':
            thank_you()
        elif result == '2':
            report()
        elif result == '3':
            break
        else:
            print("\n*** Selected item not in the menu. Please try again. ***\n")

def donor_search(n):
    """ Search donor by name, return donor tuple """
    for donor in donors:
        if donor[0].lower() == n.lower():
            return donor
    return None


def email(n):
    """ Send donor an email with latest donation """
    print("""
        Dear {},

        Thank you for your recent generous donation of ${}.
        Your support encourages our continued commitment to reaching our goal.

        Sincerely,
        The Donation Management
        """.format(donor_search(n)[0], donor_search(n)[1][-1]))

def thank_you():
    """ Thank you function """
    while True:
        result = input("\nPlease enter full name, 'list' for current donor list, or 'q' return to the main menu: ")

        # Print donor list
        if result == "list":
            print("Current donor list: ")
            for donor in donors:
                print(donor[0])
        # Back to the main menu
        elif result == "q":
            break
        # Add new donor listing
        elif donor_search(result) == None:
            amount = input("\nA new donor, please enter the amount of donation: ")
            donors.append((result, [float(amount)]))
            print("Donor record added - Name: {}, Donation: ${}".format(donors[-1][0], donors[-1][1][-1]))
            print("\nSending Thank You email...")
            email(result)
        # Existing donor, add new donation
        else:
            amount = input("Existing donor: {}\nPlease enter the amount of donation: ".format(donor_search(result)))
            donor_search(result)[1].append(float(amount))
            print("New Donation Added: {}".format(donor_search(result)))
            print("\nSending Thank You email...")
            email(result)

def report():
    """ Generate report """
    print("\n* Donor Name                  |     Total gifted     | Donations |  Average gifted *")
    print("====================================================================================")
    for donor in donors:
        # Total amount
        total = 0.0
        for i in donor[1]:
            total += i
        # Number of donations
        don = len(donor[1])

        # Average donation
        avg = total/don

        # Print report
        print("* {: <30}{:16.2f}{: >16}{:18.2f} *".format(donor[0], total, don, avg))
    print("====================================================================================")



if __name__ == '__main__':
    """ Main function """
    main_loop()
