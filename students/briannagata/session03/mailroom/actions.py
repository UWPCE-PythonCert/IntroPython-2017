# Modules to process selections made in mailroom.py
# Python 3.6


def list_database(donors):
    """ Print the list of donor names"""    
    for name in donors.keys():
        print(name)


def send_thankyou(name, money, text):
    """ Emulate a thank you email by emulating content to terminal. """
    text = text.replace('[DONOR]', name)
    text = text.replace('[DONATION]', '{:.2f}'.format(money))
    print(text, end='\n')


def create_report(donors):
    """ Print the databse of donor information. """
    print('\n{:20}|{:13}|{:13}|{:13}'.format('Donor Name',
                                             'Total Given',
                                             'Num Gifts',
                                             'Average Gift'))
    print('-' * 63)

    for key, value in sorted(donors.items(), key=lambda x: x[1], reverse=True):
        print('{:20} ${:10.2f} {:13}   ${:11.2f}'.format(key,
                                                         sum(value),
                                                         len(value),
                                                         sum(value)/2))
