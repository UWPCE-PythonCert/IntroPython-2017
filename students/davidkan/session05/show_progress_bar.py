#!/usr/bin/env python
# Description: Demo on progressbar2 3.34.3 ref: https://pypi.python.org/pypi/progressbar2
# Last modified on 10/29/2017 by David Kan


from progressbar import ProgressBar, UnknownLength
import csv
import time


def wrapping_an_iterable(bar):
    """
    Function shows an example of wrapping an iterable
    Progress example: 100% (1000 of 1000) |#####################| Elapsed Time: 0:00:10 Time: 0:00:10
    :param bar: instance of ProgressBar
    :return: none
    """
    for i in bar(range(1000)):
        time.sleep(0.01)

def context_wrapper():
    """
    Function shows an example of a context wrapper
    Progress example: 100% (1000 of 1000) |#####################| Elapsed Time: 0:00:10 Time: 0:00:10
    :return: none
    """
    with ProgressBar(max_value=1000) as bar:
        for i in range(1000):
            time.sleep(0.01)
            bar.update(i)

def progressbars_unknown_length():
    """
    Function shows an example of how to use progressbar on an unknown length
    Progress example: | 995 Elapsed Time: 0:00:10
    :return: none
    """
    bar = ProgressBar(max_value=UnknownLength)
    for i in range(1000):
        time.sleep(0.01)
        bar.update(i)

def read_csv_file(bar):
    """
    Function reads in a csv file using the DictReader (class csv.DictReader)
    Create an object which operates like a regular reader but maps the information
    read into a dict whose keys are given by the optional fieldnames parameter
    ref: https://docs.python.org/2/library/csv.html#csv.DictReader
    :return: none
    """
    with open('input.csv', newline='') as f:
        reader = csv.DictReader(f)
        header = next(reader)
        csv_to_dict(reader, header, bar)

def csv_to_dict(reader, header, bar):
    """
    Function takes the csv file column name and value and adds it to a dict object. The progressbar in
    this function is an example of an unknown length of the reader object (<class 'csv.DictReader'>)
    :param reader: contains the values in each column
    :param header: contains the column names
    :param bar: instance of ProgressBar
    :return: none
    """
    column_name = {}
    for name in header:
        column_name.setdefault(name, [])

    for row in bar(reader):
        column_name['cdatetime'].append(row.get('cdatetime', None))
        column_name['address'].append(row.get('address', None))
        column_name['district'].append(row.get('district', None))
        column_name['beat'].append(row.get('beat', None))
        column_name['grid'].append(row.get('grid', None))
        column_name['crimedescr'].append(row.get('crimedescr', None))
        column_name['ucr_ncic_code'].append(row.get('ucr_ncic_code', None))
        column_name['latitude'].append(row.get('latitude', None))
        column_name['longitude'].append(row.get('longitude', None))
        time.sleep(0.01)


if __name__ == "__main__":

    # Create instance of ProgressBar
    bar = ProgressBar()

    # Demo the main three commonly used progressbars
    wrapping_an_iterable(bar)
    # context_wrapper()
    # progressbars_unknown_length()

    # Demo of progressbar for unknown length
    # read_csv_file(bar)