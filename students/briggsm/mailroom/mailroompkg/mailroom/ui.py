import os
import model as MD
import logging
import traceback


def send_thanks(donor_records, filename):
    ''' '''
    # get set of full names
    logging.info('Send thanks.')
    full_name_list = []
    for record in donor_records.donors:
        full_name_list.append(record.full_name)
    full_name_set = set(full_name_list)

    #get selection (list or name)
    thanks = input("Type \'List\' for a list of donors, or a full name to thank. > ")

    if thanks.lower() == "list":
        logging.info('Getting list.')
        for record in donor_records.donors:
            print(record.full_name)
        return True
    
    elif thanks in full_name_set:
        # get donation amount, add to donations, and print thank you latter.
        try:
            amount = float(input("Type a donation amount. > "))
            logging.info('Thanks to {} for {}'.format(thanks, amount))
            for record in donor_records.donors:
                if thanks == record.full_name:
                    record.donations.append(amount)
                    letter1 = MD.Letter()
                    letter1_text = letter1.create_letter(record.full_name, record.email, "User", amount)
                    print(letter1_text)
                    return True
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.info("Error: {}".format(e))
            print("Sorry there was an error. Try to thank the donor again.")
            return True

    else:
        try:
            print("A new donor!")
            first_name = input("First name > ")
            last_name = input("Last name > ")
            email = input("Email name > ")
            amount = float(input("Type a donation amount. > "))
            new_donor = MD.Donor()
            new_donor.first_name = first_name
            new_donor.last_name = last_name
            new_donor.email = email
            new_donor.donations.append(amount)
            donor_records.donors.append(new_donor)
            logging.info('Adding a new donor: {} for {}'.format(new_donor.full_name, amount))
            letter2 = MD.Letter()
            letter2_text = letter2.create_letter(new_donor.full_name, new_donor.email, "User", amount)
            print(letter2_text)
            return True
        except Exception as e:
            logging.error(traceback.format_exc())
            logging.info("Error: {}".format(e))
            print("Sorry there was an error. Try to thank the donor again.")
            return True


def create_report(donor_records, filename):
    '''Create a pretty printed report with the Report class.'''
    logging.info('Create report.')
    report = MD.Report()
    report.create_report(donor_records)
    return True


def exit_mail(donor_records, filename):
    '''Save the data; close the app.'''
    logging.info('Exiting...')
    utility = MD.Utilities()
    try:
        print("Goodbye.")
        utility.save_json(donor_records, filename)
        return False
    except Exception as e:
        logging.error(traceback.format_exc())
        logging.info("Error: {}".format(e))
        print("Failed to write file.")
        utility.spill_records(donor_records)
        return False


chooser = {
    "1": ("Send a Thank You",send_thanks),
    "2": ("Create a Report",create_report),
    "3": ("Quit",exit_mail)
    }


def mainloop(donor_records, filename):
    '''Central loop of the mailroom application.'''
    run = True
    loop_count = 0
    while run == True:
        loop_count += 1
        logging.info("loop No: {}".format(loop_count))
        try:
            for k in chooser.keys():
                print("{} | {}".format(k, chooser[k][0]))
            sel = input("Type a choice. > ")
            run = chooser[sel][1](donor_records, filename)
        except:
            print("Please type a valid menu item.")


if __name__ == "__main__":
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    logging.basicConfig(filename=fileDir + '\\data\\mailroom.log', level=logging.INFO)
    logging.info('\nStarted')
    try:
        filename = fileDir + "\\data\\mailroomdata.json"
        utility = MD.Utilities()
        donor_records = utility.open_json(filename)
        print ("Data loaded.")
        mainloop(donor_records, filename)
        logging.info('Finished')
    except FileNotFoundError:
        logging.info('End - FileNotFoundError')
        print ("Unable to find data file.")