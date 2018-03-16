#!/usr/bin/env python3
from leankitbackend.time_import import files_to_import
from leankitbackend.date_analysis import cvt_d, delta_now
from leankitbackend.util import lst_to_xl, format_xl, lst_to_xl_format
from leankitbackend.setting import init
from leankitbackend.dataprocess import assigned, blocked
from os import chdir, path
from collections import defaultdict
from prettytable import PrettyTable, MSWORD_FRIENDLY


def weekly_subset(Cards_dict):
    ddict = defaultdict(list)
    for key, value in Cards_dict.items():
        alpha = key.isocalendar()
        key = '{}-{}'.format(alpha[0], alpha[1])
        ddict[key].append(value)

    for key, value in ddict.items():
        tmp = max(value, key=lambda x: x.date)
        ddict[key] = tmp

    return dict(ddict)


def projects(lst, Cards_dict, week_nb=None, Attr='projects'):

    return {key: getattr(value, Attr) for key, value in Cards_dict.items()}


def Active_projects(lst, Cards_dict, week_nb=None):
    '''
    Cards Dict is a dictionnary of leankit_cards
    '''
    return projects(lst, Cards_dict, week_nb, Attr='in_progress')


def table_projects(projs):

    def f(value):
        tmp = list()
        for item in value:

            a = [item.title,
                 cvt_d(item.createdOn),
                 item.lane['title'],
                 assigned(item),
                 blocked(item),
                 # cvt_d(item.movedOn),
                 item.plannedFinish]
            tmp.append(a)
        return tmp

    def g(value):
        tmp = []
        for item in value:
            tmp.append(item[1:])
            tmp.sort(key=lambda x: h(x))
        return tmp

    def h(lst):
        '''
        Sorted per year, then per week number using a set
        '''
        tmp = lst[0].split('-')
        tmp = map(int, tmp)
        tmp_l = tuple(tmp)
        return tmp_l

    def init_last_date(item):
        '''
        return first & last date
        '''
        first = None
        last = item[-1][-1]
        if last is not None:
            last = cvt_d(last, d_format='%Y-%m-%d').strftime('%m/%d/%Y')
        for i in item[2:-1]:
            first = i[-1]
            if first is not None:
                first = cvt_d(first, d_format='%Y-%m-%d').strftime('%m/%d/%Y')
                break
        return [first, last]

    dic = {key: f(value) for key, value in projs.items()}
    ddict = defaultdict(list)

    for key, value in dic.items():
        for item in value:
            ddict[item[0]].append([item[1], key, *item[2:]])

    # print(ddict)
    lst = [[key, value[0][0], *g(value)] for key, value in ddict.items()]
    lst.sort(key=lambda x: x[1])
    lst.reverse()
   
    ret_lst = [[item[0],
                item[1].strftime('%m/%d/%Y'),
                delta_now(item[1]),
                item[-1][1],
                item[-1][2],
                *init_last_date(item),
                item[-1][-2]]
               for item in lst]
    
    header = ['Project', 'createdOn', 'Nb Days', 'Column', 'Assigned to',
              'Initial ECD', 'Current ECD', 'Blocked']
    ret_lst.insert(0, header)

    table = PrettyTable()
    table.field_names = header
    for row in ret_lst[1:]:
        table.add_row(row)

    table.set_style(MSWORD_FRIENDLY)
    print(table.get_string(title='Current Status'))
    # chdir(opath)
    lst_to_xl_format(ret_lst, path.join(opath, 'time_analysis.xlsx'), True)
    '''
    [wb, ws] = lst_to_xl(ret_lst, path.join(opath, 'time_analysis.xlsx'), True)
    format_xl(wb, ws)
    '''
    return lst, ret_lst, table


def time_report():

    Leankit_input = init()
    if Leankit_input != {}:
        global opath
        opath = Leankit_input['output']
        cron_path = Leankit_input['cron_data']

        d_format = '%Y-%m-%d %H:%M:%S.%f'
        name = 'Cards_all.json'
        a = [cron_path, 'imported_files', name, d_format]
        lst, Cards_dict = files_to_import(*a)
        b = weekly_subset(Cards_dict)
        projs = projects(lst, b)
        d, c, table = table_projects(projs)

        return [d, c, table]


if __name__ == "__main__":
    [d, c, table] = time_report()




