#!/usr/bin/env python3
from leankitbackend.leankitapi import LeanKit_Auth, Board_id, Cards_info_aio
from leankitbackend.leankitcards import (Leankit_Cards, Leankit_Board,
                                         cards_per_users, cards_per_projects)

from leankitbackend.dataprocess import (cvt_pretty, lst_projects,
                                        projects_contributors,
                                        table_new_requests,
                                        table_cards_per_users,
                                        table_cards_per_projects)

from leankitbackend.util import (import_data, table_to_xl,
                                 tables_to_xl, lsts_to_xl, lst_to_xl)
import leankitbackend.setting as setting
from ast import literal_eval
import json

from os import remove, listdir, path

today = '2018-02-26'  # Cards per users
cut_off = '2018-02-05'  # Card per users

'''
teams_dic = {'eat_team': 'eat_team.txt', 'g_team': 'g_team.txt',
             'd_team': 'd_team.txt', 'a_team': 'a_team.txt'}

cpath = path.realpath(__file__)
fname = path.basename(__file__)
cpath = cpath[:len(cpath) - len(fname)]
ipath = '{}/input'.format(cpath)
opath = '{}/output'.format(cpath)


chdir(ipath)
teams = []
for team, file in teams_dic.items():
    with open(file, 'r') as in_f:
        team_l = literal_eval(in_f.read())
        teams_dic[team] = team_l
'''


def Leankit_script(dic):

    # Getting the token to access leankit
    Auth = LeanKit_Auth()
    Auth.get_token(**dic)
    if Auth.status == 'Success':
        # Cards Data
        Cards_list = Cards_info_aio(Auth.token, **dic)
        with open('Cards_Data.json', 'w') as out:
            json.dump(Cards_list, out)
        Cards_list = import_data('Cards_Data.json')
        Cards = Leankit_Cards(Cards_list)

        # Boards Info
        Board_info = Board_id(Auth.token, **dic)
        with open('Board_Data.json', 'w') as out:
            json.dump(Board_info, out)
        Board_info = import_data('Board_Data.json')
        Board = Leankit_Board(Board_info)

        Auth.revoke_tokens(**dic)

        return Board, Cards


def report():

    input_f  = path.join(ipath, 'input.json') 
    # Generate data structure from the API Call
    dic = import_data(input_f)
    Board, Cards = Leankit_script(dic)
    print('API Call Done')

    # Make sure the API Call was successful
    if hasattr(Cards, 'cards_list'):

        # Generate Data Structure
        Users_Cards = cards_per_users(Cards)
        Projects_Cards = cards_per_projects(Cards)

        # Generate a project table
        projects_table = lst_projects(Cards)
        print(projects_table)
        table_to_xl(projects_table, path.join(opath, 'Projects_status.xlsx'))
        print('\n')

        # Generate  Report per team for individual output
        for team, team_lst in teams_dic.items():
            users_table = cvt_pretty(Users_Cards, team_lst, today)
            print(users_table.get_string(title="Cards & Points"))
            xlsx_name = '{}.xlsx'.format(team)
            xlsx_name = path.join(opath, xlsx_name)
            table_to_xl(users_table, xlsx_name)
            print('\n')

        # Generate a table
        Proj_lst, Proj = projects_contributors(Cards)
        print(Proj.get_string(title='Projects list'))
        lst_to_xl(Proj_lst, path.join(opath, 'Projects_stakeholders.xlsx'))

        print('\n')
        new_req = table_new_requests(Cards, cut_off)
        print(new_req.get_string(title='New Requests'))
        table_to_xl(new_req, path.join(opath, 'new_request.xlsx'))

        # generate a list of all the card assigned per users
        cards_users = table_cards_per_users(Users_Cards)
        tables_to_xl(cards_users, path.join(opath, 'users_activity.xlsx'))

        # generate a list of cards per projects
        lsts, Projects_tables = table_cards_per_projects(Projects_Cards)
        lsts_to_xl(lsts, path.join(opath, 'projects_cards.xlsx'))

        # delete the temp file
        opath_lst = listdir(opath)
        for item in opath_lst:
            if item.endswith(".csv"):
                item = path.join(opath, item)
                remove(item)

    return Board, Cards


def team(teams_dic):

    # chdir(ipath)
    for team, file in teams_dic.items():
        file = path.join(ipath, file)
        with open(file, 'r') as in_f:
            team_l = literal_eval(in_f.read())
            teams_dic[team] = team_l
    return teams_dic


def Report_Stat():
    global Leankit_input
    global teams_dic
    global ipath
    global opath

    Leankit_input = setting.init()
    teams_d = Leankit_input['teams_dic']
    ipath = Leankit_input['input']
    opath = Leankit_input['output']

    teams_dic = team(teams_d)

    Board, Cards = report()
    Data = Board.lanes

    print('\n')
    total_cards = 0
    for item in Data:
        lst = [item['name'], item['index'], item['cardCount'],
               item['parentLaneId']]
        a = '{} {} {} {}'.format(*lst)

        if lst[-1] is None:
            print(a)
            total_cards += int(lst[2])
    print('\ntotal = {}\n'.format(total_cards))

    return Board, Cards, Data


if __name__ == "__main__":

    Board, Cards, Data = Report_Stat()
