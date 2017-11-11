#!/usr/bin/env python

import sys
import io

""" Program to manage donations. """

# Define the static donor list
donors = [ 
        { "last_name": "Smith", "first_name": "Joe", 
            "donations": [ 
                { "amount": 10000.00 }, { "amount": 2100.00 }, { "amount": 2330.20 } ] },
        { "last_name": "Gates, III", "first_name": "William",
            "donations": [
                { "amount": 326892.00 }, { "amount": 326892.49 } ] },
        { "last_name": "Zuckerberg", "first_name": "Mark",
            "donations": [
                { "amount": 5000.00 }, { "amount": 5000.00 }, { "amount": 6396.10 }  ] },
        { "last_name": "Bezos", "first_name": "Jeff",
            "donations": [
                { "amount": 877.33 } ] },
        { "last_name": "Allen", "first_name": "Paul",
            "donations": [
                { "amount": 10.00 }, { "amount": 600.00 }, { "amount": 98.42} ] },
        { "last_name": "Adams", "first_name": "Georgia", 
            "donations": [
                { "amount": 200 }, { "amount": 500 }, { "amount": 200000 }, { "amount": 700 } ] }
         ]


def safe_input(prompt=">"):
    """ Generic input routine. """
    # return null if anything goes wrong
    selection=""
    try:
        selection=input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        # don't exit the program on ctrl-c, ctrl-d
        pass
    return selection


def print_lines(lines=2,dest=sys.stdout):
    """ Print variable number of linefeeds for clarity. """

    for i in range(lines):
        print("",file=dest)


def print_report():
    """ Print formatted list of all donors. """

    print_lines()
  
    # print report header
    #      index    name   total gvn #gifts  avg gift
    print("{0:5} | {1:20} | {2:14} | {3:9} | {4:12}".format(
        "ID","Donor Name","Total Given","Num Gifts","Average Gift"))
    print("-"*72)

    # enumerate so we have the list index handy
    for donor_index, donor in enumerate(donors):

        num_donations=len(donor["donations"])

        total_donations = 0
        for donation in donor["donations"]:
            total_donations += donation["amount"]

        average_donation = total_donations / num_donations

        #      index      name     total gvn    #gifts    avg gift
        print("{0:05d}   {1:20}  ${2:14,.2f}   {3:9.0f}  ${4:12,.2f}".format(
            donor_index,donor["first_name"]+" "+donor["last_name"],
            total_donations,num_donations,average_donation))


def parse_name(full_name):
        """ Convert string name into constituent parts. """

        # capture suffix, if present.  we assume it will follow a comma
        try:
            suffix=full_name.split(",")[1].strip()
        except:
            suffix=""

        # name with suffix removed
        informal_name=full_name.split(",")[0].strip()
        # we assume the last name is one word minus the suffix
        last_name=informal_name.split()[-1].strip()
        # we assume the first name(s) is everything to the left of the last name
        first_name=" ".join(informal_name.split()[0:-1])

        return { "full_name": full_name.title(), "informal_name": informal_name.title(),
            "suffix": suffix.upper(), "last_name": last_name.title(), "first_name": first_name.title() }


def get_donation_amount(informal_name):
    """ Get a donation. """

    menu =  "\n"
    menu += "GIFT ENTRY (ammount)\n"
    menu += "-----------------------\n"
    menu += "\n"
    menu += "Enter the numeric amount {} has donated or\n"
    menu += "(q)uit to return to cancel the donation and\n"
    menu += "return to the previous menu.\n"
    menu += "\n"

    amount=0
    while amount==0:

        print_lines()

        print(menu.format(informal_name))
        selection=safe_input("Donation amount or (q)uit: ")

        # let them bail if they want
        if selection.lower() in ["q", "quit"]:
            return None

        # protect against non numeric input
        try:
            amount=float(selection)
            return amount
        except ValueError:
            print_lines()
            print("The value must be numeric.  Please try again or (q)uit.")


def print_thank_you(donor_id,hint="wonderful",dest=sys.stdout):
    """ Print a thank you letter. """

    letter =  "\n"
    letter += "Dearest {first_name} {last_name},\n"
    letter += "\n"
    letter += "We are are grateful for the generious donation on the behalf of\n"
    letter += "the {last_name} family.\n"
    letter += "\n"
    letter += "It is through the donations of {} patrions like yourself that\n"
    letter += "allows us to continue to support the community.\n"
    letter += "\n"
    letter += "Sincerely,\n"
    letter += "\n"
    letter += "Tux Humboldt\n"
    letter += "Shark Loss Prevention Institue\n"

    print_lines(2,dest)
    print("-"*80,file=dest)

    print(letter.format(hint,**donors[donor_id]),file=dest)

    print("-"*80,file=dest)
    print_lines(2,dest)


