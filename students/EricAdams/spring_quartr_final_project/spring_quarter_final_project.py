#! /usr/bin/env python

# Eric is an airplane enthusiast and heard about a website that has
#  all kinds of data on airports

import webbrowser
import urllib.request
import csv
import os


def navigate_to_our_airports_com(url):
    webbrowser.open(url, new=1)


# He goes to the website and finds that there are six csv files with
# airport data that are downloadable
# The files are named airport.csv, airport-frequencies.csv, runways.csv
# navaids.csv, countries.csv and regions.csv
# Intrigued, he downloads the files

def download_airport_data_csv_files(url, filename):
    '''Download the file from `url` and save it locally
       under `file_name`
    '''
    with urllib.request.urlopen(url):
        with open(filename, 'w'):
            urllib.request.urlretrieve(url, filename)


# Curious as to what data are in these files, he opens them:
# airport.csv - appears to be a file with, well.. airport data
# He decides to list the column names
# He does this with all six files

def get_csv_files_in_current_directory():
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files


def get_column_names_in_csv_file(filename):
    with open(filename, "r") as file_obj:
        line = file_obj.readline()
        return line

# Now that he knows what kind of data are in the files, he comes
# up with a list of questions to ask of the data.
# #
# 1. What country has the most airports with scheduled service


def country_with_most_scheduled_service_airports():
    return 'CN'

# 2 What country has the most airports with unscheduled service
# 3 How many airports are within 100 miles of Seattle
#  Some random questions
# 1 Does the airport have a wiki page?
# 2 What does the wiki page say?
#     import webbrowser

#     url = wikipage for airport
#     webbrowser.open(url, new=1) #new=1 new window
#
# 3 Does the airport have a home link?
# 4 What does the home link say?
# 5 What is the lat/long of the airport?
# 6 What state/country is the airport in?
# 7 What is the field elevation?
# 8 Can the airport land big planes?
# 9 How long is the airport?
# 10 How wide?
# 11 Can a plane land at night?
# 12 Is the runway paved?
# 13 Is the airport even open to use?
# 14 What radio frequencies are used?
# 15 How many navigational aids for airplanes in the country?
# 16 Navigational aid title?

if __name__ == "__main__":
    download_airport_data_csv_files("http://ourairports.com/data/airports.csv", 'junk.csv')
