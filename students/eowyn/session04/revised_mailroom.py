#!/usr/bin/env python

import sys

''' global variables'''
donor_names = ["Margaret Atwood", "Fred Armisen",
               "Heinz the Baron Krauss von Espy"]
donations = [[300, 555], [240, 422, 1000], [1500, 2300]]
DONORS = dict(zip(donor_names, donations))


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
        try:
            arg_dict.get(answer)()
        except KeyError:
            continue


def safe_input():
    return None

def quit_code():
    sys.exit()


def thank_you():
    ''' Update donor records and print thank you notes.'''
    while True:
        try:
            fullname = input("To send a thank you, "
                             "Enter a donor name (new or existing)\n"
                             "Enter all to list existing DONORS \n"
                             "Enter menu to return to main menu \n >")
        except (EOFError, KeyboardInterrupt):
            safe_input()

        fullname = remove_inputquotes(fullname)
        if fullname == 'menu':
            break
        if fullname.lower() == 'all':
            print("All Donors:")
            [print(x) for x in DONORS]
        elif fullname in DONORS:
            print("Existing Donor")
            DONORS[fullname].append(float(input("Donation amount: ")))
            print(generate_letter(fullname))
        else:
            print("New Donor")
            # must be a list to append later
            DONORS[fullname] = [float(input("Donation amount: "))]
            print(generate_letter(fullname))


def print_report():
    ''' Pretty-print a table of donor statistics '''
    while True:
        try:
            choice = input("To generate a summary report, \n"
                           "type run now.\n"
                           "To return to the main menu,\n"
                           "type menu now>")
        except (EOFError, KeyboardInterrupt):
            safe_input()
        choice = remove_inputquotes(choice)
        if choice == 'menu':
            break
        else:
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
    '''check for and remove anxillary quotes'''
    if a_string[0] == a_string[-1] == '"' or a_string[0] == a_string[-1] == "'":
        a_string = a_string[1:-1]
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


if __name__ == "__main__":
    print("starting...")
    mainloop()
