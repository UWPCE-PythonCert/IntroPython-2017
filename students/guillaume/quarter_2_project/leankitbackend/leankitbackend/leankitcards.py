from collections import defaultdict
import types
from datetime import datetime

'''
Maybe define a Project class
'''

lanes_current_sprint = ['Current Sprint Backlog', 'Doing Now', 'Under Review',
                        'Finished As Planned']

lanes_Backlogs_next_sprint = ['Backlog', 'Next Sprint Planning']


# Attention sub columns of recently finished / ready to archived has the
# same name
lanes_Finished = ['Finished As Planned', 'Started but not Finished',
                  'Discarded or Obsolete']


class Leankit_Cards:
    def __init__(self, cards_list=None, date=None):
        self.date = date
        if cards_list is not None:
            self.append(cards_list, date)

    def append(self, cards_list, date=None):
        if isinstance(cards_list, list):
            self.date = date
            self.cards_list = []
            self.cards_id = []
            self.cards_title = []
            self.json = []

            try:
                for card in cards_list:
                    self.cards_list.append(Leankit_Card(card))
                    self.cards_id.append(card['id'])
                    self.cards_title.append(card['title'])
                    self.json.append(self.cards_list[-1].json)

                self.projects = projects(self.cards_list)
                self.len = len(cards_list)
                self.status = True
                # self.json = [card.json for card in self.cards_list]
            except KeyError:
                self.status = False

    def projects(self):
        return projects(self)

    def sorted_projects(self):
        return sorted_projects(self)

    def in_progress(self):
        return self.sorted_projects()['In Progress']

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, datetime_obj):
        if isinstance(datetime_obj, datetime):
            self._date = datetime_obj
            # self.year = self.date.year
            # self.week_n = self.date.isocalendar[1]

    def __repr__(self):
        if hasattr(self, 'cards_list'):
            return ('').join([card.__repr__() for card in self.cards_list])
        return 'There is no cards being imported'


class Leankit_Card:
    def __init__(self, card):
        if isinstance(card, dict):
            self.json = card
            for key, value in card.items():
                setattr(self, key, value)
            self.status = True
        else:
            self.status = False

    def __repr__(self):
        try:
            Name = ''
            if len(self.assignedUsers) > 0:
                tmp_lst = [user['fullName'] for user in self.assignedUsers]
                Name = (', ').join(tmp_lst)
            tmp_lst = self.type['title'], self.id, self.title, Name
            return '{} {} {} {}\n'.format(*tmp_lst)
        except (AttributeError, KeyError):
            return 'input was not a card'


class Leankit_Board:
    def __init__(self, board):
        if isinstance(board, dict):
            self.json = board
            for key, value in (self.json).items():
                setattr(self, key, value)
            self.status = True
        else:
            self.status = False

    def __repr__(self):
        try:
            tmp_lst = [self.id, self.title]
            ret_str = ' '.join(tmp_lst) + '\n'
            ret_str += (('{}\n') * len(self.json)).format(*self.json.keys())
            return ret_str
        except AttributeError:
            return 'Bad Data'

    def users_list(self):
        try:
            return [user['fullName'] for user in self.users]
        except (KeyError, AttributeError):
            return []

    def lanes_list(self):
        def f(lane):
            a = [lane['id'], lane['name'], lane['parentLaneId']]
            return '{} {} {}'.format(*a)

        try:
            return [f(lane) for lane in self.lanes]
        except (KeyError, AttributeError):
            return []

    def lanes_structures(self):

        def f(key, lst):
            if key in lst:
                return lst.index(key)

        def la(lane):
            return [lane['name'], lane['id'], lane['index']]
        try:
            lst_1 = [la(lane) for lane in self.lanes
                     if lane['parentLaneId'] is None]
            d = defaultdict(list)
            for lane in self.lanes:
                if lane['parentLaneId'] is not None:
                    d[lane['parentLaneId']].append(la(lane))

            def g(key):
                a = f(key, [item[1] for item in lst_1])
                return lst_1[a][0]

            e = {g(key): value for key, value in dict(d).items()}

            for value in e.values():
                value.sort(key=lambda x: x[-1])

            return [lst_1, e]

        except (KeyError, AttributeError):
            return []


def cards_per_types(cards, attribute='type', key='title'):
    dic = defaultdict(list)
    if isinstance(cards, Leankit_Cards):
        cards_lst = cards.cards_list
    elif isinstance(cards, list):
        cards_lst = cards
    else:
        print(type(cards))
        cards_lst = cards

    try:
        for card in cards_lst:
            d = getattr(card, attribute)
            if isinstance(d, dict):
                nkey = d[key]
                dic[nkey].append(card)
            else:
                for it in d:
                    nkey = it[key]
                    dic[nkey].append(card)
        return dic
    except (KeyError, AttributeError):
        return dic


def projects(cards):
    if isinstance(cards, Leankit_Cards):
        cards = cards.cards_list
    return [card for card in cards if card.type['title'] == 'Project']


def sorted_projects(cards):
    projs = projects(cards)
    return cards_per_lanes(projs)


def cards_per_users(cards):
    return cards_per_types(cards, attribute='assignedUsers', key='fullName')


def cards_per_lanes(cards):
    return cards_per_types(cards, 'lane', 'title')


def return_card(id_v, lst_cards):
    for card in lst_cards:
        if card.id == id_v:
            return card
    return None


def cards_per_projects(cards):
    if isinstance(cards, Leankit_Cards):
        project_lst = projects(cards.cards_list)
    else:
        project_lst = projects(cards)
    pro_dic = {card.id: [] for card in project_lst}

    def r_card(cardid):
        return return_card(cardid, project_lst)

    for card in cards.cards_list:
        lst = card.parentCards
        for item in lst:
            if item['cardId'] in pro_dic:
                pro_dic[item['cardId']].append(card)
    pro_dic = dict((r_card(key), value) for key, value in pro_dic.items())
    return pro_dic


def project_size(lst_cards):
    return sum(lst_Cards(lst_cards, o_attr=None, crit=None))


def project_in_work(lst_cards):
    return sum(lst_Cards(lst_cards))


def project_next_sprint(lst_cards, crit=lanes_Backlogs_next_sprint):
    return sum(lst_Cards(lst_cards, crit))


def workload_users(lst_cards, user):
    workload = lst_Cards(lst_cards, o_attr='assignedUsers',
                         o_key='fullName', crit=user)
    return user, sum(workload)


def lst_Cards(lst_cards, r_attr='size', r_key=None,
              o_attr='lane', o_key='title',
              crit=lanes_current_sprint):
    '''
    Generate a list of attritube([key]) from a list of cards
    using an optional crit (for example Being within a column)
    '''
    def card_r(card, attr, key):
        if key is not None:
            if isinstance(getattr(card, attr), dict):
                return getattr(card, attr)[key]
            else:
                lst = [it[key] for it in getattr(card, attr)]
                if len(lst) == 1:
                    return lst[0]
                return lst
        if attr is None:
            return card
        return getattr(card, attr)

    def card_i(card):
        return card_r(card, r_attr, r_key)

    def card_o(card):
        return card_r(card, o_attr, o_key)

    def Crit(card, crit):
        if isinstance(crit, types.FunctionType):
            return crit(card, crit)
        else:
            card = card_o(card)
            if not isinstance(card, list):
                if isinstance(crit, list):
                    return card in crit
                else:
                    return card == crit
            else:
                return crit in card

    if crit is None:
        return [card_i(card) for card in lst_cards]
    return [card_i(card) for card in lst_cards if Crit(card, crit)]


def find_cards(Cards, **args):
    pass

