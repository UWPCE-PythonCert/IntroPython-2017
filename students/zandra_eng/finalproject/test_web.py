#!/usr/bin/env python 3

import pytest
from web import StockPlotter
import csv
expected = [[88.14,  90.50,  88.07,  89.98,  13383214],
            [90.35,  90.50,  88.63,  89.06,  11054682],
            [87.98,  88.53,  87.34,  87.74,  11453034]]

def test_fetch_stock():

    s = StockPlotter()
    stocks = s.fetch_stock('WMT', '3/5/2018', '3/7/2018')
    assert len(stocks) == 3
    for rindex, row in enumerate(expected):
        for cindex, col in enumerate(row):
            assert col == stocks.ix[rindex, cindex]

def test_save_stock():

    s = StockPlotter()
    stocks = s.fetch_stock('WMT', '3/5/2018', '3/7/2018')
    s.save(stocks, 'test.csv')
    with open('test.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if reader.line_num == 1:
                continue
            for cindex, col in enumerate(row):
                if cindex == 0:
                    continue
                assert stocks.ix[reader.line_num-2, cindex-1] == float(col)

