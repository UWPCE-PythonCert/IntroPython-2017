import os
import model as Mod
import json

def open_json(filename):
    '''Opens a JSON file and returns the JSON data as a dictionary.'''
    with open(filename) as f:
        read_data = f.read()
    jsondict = json.loads(read_data)
    records = {}
    for key, value in jsondict.items():
        record = Mod.Donor(key, value)
        records[key] = record
    return records


def write_json(records, filename):
    '''Write dictionary as JSON to the target filename.'''
    #flatten records
    jsondata = {}
    for key, value in records.items():
        jsondata[key] = value.Donations
    outdata = json.dumps(jsondata)
    fout = open(filename, "w")
    for line in outdata:
        fout.write(line)
    fout.close()


def make_thanks(name, donation):
    '''Takes the name and donation and return a thank you text.'''
    thankyou = '''
    Dear {},

    Thank you for your generous donation of $ {}. Your
    support enables us to keep doing good in the world. Which means
    your money, earned through whatever means money is earned in
    the amounts you have earned, is now doing good. We thank you. The
    world thanks you.

    Regards,
    Foundation Against Suffering

    '''.format(name, donation)
    return thankyou


def send_thanks(records, filename, thanks="", amount=0):
    '''Send a thank you card.
    X If the user types ‘list’, show them a list of the donor names and re-prompt
    X If the user types a name not in the list, add that name to the data structure and use it.
    X f the user types a name in the list, use it.
    X Once a name has been selected, prompt for a donation amount.
    X Turn the amount into a number – it is OK at this point for
        the program to crash if someone types a bogus amount.
    X Once an amount has been given, add that amount to the donation history of the
         selected user.
    X Finally, use string formatting to compose an email thanking
        the donor for their generous donation. Print the email to the terminal and
        return to the original prompt.'''
    print("Thanks...")
    thanks = input("Type \'List\' for a list of donors, or a name to thank. > ")
    if thanks.lower() == "list":
        for key in records.items():
            print(key[0])
        run = True
        return run
    else:
        try:
            amount = float(input("Type a donation amount. > "))
            if thanks in records:
                records[thanks] + amount
            else:
                record = Mod.Donor("thanks", [amount])
                records[thanks] = record
            print(make_thanks(thanks, amount))
            run = True
            return True
        except TypeError():
            print("Please type a donation amount using a number.")

            run = True
            return run

def create_report(records, filename):
    '''If the user (you) selected “Create a Report”, print a list of
        your donors, sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and
        average donation amount as values in each row. You do
        not need to print out all their donations, just the summary info.
    Using string formatting, format the output rows as nicely as
    possible. The end result should be tabular (values in each
    column should align with those above and below)
    After printing this report, return to the original prompt.'''
    print("\nREPORT\nDonor      \t\tNo\tAverage\tTotal\n")
    for key, value in records.items():
        print("{}\t\t{}\t{}\t{}".format(
            key, value.DonationNumber, value.AverageDonations, value.DonationTotal))
    print("\n")
    run = True
    return run


def exit_mail(records, filename):
    '''Save the data; close the app.'''
    try:
        write_json(records, filename)
    except:
        print("Failed to write file.")
    print("Goodbye.")
    run = False
    return run


def test(records, filename):
    '''temporary method to print data store.'''
    for key, value in records.items():
        print("{} : {}".format(key, value.Donations))

    run = True
    return run


# Menu choices

chooser = {
    "1": ("Send a Thank You",send_thanks),
    "2": ("Create a Report",create_report),
    "3": ("Quit",exit_mail),
    "4": ("Test",test)
    }


def mainloop(records, filename):
    '''Central loop of the app.'''
    run = True
    while run == True:
        try:
            for k in chooser.keys():
                print("{} | {}".format(k, chooser[k][0]))
            sel = input("Type a choice. > ")
            run = chooser[sel][1](records, filename)
        except:
            print("Please type a valid choice.")


if __name__ == "__main__":
    print ("Starting...")
    try:
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, 'data\mailroomdata.json')
        records = open_json(filename)
        print ("Data loaded.")
        mainloop(records, filename)
    except:
        print ("Unable to find source file.")
