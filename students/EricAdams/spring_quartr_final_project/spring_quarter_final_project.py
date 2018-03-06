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
    print('*' * 80)
    print(
        'country with most scheduled service airports,(number)')
    print('{0:>30},({1})'.format(result[0], result[1]))
    print('*' * 80)


def country_with_the_most_scheduled_nonscheduled_service_false():
    airport_obj = airports()
    result =\
        airport_obj.country_with_the_most_scheduled_nonscheduled_service(False)
    print('*' * 80)
    print(
        'country with most unscheduled service airports,(number)')
    print('{0:>30},({1})'.format(result[0], result[1]))
    print('*' * 80)


def towns_with_airports_within_100_miles_of_Seattle():
    airport_id = 'KSEA'
    airport_name = 'Seattle'
    airport_obj = airports()
    result = airport_obj.nearby_airports_within_one_degree(airport_id)
    print('*' * 80)
    print(
        'number of towns with airports within 100 miles of ', airport_name)
    print('{0:>30}'.format(len(result)))
    print('*' * 80)


def home_page():
    airport_obj = airports()
    result = airport_obj.airports_with_home_links()
    url = result["Seattle Tacoma International Airport"]
    airport_obj.open_web_page(url)


def lat_long():
    airport_obj = airports()
    airport_id = "KSEA"
    result =\
        airport_obj.nearby_airports_within_one_degree(
            airport_id, airport_lat_long=True)
    print('*' * 80)
    print('Latitude/Longitude of ', airport_id)
    print('{0:>30}/{1}'.format(result[0], result[1]))
    print('*' * 80)


def state_country():
    airport_obj = airports()
    airport_id = "KSEA"
    result =\
        airport_obj.nearby_airports_within_one_degree(
            airport_id, state_country=True)
    print('*' * 80)
    print('State-Country of ', airport_id)
    print('{0:>30}'.format(result[1]))
    print('*' * 80)


def elevation_runway():
    runway_obj = runways()
    airport_id = "KSEA"
    result =\
        runway_obj.runway_data_from_csv_file(airport_id, elevation=True)
    print('*' * 80)
    print('Runway elevations ', airport_id)
    # returned runway names are like 'runway_elevation_runway'
    for runway_name in result:
        runway = runway_name.split('_')
        print('{0}{1:>30}'.format(runway[2], result[runway_name]))
    print('*' * 80)


def wiki():
    airport_obj = airports()
    result = airport_obj.airports_with_wiki_pages()
    url = result["Seattle Tacoma International Airport"]
    airport_obj.open_web_page(url)


def land_737():
    # takes 6791 ft of runway to land a 737
    landing_737 = 6791.0
    landing_flag = False
    runway_obj = runways()
    airport_id = 'KSEA'
    result = runway_obj.runway_data_from_csv_file(airport_id, length=True)
    print('*' * 80)
    print('Runway lengths', airport_id)
    print('Runway name', ' ' * 10, 'Runway length', ' ' * 10, '737?')

    # returned runway names are like 'runway_elevation_runway'
    for runway_length in result:
        length = runway_length.split('_')
        if float(result[runway_length]) / landing_737 > 1.0:
            landing_flag = True
        print('{0}{1:>30}{2:>17}'.format(
            length[2], result[runway_length], landing_flag))
        landing_flag = False
    print('*' * 80)


def runway_length():
    runway_obj = runways()
    airport_id = 'KSEA'
    result = runway_obj.runway_data_from_csv_file(airport_id, length=True)
    print('*' * 80)
    print('Runway lengths', airport_id)
    print('Runway name', ' ' * 10, 'Runway length')

    # returned runway names are like 'runway_elevation_runway'
    for runway_length in result:
        length = runway_length.split('_')
        print('{0}{1:>30}'.format(length[2], result[runway_length]))
    print('*' * 80)


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
              "  The country with the most airports with "
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
            "3": towns_with_airports_within_100_miles_of_Seattle,
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
