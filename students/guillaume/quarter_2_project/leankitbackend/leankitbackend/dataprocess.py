#!/usr/bin/env python3
from leankitbackend.leankitcards import (cards_per_lanes, workload_users,
                                         cards_per_users, projects,
                                         cards_per_projects, project_size)
from leankitbackend.leankitcards import project_in_work
from prettytable import PrettyTable
from leankitbackend.date_analysis import delta_date, cvt_d

'''
http://zetcode.com/python/prettytable/
'''


lanes_current_sprint = ['Current Sprint Backlog', 'Doing Now', 'Under Review',
                        'Finished As Planned']


def assigned(card, attr='assignedUsers'):
    name_str = ', '.join([assigned['fullName']
                          for assigned in getattr(card, attr)])
    return name_str


def created_by(card):
    return card.createdBy['fullName']


def blocked(card):
    if card.blockedStatus['isBlocked']:
        return 'Blocked'
    return ''


def created_on(card):
    return str(cvt_d(card.createdOn).date())


def current_sprint(cards_lanes, users):
    res_lst = [users]
    tot = 0
    for lane in lanes_current_sprint:
        lane_lst = cards_lanes[lane]
        user, workload = workload_users(lane_lst, users)
        res_lst.append([lane, workload])
        tot += workload
    res_lst.append(['total', tot])
    return res_lst


'''
To refactor
'''


def current_sprint_team(cards_lanes, team):
    '''
    keys are lanes
    return a dictionnary with value are dictionnaries of cards with keys
    being the users
    '''
    ret_dict = dict()
    for lane in lanes_current_sprint:
        lane_lst = cards_lanes[lane]
        tmp_dict = cards_per_users(lane_lst)
        dic_values = {key: value for key, value
                      in tmp_dict.items() if key in team}
        ret_dict[lane] = dic_values
    return ret_dict


def current_sprint_team_2(cards_lanes, team):
    '''
    keys are users
    return a dictionnary with value are dictionnary of cards with keys
    being the column
    '''
    ret_dict = dict()
    for user in team:
        lane_lst = cards_lanes[user]
        tmp_dict = cards_per_lanes(lane_lst)
        dic_values = {key: value for key, value
                      in tmp_dict.items() if key in lanes_current_sprint}
        ret_dict[user] = dic_values
    return ret_dict


def c_sprint_cut_off(cards_lanes, team, cut_off):
    '''
    Modify the outcome of current_sprint_team_2 with a cutoff date
    in the finished as planned column
    '''
    def delta(card):
        return delta_date(card.json['movedOn'], cut_off)

    def test_d(cards):
        return [card for card in cards if delta(card)]

    cards = current_sprint_team_2(cards_lanes, team)
    for value in cards.values():
        try:
            a = value['Finished As Planned']
            value['Finished As Planned'] = test_d(a)
            # value['Finished As Planned'] = []
        except KeyError:
            pass

    return cards


def new_requests(cards, cutoff_date):

    dic_cards = cards_per_lanes(cards)
    new_requests = dic_cards['New Requests']

    def cut(cards):
        return delta_date(cards.json['createdOn'], cutoff_date)

    return [card for card in new_requests if cut(card)]


'''
Table Creation
'''


def cvt_pretty(cards_lanes, team, cutoff):
    '''
    Convert the outcome of c_sprint_cut_off to a pretty table
    '''
    cards = c_sprint_cut_off(cards_lanes, team, cutoff)
    lanes_lst = ['Users', 'Nb Cards']
    lanes_lst.extend(lanes_current_sprint)
    lanes_lst.append('Total')
    data = []
    for user, tasks in cards.items():
        lst = [user]
        tmp_lst = [0] * len(lanes_current_sprint)
        nb_cards = 0
        for key, value in tasks.items():
            # value is dict wit key being lane and value
            # being a list of cards
            tmp = sum([it.json['size'] for it in value])
            ind = lanes_current_sprint.index(key)
            tmp_lst[ind] = tmp
            nb_cards += len(value)

        tmp_lst.append(sum(tmp_lst))
        lst.append(nb_cards)
        lst.extend(tmp_lst)
        data.append(lst)

    data.sort(key=lambda x: -x[-1])
    table = create_table(data, lanes_lst)
    return table


