#!/usr/bin/env python3
from leankitbackend.setting import init
from leankitbackend.util import read_json, merg_d
from requests import post, get, delete
from requests.auth import HTTPBasicAuth
import json
import asyncio
from aiohttp import ClientSession

from os import chdir

'''
This module provide a wrapper around LeanKit API v2
https://isilon.leankit.com/io/docs
https://aiohttp.readthedocs.io/en/stable/
'''
web = ".leankit.com/io/"
web_auth = "{}auth/token".format(web)
web_card = "{}card".format(web)
web_board = "{}board".format(web)


class LeanKit_Auth:

    '''
    This Class is generating a token for connecting to Leankit API V2
    more documentation about this API at
    https://isilon.leankit.com/io
    '''

    def __init__(self):
        pass

    def get_token(self, **args):

        '''
            **args is a dict including the followwing sets of key: value
            company : name
            username : username
            password : password
            optional :
            description : description
        '''
        if set(('company', 'username', 'password')).issubset(args):

            url = "https://{}{}".format(args['company'], web_auth)
            auth = HTTPBasicAuth(args['username'], args['password'])
            params = {'description': 'PythonToken'}
            if 'description' in args:
                params = {'description': args['description']}
            response = post(url, auth=auth, params=params)
            self.url = response.url
            self.status = 'Failure'

            if response.status_code == 200:
                self.status = 'Success'
                try:
                    for key, value in response.json().items():
                        # each set of key: value is put into an attribute:value
                        setattr(self, key, value)
                except json.decoder.JSONDecodeError:
                    pass

    def list_tokens(self, **args):
        self.status = 'Failure'
        if set(('company', 'username', 'password')).issubset(args):

            url = "https://{}{}".format(args['company'], web_auth)
            auth = HTTPBasicAuth(args['username'], args['password'])
            response = get(url, auth=auth)
            if response.status_code == 200:
                self.status = 'Success'
                try:
                    self.active_tokens = list(response.json().values())[0]
                except json.decoder.JSONDecodeError:
                    pass

    def revoke_tokens(self, token_id=None, **args):
        '''
        This function will revoke specific token if given or
        revoke all the tokens if here are no others arguments than **args
        '''
        self.status = "Bad Input"
        if set(('company', 'username', 'password')).issubset(args):
            auth = HTTPBasicAuth(args['username'], args['password'])

        if token_id is not None:
            token_lst = [token_id]
        else:
            self.list_tokens(**args)
            token_lst = [token['id'] for token in self.active_tokens]

        for token in token_lst:
            url = "https://{}{}/{}".format(args['company'], web_auth, token)
            response = delete(url, auth=auth)
            self.url = response.url
            self.list_tokens(**args)
            self.status = response.status_code


# The following functions will abstract the API calls:

# 1. API calls for the cards

def Cards_list(token, **args):
    '''
    Abstract API call card:list

    Due to the API Limitation, it can only publish 500 records at once
    A request has been made to Leankit to solve it
    A solution is to play with offset to generate a list of all the cards
    on the board

    "pageMeta": {
        "totalRecords": 582,
        "offset": 500,
        "limit": 500,
        "startRow": 501,
        "endRow": 582
    }

    '''
    if set(('company', 'board')).issubset(args):
        url = "https://{}{}".format(args['company'], web_card)
        Bearer = "Bearer {}".format(token)
        headers = {'Authorization': Bearer}
        params = {'board': args['board'], 'limit': args['limit']}
        response = get(url, headers=headers, params=params)

        # First API Call
        if response.status_code == 200:
            try:
                ret_lst = response.json()['cards']
                total = response.json()['pageMeta']['totalRecords']
                end_row = response.json()['pageMeta']['endRow']
            except (json.decoder.JSONDecodeError, KeyError):
                return {}

            # Making sure all the cards are collected
            while total != end_row:
                params['offset'] = end_row
                response = get(url, headers=headers, params=params)
                try:
                    ret_lst.extend(response.json()['cards'])
                    total = response.json()['pageMeta']['totalRecords']
                    end_row = response.json()['pageMeta']['endRow']
                except (json.decoder.JSONDecodeError, KeyError):
                    return {}

        return ret_lst


def Card_info(token, **args):
    '''
    Abstract Card:self
    '''
    if set(('company', 'card')).issubset(args):
        url = "https://{}{}/{}".format(args['company'], web_card,
                                       args['card'])
        Bearer = "Bearer {}".format(token)
        headers = {'Authorization': Bearer}
        response = get(url, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return {}


def Cards_info(token, **args):
    '''
    Make the Card_info call for a Cards_list
    and add to it by merging 2 dictionnaries
    return a list of dictionnaries
    '''
    def extra_info(card):
        '''currying a function '''
        return Card_info(token, card=str(card), **args)

    card_dict = Cards_list(token, **args)
    card_lst = [card['id'] for card in card_dict]
    return [merg_d(info, extra_info(card)) for card, info
            in zip(card_lst, card_dict)]


def Cards_info_aio(token, **args):
    card_dict = Cards_list(token, **args)
    if card_dict != {}:
        loop = asyncio.get_event_loop()  # event loop
        future = asyncio.ensure_future(get_calls(token,
                                                 cards=card_dict, **args))
        loop.run_until_complete(future)
        tmp = [a.result() for a in future.result()]
        return [merg_d(info, card) for card, info
                in zip(tmp, card_dict)]
    print('there is a pb')
    return []


async def get_calls(token, **args):
    tasks = []
    card_dict = args['cards']
    card_lst = [card['id'] for card in card_dict]
    async with ClientSession() as session:
        def get_call_c(card):
            return get_call(session, token, card=card, **args)
        for card, info in zip(card_lst, card_dict):
            task = asyncio.ensure_future(get_call_c(card))
            tasks.append(task)
        _ = await asyncio.gather(*tasks)
    return tasks


async def get_call(session, token, **args):

    if set(('company', 'card')).issubset(args):
        url = "https://{}{}/{}".format(args['company'], web_card,
                                       args['card'])
        Bearer = "Bearer {}".format(token)
        headers = {'Authorization': Bearer}
        async with session.get(url, headers=headers) as response:
            try:
                resp = await response.json()
                return resp
            except json.decoder.JSONDecodeError:
                return None


def Board_id(token, **args):
    '''
    Abstract API call board:self
    '''
    if set(('company', 'board')).issubset(args):
        url = "https://{}{}/{}".format(args['company'],
                                       web_board, args['board'])
        Bearer = "Bearer {}".format(token)
        headers = {'Authorization': Bearer}
        response = get(url, headers=headers)
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            return None


def Board_Create(token, **args):
    pass


if __name__ == "__main__":
    
    Leankit_input = init()

    if Leankit_input != {}:
        ipath = Leankit_input['input']
        chdir(ipath)
        Auth_Obj = LeanKit_Auth()
        Auth_Obj.get_token(**Leankit_input)

    