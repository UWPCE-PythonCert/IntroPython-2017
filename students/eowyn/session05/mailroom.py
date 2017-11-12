#!/usr/bin/env python

import sys

''' global variables'''
donor_names = ["Margaret Atwood", "Fred Armisen",
               "Heinz the Baron Krauss von Espy"]
donations = [[300, 555], [240, 422, 1000], [1500, 2300]]
DONORS = dict(zip(donor_names, donations))



def safe_input():
    return None

def quit_code():
    sys.exit()

def return_to_menu():
    ''' Raise a zero division error to trigger exit out of loop'''
    # raise NotImplementedError
    return True

def list_donors():
    ''' List all DONORS '''
    print("All Donors:")
    [print(x) for x in DONORS]


def generate_table():
    ''' Pretty-print a table of donor statistics '''
    [name, total, number, ave] = [[], [], [], []]
    for x in DONORS:  # loop over the keys which are donor names
        name.append(x)
        total.append(round(sum(DONORS[x])))
        number.append(len(DONORS[x]))
        ave.append(round(total[-1] / number[-1]))
    report_data = list(zip(name, total, number, ave))
    report_data = sorted(
        report_data, key=lambda y: int(y[1]), reverse=True)
    print_table(report_data)


def send_letters():
    ''' Send thank you notes to everyone in the DONORS dict'''
    for donor in DONORS:
        outfile = donor.replace(" ", "_") + '.txt'
        with open(outfile, 'w') as f:
            f.write(generate_letter(donor))
    print("Successfully saved letters for each donor.")


def generate_letter(donor_name):
    '''
    Generate a formatted thank you note to a donor and return
    the string of the thank you note for printing or writing.
    '''
    fs = "Thank you, {}, for your generosity and recent gift of ${}."
    return fs.format(donor_name, DONORS[donor_name][-1])


def remove_inputquotes(a_string):
    '''Remove auxillary quotes to cleanse a_string'''
    a_string.replace('"', '')
    a_string.replace('"', '')
    return a_string


def print_table(list_data):
    ''' Pretty-print the donor records '''
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    fs1 = '|'.join(["{:<40}", "{:<12}", "{:<10}", "{:<12}"])
    width = len(fs1.format(*headers))
    fs2 = ''.join(["{:<40}", "${:^12.2f}", "{:^12d}", "${:^12.2f}"])
    print(fs1.format(*headers))
    print(width * "-")
    for i in range(len(list_data)):
        entry = list_data[i]
        print(fs2.format(*entry))

def update_donor():
    '''
    Add new donation to DONORS; if new donor, add to DONOR.
    Then print a thank-you note for the donation.
    '''
    fullname = input("Enter a donor name (new or existing):\n")
    fullname = remove_inputquotes(fullname)
    if fullname in DONORS:
        print("Existing Donor")
        DONORS[fullname].append(float(input("Donation amount: ")))
        print(generate_letter(fullname))
    else:
        print("New Donor")
        DONORS[fullname] = [float(input("Donation amount: "))]
        print(generate_letter(fullname))

def thank_you():
    ''' Update donor records and print thank you notes.'''
    arg_dict = {"1": update_donor, "2": list_donors, "3": return_to_menu}

    while True:
        try:
            answer = input("To send a thank you, select one:\n "
                           "(1) Update donor and send thank-you\n"
                           "(2) List all existing DONORS\n"
                           "(3) Return to main menu\n >")
        except (EOFError, KeyboardInterrupt, TypeError):
            safe_input()
        else:
            try:
                result = arg_dict.get(answer)()
            # errors are for if key doesn't exist or is None
            except (KeyError, TypeError):
                continue
            else:
                if result:
                    return


def print_report():
    ''' Print donor report or return to menu '''
    arg_dict = {"1": generate_table, "2": return_to_menu}
    try:
        while True:
            try:
                choice = input("Select one:\n"
                               "(1) Generate a summary report\n"
                               "(2) Return to the main menu\n")
            except (EOFError, KeyboardInterrupt):
                safe_input()
            try:
                arg_dict.get(choice)()
            except (KeyError, TypeError):
                # errors are for if key doesn't exist or is None
                continue
    except ZeroDivisionError:
        pass


def mainloop():
    ''' main interactive loop
    "send a thank you" "create a report" or "quit"
    '''
    arg_dict = {"1": thank_you, "2": print_report,
                "3": send_letters, "4": quit_code}
    while True:
        try:
            answer = input("Select from one of these options: \n"
                           "(1) Send a Thank You\n"
                           "(2) Create a Report\n"
                           "(3) Send letters to everyone\n"
                           "(4) Quit\n>")
        except (EOFError, KeyboardInterrupt):
            safe_input()
        else:
            try:
                arg_dict.get(answer)()
            except (KeyError, TypeError):
                # errors are for if key doesn't exist or is None
                continue

if __name__ == "__main__":
    print("starting...")
    mainloop()
