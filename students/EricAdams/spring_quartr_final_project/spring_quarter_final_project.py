#! /usr/bin/env python

import webbrowser
import os
import logging
from Airports import airports, countries, runways,\
    navaids

logger = logging.getLogger('test_spring_quarter_final_project')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('test_spring_quarter_final_project.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Eric is an airplane enthusiast and heard about a website that has
#  all kinds of data on airports


def country_with_the_most_scheduled_nonscheduled_service_true():
    airport_obj = airports()
    result =\
        airport_obj.country_with_the_most_scheduled_nonscheduled_service(True)
    print(result)


def country_with_the_most_scheduled_nonscheduled_service_false():
    airport_obj = airports()
    result =\
        airport_obj.country_with_the_most_scheduled_nonscheduled_service(False)
    print(result)


def country_with_scheduled_service():
    pass


def home_page():
    pass


def lat_long():
    pass


def state_country():
    pass


def elevation_runway():
    pass


def wiki():
    pass


def land_737():
    pass


def runway_length():
    pass


def runway_lighted():
    pass


def runway_status():
    pass


def radio_freq():
    pass


def count_of_navaids():
    pass


def navaid_names():
    pass


def runway_width():
    pass


def navigate_to_our_airports_com(url):
    webbrowser.open(url, new=1)


# He goes to the website and finds that there are six csv files with
# airport data that are downloadable
# The files are named airport.csv, airport-frequencies.csv, runways.csv
# navaids.csv, countries.csv and regions.csv
# Intrigued, he downloads the files
# Curious as to what data are in these files, he opens them:
# airport.csv - appears to be a file with, well.. airport data
# He decides to list the column names
# He does this with all six files


def get_csv_files_in_current_directory():
    """ Return all .csv files in the current directory."""
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files

# Now that he knows what kind of data are in the files, he comes
# up with a list of questions to ask of the data.
# #
# 1. What country has the most airports with scheduled service
# 2 What country has the most airports with unscheduled service
# 3 How many airports are within 100 miles of Seattle
# 4 What does the home link say?
# 5 What is the lat/long of the airport?
# 6 What state/country is the airport in?
# 1 Does the airport have a wiki page?
# 2 Does the airport have a home link?
# 3 What does the wiki page say?

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
    while True:
        print('{:^60}'.format('MENU'))
        print("1."
              "  The country with the most airports with scheduled"
              " service")
        print("2."
              "  The country with the most airports with"
              "unscheduled service")
        print("3."
              "  The number of airports that are within 100 miles"
              " of Seattle")
        print("4."
              "  Bring up the home page for Seatac International")
        print("5.  The lat/long of Seatac International")
        print("6.  State/country Seatac is in")
        print("7.  Seatac runway(s) elevation(s)")
        print("8.  Bring up the wiki page for Seatac")
        print("9.  Can a 737 land at Seatac?")
        print("10.  Runway length(s) for Seatac")
        print("11.  Runway(s) lit at night?")
        print("12.  Runway(s) open or closed")
        print("13.  Radio frequencies in use at Seatac")
        print("14.  How many navigational aides are in the US")
        print("15.  What are the names of the navigational aids in the US")
        print("16.  How wide is, (are), the runway(s) at Seatac")
        answer = input("Make a choice, 1 - 16,"
                       " e.g. enter 16, (without the period)")
        try:
            if int(answer) in range(1, 17):
                break
        except ValueError as e:
            print("Please input a number between 1 and 16. ", e)
    answer_dict =\
        {
            "1": country_with_the_most_scheduled_nonscheduled_service_true,
            "2": country_with_the_most_scheduled_nonscheduled_service_false,
            "3": country_with_scheduled_service,
            "4": home_page,
            "5": lat_long,
            "6": state_country,
            "7": elevation_runway,
            "8": wiki,
            "9": land_737,
            "10": runway_length,
            "11": runway_lighted,
            "12": runway_status,
            "13": radio_freq,
            "14": count_of_navaids,
            "15": navaid_names,
            "16": runway_width,
        }
    answer_dict[answer]()
