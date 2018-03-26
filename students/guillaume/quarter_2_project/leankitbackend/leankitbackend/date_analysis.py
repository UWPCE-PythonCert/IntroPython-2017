#!/usr/bin/env python3
from datetime import datetime
from calendar import day_name


def cvt_d(l_date, d_format='%Y-%m-%dT%H:%M:%SZ'):
    '''
    Little function made to convert back and forth a str or a date
    string format must be 2018-02-09T16:19:57Z
    '''
    if isinstance(l_date, str):
        return datetime.strptime(l_date, d_format)
    elif isinstance(l_date, datetime):
        return datetime.strftime(l_date, d_format)
    else:
        return None


def delta_date(date_c, cutoff):
    date_c = cvt_d(date_c)
    cutoff = datetime.strptime(cutoff, '%Y-%m-%d')
    delta = cutoff - date_c
    if delta.days >= 0:
        return False
    return True


def week_day(l_date):
    '''
    Little function made to return the day of the week
    '''
    if not isinstance(l_date, datetime):
        l_date = cvt_d(l_date)
    return day_name[l_date.weekday()]


def delta_now(l_date):
    return int((datetime.today() - l_date).days)