def thank_you_entry():
    """ Enter new donation and send thank you. """

    menu =  "\n"
    menu += "DONATION ENTRY (Donor Name)\n"
    menu += "---------------------------\n"
    menu += "\n"
    menu += "Enter the full name (first, last) of the donor\n"
    menu += "for whom you would like to enter a donation,\n"
    menu += "(l)ist to see a list of the existing donors, or\n"
    menu += "(q)uit to return to the previous menu.\n"
    menu += "\n"

    while True:

        print_lines()

        print(menu)
        selection=safe_input("Donor Name, (l)ist or (q)uit: ")

        # check for a quit directive
        if selection.lower() in ["q", "quit"]:
            return

        # check for a list directive
        if selection.lower() in ["l", "list"]:
            print_report()
            continue

        # parse the string into name components
        current_donor=parse_name(selection)

        # determine if the provided name matches an existing record
        donor_id=None
        for donor_index, existing_donor in enumerate(donors):
            # assemble full name from first_name, last_name
            existing_full_name = existing_donor["first_name"]+" "+existing_donor["last_name"]
            # if we get a match, store the index of the donor record
            if existing_full_name.lower().strip() == current_donor["full_name"].lower().strip():
                donor_id=donor_index

        # prompt for new donation, cancel if None returned
        new_donation=get_donation_amount(current_donor["informal_name"])
        if new_donation is None:
            print_lines()
            print("Donation cancelled!")
            return

        # donor_id will be None if it didn't match an existing entry

        # add donation to an existing donor
        if donor_id is not None:
            donors[donor_id]["donations"].append({ "amount": new_donation})
            hint="returning"
            #print("existing donor:",donors[donor_id])

        # add a new donor
        else:
            donors.append( { "last_name": ", ".join(filter(None,[current_donor["last_name"], current_donor["suffix"]])),
                "first_name": current_donor["first_name"],
                "donations": [ { "amount": new_donation} ] } )
            # set the donor_id to the new donor
            donor_id=len(donors)-1
            hint="new"
            #print(donors[donor_id])

        # thank the donor for the new donation
        print_thank_you(donor_id,hint)


def thank_all_donors():
    for index in range(len(donors)):
        #dest=sys.stdout
        donor_name = donors[index]["last_name"]+"_"+donors[index]["first_name"]
        donor_name = donor_name.strip().lower().replace(" ", "_").replace(",", "")
        donor_file="thank_you_" + donor_name
        dest = open(donor_file, "w")
        print_thank_you(index,"wonderful",dest)
        dest.close()

def main():
    """ Main menu / input loop. """
    

    menu =  "\n"
    menu += "DONATION WIZARD MAIN MENU\n"
    menu += "-------------------------\n"
    menu += "\n"
    menu += "Select from the following:\n"
    menu += "\n"
    menu += "(L)ist Donors\n"
    menu += "(E)nter Donation\n"
    menu += "(P)rint Donor Letters\n"
    menu += "(Q)uit\n"
    menu += "\n"

    selection=None
    while selection not in ["0", "quit", "q"]:

        print_lines()

        print(menu)
        selection=safe_input("(l)ist, (e)nter, (q)uit: ").lower()

        if selection in ["1", "l", "list"]:
            print_report()

        if selection in ["p", "print"]:
            thank_all_donors()

        # accept either send or enter
        if selection in ["2", "s", "send", "e", "enter"]:
            thank_you_entry()

        if selection in ["d", "debug"]:
            print_lines()
            print("Donors:", donors)

    print_lines()
    print("Thank you for using Donation Wizard!")
    print_lines()


def print_fatal(routine="importaint"):
    """ Upon fatal error, print message and exit. """
    print("The {} function has malfunctioned.  Contact customer support!".format(routine))
    sys.exit(1)


def sanity_tests():

    # verify the parse_name() function
    try:
        assert parse_name("Mary Jo Smith, IV") == {
            'full_name': 'Mary Jo Smith, Iv', 
            'informal_name': 'Mary Jo Smith',
            'suffix': 'IV',
            'last_name': 'Smith',
            'first_name': 'Mary Jo' }
    except AssertionError:
        print_fatal("parse_name()")

    # verify the print_lines() function
    out = io.StringIO()
    print_lines(3,out)
    output = out.getvalue()
    out.close()
    try:
        assert output == "\n\n\n"
    except AssertionError:
        print_fatal("print_lines()")

    # verify the print_thank_you() function
    out = io.StringIO()
    print_thank_you(0,"testfull",out)
    output = out.getvalue()
    out.close()
    try:
        assert "Dearest Joe Smith," in output
    except AssertionError:
        print_fatal("print_thank_you()")


if __debug__:
    sanity_tests()


# call the main input loop
if __name__ == "__main__":
    main()


