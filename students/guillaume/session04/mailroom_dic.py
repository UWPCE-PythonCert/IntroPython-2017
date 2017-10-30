#!/usr/bin/env python3
from os import system


def read_data_dic(textfile):
    '''
    Read data from a textfile about the donor and the
    amount of donations
    Pattern is as follow:
    '''
    file = open(textfile, 'r')
    donors = list()
    for i in list(file.readlines()):
        tmp_lst = i.rstrip().split(',')
        tmp_lst[2] = tmp_lst[2].lstrip(' [')
        tmp_lst[-1] = tmp_lst[-1].rstrip(']')
        tmp_dic = {'first_name': tmp_lst[0].lstrip(),
                   'last_name': tmp_lst[1].lstrip(),
                   'donations': [int(s.lstrip()) for s in tmp_lst[2:]]}
        donors.append(tmp_dic)
    file.close()
    return donors


def write_data_dic(textfile, donors):
    '''
    '''
    file = open(textfile, 'w')
    for donor in donors:
        tmp_str = '{first_name}, {last_name}, {donations}'.format(**donor)
        file.write('{}\n'.format(tmp_str))
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
            print(donors[ind])
            print(type(donors[ind]))
            if 'donation' not in donors[ind].keys():
                donors[ind]['donations'] = [donation]
            else:
                donors[ind]['donations'].append(donation)
    return donors, donation


def email_thank_you(donor, donation, charity='local charity'):
    '''
    '''
    email = '''
            Dear {},

            I would like to thank you persnnally for the generous
            donation of ${} that you have made recently.
            Your commmitment to our cause is very valuable to us.

            Best regards,

                                    John Adams
                                    CEE of charity {}
            '''.format(donor, donation, charity)
    return email


def send_thank_you(textfile):
    '''
    '''
    donors = read_data_dic(textfile)
    print(donors)
    names = ['{first_name} {last_name}'.format(**donor) for donor in donors]
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
            donor = name.split(' ')
            print(donor)
            donors.append({'first_name': donor[0], 'last_name': donor[1]})
            donors, donation = add_donation(-1, donors)
        else:
            print('Make sure you enter Last & first name\n')

    write_data_dic(textfile, donors)
    email = email_thank_you(name, donation)
    print(email)
    return True


def mass_mailing(textfile):
    donors = read_data_dic(textfile)
    for donor in donors:
        file = open('{first_name}_{last_name}_thank_you.txt'.format(**donor), 'w')
        letter = '''
            Dear {first_name} {last_name},

            I would like to thank you personally for your generous
            donations that you have made recently.
            Your commitment to our cause is very valuable to us.

            Best regards,

                                    John Adams
            '''.format(**donor)
        file.write(letter)
        file.close
    return True


def quit(textfile):
    print('Leaving Program')
    return False


def report(textfile):
    print('report')
    donors = read_data_dic(textfile)
    str_donors = [['{first_name} {last_name}'.format(**donor)]
                  for donor in donors]
    for ind, donor in enumerate(donors):
        add_list = [sum(donor['donations']), len(donor['donations'])]
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
    print(table)
    return True


def input_sc(textfile):
    '''
    '''
    selection_dic = {'Thank_you': '1 - Send a thank you',
                     'Report': '2 - Create a report',
                     'Mass_Mailing': '3 - Send letter to everyone',
                     'Quit': '4 - Quit'}

    welcome = """\nlocal charity donor database\n
    Please make a choice:\n
    {Thank_you} \n
    {Report} \n
    {Mass_Mailing} \n
    {Quit} \n
    """.format(**selection_dic)

    prog_dic = {1: send_thank_you, 2: report, 3: mass_mailing,
                4: quit}

    bool = True
    while bool:
        print(welcome)
        selection = input('Please type a number between 1 & 4:\n')
        if selection.isdecimal():
            selection = int(selection)
            bool = prog_dic.get(selection, 'None')(textfile)


if __name__ == '__main__':
    '''
    '''
    textfile = 'donors.txt'
    input_sc(textfile)
