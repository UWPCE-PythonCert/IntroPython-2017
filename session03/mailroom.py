#!/usr/bin/env python3

"""
Mailroom
A complete program

Using Python’s basic data types and logic for a full program.
Goal:

You work in the mail room at a local charity. Part of your job is to write incredibly boring,
repetitive emails thanking your donors for their generous gifts. You are tired of doing this
over an over again, so you’ve decided to let Python help you out of a jam and do your work for you.
The program

Write a small command-line script called mailroom.py. This script should be executable.
The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a history of the amounts they have donated.
    This structure should be populated at first with at least five donors, with between 1 and 3 donations each.

    You can store that data structure in the global namespace.

    The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”,
    “Create a Report” or “quit”)

Sending a Thank You

    If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        If the user types ‘list’, show them a list of the donor names and re-prompt
        If the user types a name not in the list, add that name to the data structure and use it.
        If the user types a name in the list, use it.
        Once a name has been selected, prompt for a donation amount.
        Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
        Once an amount has been given, add that amount to the donation history of the selected user.
        Finally, use string formatting to compose an email thanking the donor for their generous donation.
        Print the email to the terminal and return to the original prompt.

It is fine (for now) to forget new donors once the script quits running.
Creating a Report

    If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
        Include Donor Name, total donated, number of donations and average donation amount as values in each row.
        You do not need to print out all their donations, just the summary info.
        Using string formatting, format the output rows as nicely as possible.
        The end result should be tabular (values in each column should align with those above and below)
        After printing this report, return to the original prompt.
    At any point, the user should be able to quit their current task and return to the original prompt.
    From the original prompt, the user should be able to quit the script cleanly

Your report should look something like this:

Donor Name                | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------
William Gates, III         $  653784.49           2  $   326892.24
Mark Zuckerberg            $   16396.10           3  $     5465.37
Jeff Bezos                 $     877.33           1  $      877.33
Paul Allen                 $     708.42           3  $      236.14

Guidelines

First, factor your script into separate functions. Each of the above tasks can be accomplished by a series of steps.
Write discreet functions that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program.
Interactive programs are a classic use-case for the while loop.

Of course, input() will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an if __name__ == '__main__' block.

Finally, use only functions and the basic Python data types you’ve learned about so far.
There is no need to go any farther than that for this assignment.
Submission

As always, put the new file in your student directory in a session03 directory, and add it to your clone early.
Make frequent commits with good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.
Adding dicts…

Wait to do this till after you’ve learned about dictionaries next week!

For the next week

You should have been able to do all that with the basic data types:

numbers, strings, lists and tuples.

But once you’ve learned about dictionaries, you may be able to re-write it a bit more simply and efficiently.

        Update your mailroom program to:

            Use dicts where appropriate
            Write a full set of letters to everyone to individual files on disk
            See if you can use a dict to switch between the users selections
            Try to use a dict and the .format() method to do the letter as one big template –
            rather than building up a big string in parts.

Example:

In [3]: d
Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


In [5]: "My name is {first_name} {last_name}".format(**d)
Out[5]: 'My name is Chris Barker'

Don’t worry too much about the “**” – we’ll get into the details later, but for now, it means, more or less,
– pass this whole dict in as a bunch of keyword arguments.
Adding Exceptions and Testing

After Session05

Once you once you’ve learned about Exception handling, testing, and comprehensions,
you should be able to refactor your code to be more robust.
Tests

Add a full suite of unit tests.

“full suite” means all the code is tested. In practice, it’s very hard to test the user interaction,
but you can test everything else. Make sure that there is as little untested code in the user interaction
portion of the program – hardly any logic.

This is a big step – you may find that your code is hard to test. If that’s the case,
it’s a good sign that you should refactor your code.

I like to say: “If it’s hard to test, it’s not well structured”

Put in the tests before you make the other changes below - that’s much of the point of tests –
you can know that you haven’t broken anything when you refactor!
Exceptions-

Now that you’ve learned about exception handling, you can update your code to handle errors better –
like when a user inputs bad data.
Comprehensions

Can you use comprehensions to clean up your code a bit?

"""

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

def donor_name():
    """ collecting donor name"""
    name = input("Please enter donor name: ")
    return name

def donate_amount():
    """ collecting gift amount from donor """
    amount = input("How much would you like to donate? ")
    return amount

def print_letter():
    """ writing a thank you letter to donor """
    print("\nDear {},\n\nThank you for your kind donation of ${}."
          "\n\nSincerely,\n\nA Team".format(donor_name(), donate_amount()))

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
    while True:
        answer = input("\nPlease enter a donor's name."
                       "\nOr 'list for list of donors' names ")
        if answer == "list":
            print_donor_list()
        elif answer == donor_list:
            amount = input("Enter donation amount ")
            donor_list[0] += answer
            donor_list[1] += amount
        else:
            break

        donor = find_donor(answer)
        if donor is None:
            donor = (answer, [])
            donor_list.append(donor)

    # print a letter to thanks the donor
    print(print_letter())

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


