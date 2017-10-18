#!/usr/bin/env python3

"""
Kathryn Egan
"""


DONORS = {
    'Benedict Cumberbatch': [200000.0],
    'Elon Musk': [10000.0, 150000.0, 100000.0],
    'Dad': [20.0, 5.0],
    'Donald Trump': [2.81],
    'Alley Joe': [.54, .01, .25]}


def main():
    options = [
        '1 Send a Thank You',
        '2 Create a Report',
        '3 Quit']
    while True:
        answer = input('\n'.join(options) + '\n>')
        if answer == '1':
            send_thank_you()
        elif answer == '2':
            create_report()
        elif answer == '3':
            print('Exiting...')
            break


def send_thank_you():
    line = '-' * 80
    while True:
        name = input(
            'Who donated? (Type LIST to see current list of donors)\n')
        name = name.title()
        if name.upper() == 'LIST':
            print('Current donors:\n' + '\n'.join(sorted(DONORS)))
            continue
        if name not in DONORS:
            DONORS[name] = []
        while True:
            donation = input('How much did {} donate?\n$'.format(name))
            try:
                donation = float(donation)
                DONORS[name].append(donation)
                break
            except ValueError:
                print('{} is not a valid amount.'.format(donation))
                print('Please try again.')
        print(line)
        thank_you = \
            'Dear {},\nThank you so much for your generous donation of ' +\
            '${:.2f}. This will go towards building our new disadvantaged ' +\
            'kitten facility. We at Miuvenile Care thank you for your help.'
        print(thank_you.format(name, donation))
        print(line)
        break


def by_donation(donor):
    return sum(DONORS[donor])


def average(donations):
    avg = sum(donations) / len(donations)
    return round(avg, 2)


def dollar(amount):
    dollars, cents = str(amount).split('.')
    if len(cents) == 1:
        cents += '0'
    return '.'.join([dollars, cents])


def pad(string, length, orientation):
    left = True
    while len(string) < length:
        if orientation == 'left':
            string = string + ' '
        elif orientation == 'right':
            string = ' ' + string
        elif left:
            string = string + ' '
            left = False
        else:
            string = ' ' + string
            left = True
    return string


def print_header(headers, lengths):
    line = []
    orientations = ['left', 'right', 'right', 'right']
    for header, orientation in zip(headers, orientations):
        header = pad(header, lengths[headers.index(header)], orientation)
        line.append(header)
    line = ' | '.join(line)
    return line


def print_data(row, lengths):
    line = []
    orientations = ['left', 'right', 'right', 'right']
    formats = ['name', 'monetary', 'numerical', 'monetary']
    for index in range(len(row)):
        item = pad(row[index], lengths[index], orientations[index])
        # monetary values get WS inserted between $ and number
        if formats[index] == 'monetary':
            item = '$' + item + ' '
        # numbers are right oriented with one extra WS in front and back
        elif formats[index] == 'numerical':
            item = ' ' + item + ' '
        # names are left oriented with one extra WS trailing
        else:
            item += ' '
        line.append(item)
    return ' '.join(line).strip()


def create_report():
    headers = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    data = []
    lengths = [len(item) for item in headers]
    for donor in sorted(DONORS, key=by_donation, reverse=True):
        donations = DONORS[donor]
        line = [
            donor, dollar(sum(donations)),
            str(len(donations)), dollar(average(donations))]
        for index in range(len(line)):
            if len(line[index]) > lengths[index]:
                lengths[index] = len(line[index])
        data.append(line)
    report = []
    report.append(print_header(headers, lengths))
    report.append('-' * (sum(lengths) + 1))
    for row in data:
        report.append(print_data(row, lengths))
    print('\n'.join(report))


if __name__ == '__main__':
    main()