def print_team(cards_lanes, team):

    lanes_lst = ['Users']
    lanes_lst.extend(lanes_current_sprint)
    lanes_lst.append('total')

    data = []
    for user in team:
        sprint = current_sprint(cards_lanes, user)
        ret_lst = [it[1] for it in sprint if isinstance(it, list)]
        lst = [sprint[0]]
        lst.extend(ret_lst)
        data.append(lst)
    table = create_table(data, lanes_lst)
    return table


def lst_projects(Cards_obj):

    projects_lst = projects(Cards_obj)
    cards_proj = cards_per_projects(Cards_obj)

    data = []
    for project in projects_lst:
        i = project_size(cards_proj[project])
        j = project_in_work(cards_proj[project])
        lst = [project.title, project.plannedFinish,
               project.lane['title'], i, j, assigned(project)]
        data.append(lst)
    data.sort(key=lambda x: x[2])
    table = create_table(data, ['Project', 'End Date', 'Lane',
                                'Total Points', 'In Work', 'Assigned to'])
    return table


def projects_contributors(Cards_obj):

    projects = cards_per_projects(Cards_obj)

    def user(cards_lst):
        ret_lst = []
        if not isinstance(cards_lst, list):
            cards_lst = [cards_lst]
        for card in cards_lst:
            for assigne in card.assignedUsers:
                ret_lst.append(assigne['fullName'])
        return ret_lst

    ret_lst = []
    for project, cards_lst in projects.items():
        i = project_size(cards_lst)
        j = project_in_work(cards_lst)
        list_users = user(project)
        if cards_lst != []:
            list_users.extend(user(cards_lst))
        # using set for unicity purpose
        tmp = [project.title, project.lane['title'], project.plannedFinish,
               assigned(project), len(cards_lst), i, j]
        tmp.extend(set(list_users))
        ret_lst.append(tmp)

    nb_lane = max([len(item) for item in ret_lst])
    fields = ['Project', 'status', 'Finish Date', 'Assigned to', '# Cards',
              'Total Points', 'In Work']
    fields_tmp = ['contributor_{}'.format(k + 1)
                  for k in range(nb_lane - len(fields))]
    fields.extend(fields_tmp)

    ret_lst.sort(key=lambda x: x[1])

    def ext(line):
        line.extend([' '] * (nb_lane - len(line)))
        return line

    data = [ext(line) for line in ret_lst]
    table = create_table(data, fields)
    ret_lst.insert(0, fields)

    return ret_lst, table


def table_new_requests(cards, cutoff_date):
    cards = new_requests(cards, cutoff_date)

    def lst_card(card):
        return [card.type['title'], card.title, created_by(card),
                assigned(card), created_on(card)]

    print_lst = [lst_card(card) for card in cards]
    print_lst.sort(key=lambda x: x[-1])

    header = ['Request Type', 'Title', 'Created By', 'Assigned to',
              'Created on']

    return create_table(print_lst, header)


def create_table(iter, header=None):
    table = PrettyTable()
    table.field_names = header
    for lst in iter:
        table.add_row(lst)
    return table


def table_cards_per_users(users_cards, users_lst=None):

    def c_data(card):
        return [card.priority, card.type['title'], card.title,
                card.size, card.lane['title']]

    ret_lst = []
    for user, lst_cards in users_cards.items():
        tmp_lst = []
        for card in lst_cards:
            tmp_lst.append(c_data(card))
        ret_lst.append([user, tmp_lst])

    headers = ['priority', 'type', 'title', 'size', 'lane']

    tables = []
    for lst in ret_lst:
        table = create_table(lst[1], headers)
        stri = '{}\n'.format(str(table.get_string(title=lst[0])))
        print(stri)
        tables.append([lst[0], table])

    return tables


def table_cards_per_projects(projects_cards, projects_lst=None):

    def c_data(card):
        return [card.priority, card.type['title'], card.title,
                card.size, card.lane['title'], assigned(card)]

    headers = ['priority', 'type', 'title', 'size', 'lane', 'Assgined']

    ret_lst = []
    for project, cards in projects_cards.items():
        tmp_lst = []
        for card in cards:
            tmp_lst.append(c_data(card))
        ret_lst.append([project.title, tmp_lst])

    tables = []
    for lst in ret_lst:
        table = create_table(lst[1], headers)
        stri = '{}\n'.format(str(table.get_string(title=lst[0])))
        print(stri)
        tables.append([lst[0], table])

    return ret_lst, tables


