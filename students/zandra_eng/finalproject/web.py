#!/usr/bin/env python 3

"""
Reference:
csv file
https://docs.python.org/2/library/csv.html

matplotlib
https://matplotlib.org/gallery/pyplots/pyplot_formatstr.html#sphx-glr-gallery-pyplots-pyplot-formatstr-py


"""


#import datetime
import sys
from dateutil.parser import parse
import matplotlib.pyplot as plt
import csv

# if pulling data from the internet for python 2 use: import pandas.io.data as web

from pandas_datareader import data as web


class StockPlotter:

    def fetch_stock(self, stock_name, start, end):
        df = web.DataReader(stock_name, "google", start, end)
        return df

    def save(self, stocks, filename):
        stocks.to_csv(filename)

    def plot(self, stock_name, csvfile):
        dates = []
        values = []
        with open(csvfile) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if reader.line_num == 1:
                    continue
                dates.append(row[0])
                values.append(row[4])
        fig, ax = plt.subplots() # ax = axel, fig = figure
        ax.plot_date(dates, values, '-')
        fig.autofmt_xdate() #formating figure
        plt.xlabel("Date")
        plt.ylabel(stock_name + " close value")
        plt.show()
        #plt.savefig("./stocks.png")


if __name__ == "__main__":
    if len(sys.argv) < 4 :
        print("Error: Give a stock name, start and end dates as arguments")
        exit(1)
    stock_name = sys.argv[1]
    start = parse(sys.argv[2])
    end = parse(sys.argv[3])
    plotter = StockPlotter()
    stocks = plotter.fetch_stock(stock_name, start, end)
    csvfile = "{}.csv".format(stock_name)
    plotter.save(stocks, csvfile)  #./ = current folder
    plotter.plot(stock_name, csvfile)

