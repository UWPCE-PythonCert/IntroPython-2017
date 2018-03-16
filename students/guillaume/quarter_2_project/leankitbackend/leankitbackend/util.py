import json
import re
import csv
import xlsxwriter
from os import remove
from datetime import datetime

'''
This module provides helper functions
Some of these functions are being used for
test purpose
'''


def printd(dic):
    '''
    Print a dictionnary in a more readable way
    '''
    for key, val in dic.items():
        print('{} {}'.format(key, val))


def printl(lst):
    '''
    Print a list in a more readable way
    '''
    for item in lst:
        print(item)


def printld(lst):
    '''
    print a list of dictionnaries in a more readable way
    '''
    for dic in lst:
        printd(dic)
        print('\n')


def writel(lst_cards, out_f):
    '''
    Write a list into a file
    '''
    with open(out_f, 'w') as out:
        for card in lst_cards:
            out.write(str(card))


def writed(dic, out_f):
    '''
    Write a dictionnaty into a file
    '''
    with open(out_f, 'w') as out:
        for key, value in dic.items():
            out.write('{}: {}\n'.format(key, value))


def writeld(lst_dic, out_f):
    '''
    Write a list of dictionnaries into a file
    '''
    with open(out_f, 'w') as out:
        for dic in lst_dic:
            out.write('\n')
            for key, value in dic.items():
                out.write('{}: {}\n'.format(key, value))
        out.write('\n')


def import_data(file):
    '''
    Load a json file
    '''
    with open(file, 'r') as inp:
        return json.load(inp)


def save_data(data, file):
    '''
    Save data into a json file
    '''
    with open(file, 'w') as out:
        json.dump(data, out)


def read_json(filename):
    '''
    read a json file into a dic
    '''
    with open(filename, 'r') as inp:
        dic = json.load(inp)
        return dic


def merg_d(a, b):
        '''
        mergin two dictionnary
        '''
        tmp = a.copy()
        tmp.update(b)
        return tmp

'''
The 2 next functions are design to put a table generated 
by pretty table into a csv file
'''

def pretty_table_to_tuples(input_str):
    lines = input_str.split("\n")
    num_columns = len(re.findall("\+", lines[0])) - 1
    line_regex = r"\|" + (r" +(.*?) +\|" * num_columns)
    for line in lines:
        m = re.match(line_regex, line.strip())
        if m:
            yield m.groups()


def table_to_csv(table, file):
    with open(file, 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(pretty_table_to_tuples(table.get_string()))


def lsts_to_csv(lsts, file):
    '''
    write a list of lists into a csv file
    '''
    with open(file, 'w', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(lsts)


def table_to_xl(table, file):
    '''
    http://coderscrowd.com/app/public/codes/view/201
    '''
    csv_f = file.replace(".xlsx", ".csv")
    table_to_csv(table, csv_f)

    wb = xlsxwriter.Workbook(file)
    ws = wb.add_worksheet("WS1")    # your worksheet title here
    with open(csv_f, 'r') as csvfile:
        table_xl = csv.reader(csvfile)
        i = 0
        for row in table_xl:
            ws.write_row(i, 0, row)
            i += 1
    wb.close()


def tables_to_xl(tables, file):

    wb = xlsxwriter.Workbook(file)
    for item in tables:
        tab = item[0]
        table = item[1]
        csv_f = file.replace(".xlsx", ".csv")

        table_to_csv(table, csv_f)

        ws = wb.add_worksheet(tab)    # your worksheet title here
        with open(csv_f, 'r') as csvfile:
            table_xl = csv.reader(csvfile)
            i = 0
            for row in table_xl:
                ws.write_row(i, 0, row)
                i += 1
    wb.close()


def lst_to_xl(lst, file, ret_wb=False):

    wb = xlsxwriter.Workbook(file)
    ws = wb.add_worksheet('Projects')
    csv_f = file.replace(".xlsx", ".csv")
    lsts_to_csv(lst, csv_f)
    with open(csv_f, 'r') as csvfile:
        table_xl = csv.reader(csvfile)
        i = 0
        for row in table_xl:
            ws.write_row(i, 0, row)
            i += 1
    remove(csv_f)
    if ret_wb:
        return [wb, ws]
    else:
        wb.close()


def lst_to_xl_format(lst, file, ret_wb=False):

    wb = xlsxwriter.Workbook(file)
    ws = wb.add_worksheet('Projects')
    # Red
    format1 = wb.add_format({'bg_color': '#FFC7CE',
                             'font_color': '#9C0006'})

    # Green
    format2 = wb.add_format({'bg_color': '#C6EFCE',
                             'font_color': '#006100'})

    # Orange
    format3 = wb.add_format({'bg_color': '#FF6600',
                             'font_color': '#006100'})

    # White
    format4 = wb.add_format({'bg_color': '#FFFFFF',
                             'font_color': '#000000'})

    def format_row(row):
        col = ['In Design', 'Scoping']
        if all([row[3] in col, int(row[2]) > 15]):
            return format3
        elif row[-1] == 'Blocked':
            return format1
        elif row[-2] > row[-3]:
            return format1
        elif row[3] == 'In Progress':
            return format2
        return format4

    csv_f = file.replace(".xlsx", ".csv")
    lsts_to_csv(lst, csv_f)
    with open(csv_f, 'r') as csvfile:
        table_xl = csv.reader(csvfile)
        for i, row in enumerate(table_xl):
            ws.write_row(i, 0, row)
            if i > 0:
                ws.write_row(i, 0, row, format_row(row))
    remove(csv_f)
    ws.autofilter(0, 0, i, len(row) - 1)
    wb.close()


def format_xl(wb, ws):
    # Add a format. Light red fill with dark red text.
    # http://xlsxwriter.readthedocs.io/working_with_conditional_formats.html
    # Red
    ran = 'A2:H150'
    fran = 'A1:H150'
    format1 = wb.add_format({'bg_color': '#FFC7CE',
                             'font_color': '#9C0006'})

    # Green
    format2 = wb.add_format().set_border(1)

    ws.conditional_format(ran, {'type': 'text',
                                'criteria': 'containing',
                                'value': 'Blocked',
                                'format': format1})

    ws.conditional_format(ran, {'type': 'no_blanks', 'format': format2})
    ws.autofilter(fran)
    wb.close()



def lsts_to_xl(lsts, file):

    chars = '[:*?/\]'
    space = ' ' * len(chars)
    trans = str.maketrans(chars, space)

    wb = xlsxwriter.Workbook(file)
    ws_t = wb.add_worksheet('Projects_list')
    j = 0

    for item in lsts:

        tab, data = item
        csv_f = file.replace(".xlsx", ".csv")

        ws_t.write(j, 0, tab)
        j += 1

        lsts_to_csv(data, csv_f)
        title = tab[:31].translate(trans)

        ws = wb.add_worksheet(title)    # your worksheet title here
        ws.write(0, 0, tab)

        with open(csv_f, 'r') as csvfile:
            table_xl = csv.reader(csvfile)
            i = 1
            for row in table_xl:
                ws.write_row(i, 0, row)
                i += 1
    wb.close()


