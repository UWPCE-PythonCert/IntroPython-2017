#! /usr/bin/env python

import webbrowser
import urllib.request
import csv
import os
import operator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Eric is an airplane enthusiast and heard about a website that has
#  all kinds of data on airports


# def navigate_to_our_airports_com(url):
#     webbrowser.open(url, new=1)


# He goes to the website and finds that there are six csv files with
# airport data that are downloadable
# The files are named airport.csv, airport-frequencies.csv, runways.csv
# navaids.csv, countries.csv and regions.csv
# Intrigued, he downloads the files

def download_airport_data_csv_files(urls_filenames):
    """Download the file from `url` and save it locally
       under ./filename.
       :parameters urls_filenames = [(url1, filename1), (url2, filename2)...]
    """
    for url, filename in urls_filenames:

        if not os.path.isfile(filename):
            with urllib.request.urlopen(url):
                with open(filename, 'w'):
                    urllib.request.urlretrieve(url, filename)


# Curious as to what data are in these files, he opens them:
# airport.csv - appears to be a file with, well.. airport data
# He decides to list the column names
# He does this with all six files

def get_csv_files_in_current_directory():
    """ Return all .csv files in the current directory."""
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files


def get_column_names_in_csv_file(filename):
    """ Return the column names from a csv file.
    :parameters - filename = name of the csv file.
    """
    with open(filename, "r") as file_obj:
        line = file_obj.readline()
        return line

# Now that he knows what kind of data are in the files, he comes
# up with a list of questions to ask of the data.
# #
# 1. What country has the most airports with scheduled service


def get_list_of_records_from_a_csv_file(filename):
    """Return the records from a csv file in list form.
    :params - filename - a .csv file.
    :return - the list returned will be in the form list[row][column]
    """
    with open(filename, 'r') as file_obj:
        csv_reader_obj = csv.reader(file_obj)
        list_of_records = [record for record in csv_reader_obj]
    return list_of_records


def number_of_scheduled_or_nonscheduled_service_airports_per_country(scheduled_or_not_scheduled):
    """Use the airports.csv, existing in current working directory.
    Return a dict of
    {country_code:number_of_schedule_or_not_scheduled_airports}
    :params - scheduled_or_not_scheduled boolean True = get scheduled airports,
    False = get unscheduled airports.
    """
    # list_of_records_for_airport_csv[row][8] = country code
    # list_of_records_for_airport_csv[row][11] = scheduled service
    # list_of_records_for_airport_csv[row][1] = airport ident

    # {country_name:number_of_airports_with_scheduled_service}

    list_of_records_for_airports = get_list_of_records_from_a_csv_file(
        'airports.csv')
    list_of_countries_and_service = []
    number_of_airports_with_service_or_no_service_per_country = {}
    for row in list_of_records_for_airports:
        list_of_countries_and_service.append([row[8], row[11]])
    for country in list_of_countries_and_service:
        # Sample entry of country = country['JP', 'no']
        if country[0] in number_of_airports_with_service_or_no_service_per_country:
            number_of_airports_with_service_or_no_service_per_country[country[0]] += 1
        else:
            number_of_airports_with_service_or_no_service_per_country[country[0]] = 1
    return number_of_airports_with_service_or_no_service_per_country
    # To do list:
    # add an "airport has service" flag
    # country[1] is the service indicator, yes or no
    # populate number_of_airports_with_service_or_no_service_per_country based on flag = True or False



def country_with_the_most_scheduled_nonscheduled_service(scheduled_or_nonscheduled):
    """ Using the airport.csv in the current directory, return
    the country with the least or with the most scheduled service airports.
    :params = Boolean.  If True, return the country with the most airports
    with scheduled service.  If False then return the country
    with the most airports without scheduled service.
    """
    number_of_scheduled_nonscheduled_service_airports_in_each_country = number_of_scheduled_or_nonscheduled_service_airports_per_country(scheduled_or_nonscheduled)
    sorted_by_value_descending = sorted(number_of_scheduled_nonscheduled_service_airports_in_each_country.items(), key=operator.itemgetter(1), reverse=True)
    country_code = sorted_by_value_descending[0][0]
    return country_code, sorted_by_value_descending[00], sorted_by_value_descending[0][1]


def country_code_to_country_conversion(country_code):
    '''
    countries.csv and airport.csv are in the current directory
    country codes to country mapped in countries.csv
    :params - country_code = country code to look up in
    the countries.csv file
    '''
    # list_of_records_for_countries_csv[row][1] =  countrycode
    # list_of_records_for_countries_csv[row][2] = country name


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


# if __name__ == "__main__":
# country_with_most_scheduled_service_airports()
