#!/usr/bin/env python

import sys

#  --------------------------------------------------------------
# GLOBAL VARIABLE: DONORS is the database of donor names, amounts
# -------------------------------------------------------------------

donor_names = ["Margaret Atwood", "Fred Armisen",
               "Heinz the Baron Krauss von Espy"]
donations = [[300, 555], [240, 422, 1000], [1500, 2300]]
DONORS = dict(zip(donor_names, donations))
del donor_names
del donations


# --------------------------------------------------------------
# Following are helper functions to control program flow
# -------------------------------------------------------------------


def safe_input():
    return None


def quit_code():
    sys.exit()


def return_to_menu():
    ''' Return True to trigger exit out of sub-loop'''
    return True


# --------------------------------------------------------------
# Following are helper functions for generating reports
# -------------------------------------------------------------------


def generate_report_data():
    [name, total, number, ave] = [[], [], [], []]
    for x in DONORS:  # loop over the keys which are donor names
        name.append(x)
        total.append(round(sum(DONORS[x])))
        number.append(len(DONORS[x]))
        ave.append(round(total[-1] / number[-1]))
    report_data = list(zip(name, total, number, ave))
    report_data = sorted(
        report_data, key=lambda y: int(y[1]), reverse=True)
    return report_data


def generate_table():
    ''' Pretty-print a table of donor statistics '''
    print_table(generate_report_data())


def setup_table():
    ''' Set up the donor record table headers '''
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    fs1 = '|'.join(["{:<40}", "{:<12}", "{:<10}", "{:<12}"])
    width = len(fs1.format(*headers))
    head = (fs1.format(*headers)) + '\n'
    head = head + (width * "-") + '\n'
    return head


def setup_body(list_data):
    ''' Set up the donor records table body '''
    body = ""
    fs2 = ''.join(["{:<40}", "${:^12.2f}", "{:^12d}", "${:^12.2f}"])
    for i in range(len(list_data)):
        entry = list_data[i]
        body = body + fs2.format(*entry) + '\n'
    return body


def print_table(list_data):
    ''' Pretty-print the donor records '''
    print(setup_table())
    print(setup_body(list_data))


# --------------------------------------------------------------
# Following are helper functions for adding donations to DONORS and
# sending thank you notes to donors
# -------------------------------------------------------------------


def collect_donor_input():
    ''' Get name and donation amount to add to DONORS'''
    fullname = input("Enter a donor name (new or existing):\n")
    fullname = remove_inputquotes(fullname)
    amount = float(input("Donation amount: "))
    return (fullname, amount)


def retrieve_donations(fullname):
    ''' if donor exists, return donations, otherwise, return None'''
    if fullname in DONORS:
        return DONORS[fullname]


def add_donation(fullname, amount):
    ''' Update donor if it exists or add new donor if it does not'''
    DONORS.setdefault(fullname, []).append(amount)


def update_donors():
    '''
    Add new donation to DONORS; if new donor, add to DONOR.
    Then print a thank-you note for the donation.
    '''
    (fullname, amount) = collect_donor_input()
    add_donation(fullname, amount)
    print(generate_letter(fullname))


def list_donors():
    ''' List all DONORS '''
    print(make_donor_list())


def make_donor_list():
    ''' generate string of donor names '''
    outputstr = ""
    return ("Donor Names:" + "".join([outputstr + '\n' + x for x in DONORS]))


def generate_letter(donor_name):
    '''
    Generate a formatted thank you note to a donor and return
    the string of the thank you note for printing or writing.
    '''
    fs = "Thank you, {}, for your generosity and recent gift of ${}."
    return fs.format(donor_name, DONORS[donor_name][-1])


# --------------------------------------------------------------
# Following are helper functions for accepting and responding to
# keyboard input
# -------------------------------------------------------------------


def remove_inputquotes(a_string):
    '''Remove auxillary quotes to cleanse a_string'''
    a_string.replace('"', '')
    return a_string


def get_user_input(prompt_string):
    ''' Print a prompt_string, return keyboard input if no exceptions'''
    try:
        answer = input(prompt_string)
    except (EOFError, KeyboardInterrupt, TypeError):
        return None
    else:
        return answer


def select_action(arg_dict, answer):
    ''' Execute an action from arg_dict that corresponds to answer.
    Return None if action was executed and False if an error occurs'''
    try:
        return arg_dict[answer]()
    except (KeyError):
        return False


# --------------------------------------------------------------
# Following are primary actions called by MAINLOOP
# --------------------------------------------------------------


def send_letters():
    ''' Send thank you notes to everyone in the DONORS dict'''
    for donor in DONORS:
        outfile = donor.replace(" ", "_") + '.txt'
        with open(outfile, 'w') as f:
            f.write(generate_letter(donor))
    print("Successfully saved letters for each donor.")


def run_interactive_loop(arg_dict, prompt_string):
    while True:
        answer = get_user_input(prompt_string)
        if answer:
            result = select_action(arg_dict, answer)
            if result:
                    return


def thank_you_loop():
    ''' Primary loop to update and thank DONORS
    update DONORS, print donor names, or return to main menu
    '''
    arg_dict = {"1": update_donors, "2": list_donors, "3": return_to_menu}
    prompt_string = """To send a thank you, select one:\n
    (1) Update donor and send thank-you\n
    (2) List all existing DONORS\n
    (3) Return to main menu\n >"""
    run_interactive_loop(arg_dict, prompt_string)


def print_report_loop():
    ''' Primary reporting loop
    "generate report table" or "return to main menu"
    '''
    arg_dict = {"1": generate_table, "2": return_to_menu}
    prompt_string = """Select one:\n
    (1) Generate a summary report\n
    (2) Return to the main menu\n"""
    run_interactive_loop(arg_dict, prompt_string)


# --------------------------------------------------------------
# The MAINLOOP to control the entire program
# -------------------------------------------------------------------


def mainloop():
    ''' main interactive loop
    "send a thank you" "create a report" or "quit"
    '''
    arg_dict = {"1": thank_you_loop, "2": print_report_loop,
                "3": send_letters, "4": quit_code}
    prompt_string = """Select from one of these options: \n
    (1) Send a Thank You\n
    (2) Create a Report\n
    (3) Send letters to everyone\n
    (4) Quit\n>"""
    run_interactive_loop(arg_dict, prompt_string)


if __name__ == "__main__":
    print("starting...")
    mainloop()
