'''Session 5 Mailroom3
    Matt Briggs
    '''

import json

def open_json(filename):
    '''Opens a JSON file and returns the JSON data as a dictionary.'''
    with open(filename) as f:
        read_data = f.read()
    jsondict = json.loads(read_data)
    return jsondict


def write_json(jsondata, filename):
    '''Write dictionary as JSON to the target filename.'''
    outdata = json.dumps(jsondata)
    fout = open(filename, "w")
    for line in outdata:
        fout.write(line)
    fout.close()

def send_thank():
    '''Send a thank you card.
    X If the user types ‘list’, show them a list of the donor names and re-prompt
    X If the user types a name not in the list, add that name to the data structure and use it.
    X f the user types a name in the list, use it.
    X Once a name has been selected, prompt for a donation amount.
    X Turn the amount into a number – it is OK at this point for the program to crash if someone types a bogus amount.
    X Once an amount has been given, add that amount to the donation history of the selected user.
    X Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.'''
    print("Thanks...")
    thanks = input("Type \'List\' for a list of donors, or a name to thank. > ")
    if thanks.lower() == "list":
        for name in maildata.keys():
            print (name)
    else:
        try:
            amount = float(input("Type a donation amount. > "))
            if thanks in maildata:
                maildata[thanks] += [amount]
            else:
                maildata[thanks] = [amount]
            thankyou = '''
                                        Dear {},

                                        Thank you for your generous donation of $ {}. Your
                                        support enables us to keep doing good in the world. Which means
                                        your money, earned through whatever means money is earned in
                                        the amounts you have earned, is now doing good. We thank you. The
                                        world thanks you.

                                        Regards,
                                        Foundation Against Suffering

                                        '''.format(thanks, amount)
            print(thankyou)
        except:
            print("Please type a donation amount using a number.")

def create_report():
    '''If the user (you) selected “Create a Report”, print a list of your donors, sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
    Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
    After printing this report, return to the original prompt.'''
    print("Report...")

def quit():
    '''Save the data; close the app.'''
    write_json(maildata, persistantdata)
    print("Goodbye.")

def test():
    '''temporary method to print data store.'''
    print(maildata)

def mainloop():
    '''Central loop of the app.'''
    run = True
    while run == True:
        try:
            for k in chooser.keys():
                print("{} | {}".format(k, chooser[k][0]))
            sel = input("Type a choice. > ")
            chooser[sel][1]()
            if sel == "3":
                break
        except:
            "Please type a valid choice."

# Menu choices

chooser = {
    "1": ("Send a Thank You",send_thank),
    "2": ("Create a Report",create_report),
    "3": ("Quit",quit),
    "4": ("Test",test)
    }

persistantdata = "mailroomdata.json"

if __name__ == "__main__":
    print ("Starting...")
    try:
        maildata = open_json(persistantdata)
        print ("Data loaded.")
    except:
        print ("Unable to find source file.")
    mainloop()