#!/usr/bin/env python3
import leankitbackend.leankitapi as API
from leankitbackend.util import import_data, save_data
import leankitbackend.setting as setting
from os import path
from datetime import datetime


def get_data():

    # path
    Leankit_input = setting.init()
    ipath = Leankit_input['input']
    cron_path = Leankit_input['cron_data']

    # token
    # chdir(ipath)
    input_f  = path.join(ipath, 'input.json') 
    credentials = import_data(input_f)
    auth = API.LeanKit_Auth()
    auth.get_token(**credentials)
    token = auth.token
    
    # data from API
    # chdir(cron_path)
    cards_data = API.Cards_info_aio(token, **credentials)
    board_data = API.Board_id(token, **credentials)

    filename = 'card_data_{}.json'.format(str(datetime.today()))
    filename = path.join(cron_path, filename)
    save_data(cards_data, filename)

    filename = 'board_data_{}.json'.format(str(datetime.today()))
    filename = path.join(cron_path, filename)
    save_data(board_data, filename)


if __name__ == "__main__":

    get_data()
