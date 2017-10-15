#!/usr/bin/env python3
def read_data(textfile):
    '''
    Read data from a textfile about the donor and the
    amount of donations
    Pattern is as follow:
    '''
    file = open(textfile, 'r')
    donors = list()
    for i in list(file.readlines()):
        donors.append((i.rstrip()).split(','))
        for i, s in enumerate(donors[-1]):
            donors[-1][i] = s.lstrip()
            if donors[-1][i].isdecimal():
                donors[-1][i] = int(s)
    file.close()
    return donors


def write_data(textfile, donors):
    file = open(textfile, 'w')
    for donor in donors:
        donor_str = ', '.join(map(str, donor)) + '\n'
        file.write(donor_str)
    file.close()


def add_donation(ind, donors):
    '''
    '''
    boolean = True
    while boolean:
        donation = input('\nPlease add a donation amount?\n')
        if donation.isdecimal():
            # need to work on test for float donation
            boolean = False
            donation = int(donation)
            donors[ind].append(donation)
    return donors, donation


def email_thank_you(donor, donation, charity='local charity'):
    '''
    '''
    email = '''
            Dear {},

            I would like to thank you personnaly for the generous
            donation of ${} that you have made recently.
            Your committment to our cause is very valuable to us.

            Best regards,

                                    John Adams
                                    CEE of charity {}
            '''.format(donor, donation, charity)
    return email


def send_thank_you(textfile):
    '''
    '''
    donors = read_data(textfile)
    names = ['{} {}'.format(i[0], i[1]) for i in donors]
    boolean = True
    # Menu for Name cases
    while boolean:
        name = input('Plese enter a full name?\n')
        if name == 'list':
            print('\n')
            for i in names:
                print(i)
        elif name in names:
            boolean = False
            donors, donation = add_donation(names.index(name), donors)
        elif ' ' in name:
            # Checking for Last & First Name - very primitive
            boolean = False
            names.append(name)
            donors.append(name.split(' '))
            donors, donation = add_donation(-1, donors)
        else:
            print('Make sure you enter Last & first name\n')

    write_data(textfile, donors)
    email = email_thank_you(name, donation)
    return email


def report(textfile):
    donors = read_data(textfile)
    str_donors = [['{} {}'.format(i[0], i[1])] for i in donors]
    for ind, donor in enumerate(donors):
        add_list = [sum(donor[2:]), len(donor[2:])]
        add_list.append(round(add_list[0] / add_list[1], 2))
        str_donors[ind].extend(add_list)
    str_donors.sort(key=lambda x: x[1])
    str_donors.reverse()
    table = '''
Donor Name                | Total Given | Num Gifts | Average Gift
{}\n'''.format('-' * 66)
    for donor in str_donors:
        # string_add
        table += '{} $  {}  {} $  {}\n'.format(
            donor[0].ljust(27), str(donor[1]).ljust(13),
            str(donor[2]).ljust(8), str(donor[3]).ljust(10))
    return table


def input_sc(textfile):
    '''
    '''
    welcome = """
            local charity donor database\n

                Please make a choice:

                  1 - Send a thank you
                  2 - Create a report
                  3 - Quit\n
                """
    bool = True
    while bool:
        print(welcome)
        selection = input('Please type a number between 1 & 3:\n')
        if selection.isdecimal():
            selection = int(selection)
            if selection > 0 and selection < 4:
                if selection == 1:
                    print(send_thank_you(textfile))
                elif selection == 2:
                    print(report(textfile))
                elif selection == 3:
                    bool = False
                    print('Leaving program')


if __name__ == '__main__':
    '''
    '''
    textfile = 'donors.txt'
    input_sc(textfile)
