#! /usr/bin/env

"""
sprint_quarter_final_project.py

The class file is Airports.py.
When each class is instantiated, csv files will be automatically
downloaded from the website ourairports.com.

The downloaded csv files contain airport, runway, and navigational aid data.
This script will process the data in order to answer 17 questions.

Required files:
              Airports.py

Args:
    none, just run the script e.g. python3 sprint_quarter_final_project.py

Output:
      A log file is generated in the current directory, called
      test_spring_quarter_final_project.log.

      All output, other than the log, is output on stdout
"""


import webbrowser
import os
import logging
import sys
from Airports import airports, countries, runways,\
    navaids

logger = logging.getLogger('test_spring_quarter_final_project')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('test_spring_quarter_final_project.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def country_with_the_most_scheduled_nonscheduled_service_true():
    """ Find the country with the most scheduled service airports.

    Args:
        None

    Returns:
           Writes to stdout
    """
    airport_obj = airports()
    result =\
        airport_obj.country_with_the_most_scheduled_nonscheduled_service(True)
    print('*' * 80)
    print(
        'country with most scheduled service airports,(number)')
    print('{0:>30},({1})'.format(result[0], result[1]))
    print('*' * 80)


def country_with_the_most_scheduled_nonscheduled_service_false():
    """ Find the country with the most nonscheduled service airports.

    Args:
        None

    Returns:
           Writes to stdout
    """
    airport_obj = airports()
    result =\
        airport_obj.country_with_the_most_scheduled_nonscheduled_service(False)
    print('*' * 80)
    print(
        'country with most unscheduled service airports,(number)')
    print('{0:>30},({1})'.format(result[0], result[1]))
    print('*' * 80)


def towns_with_airports_within_100_miles_of_Seattle():
    """ Find all of the airports within 100 miles of Seattle.

    Args:
        None

    Returns:
           Writes to stdout
    """
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
    """ Open the home page of Seatac airport.

    Args:
        None

    Returns:
           Opens a web page in a separate window
    """
    airport_obj = airports()
    result = airport_obj.airports_with_home_links()
    url = result["Seattle Tacoma International Airport"]
    airport_obj.open_web_page(url)


def lat_long():
    """ Display the lat/long of Seatac airport.

    Args:
        None

    Returns:
           Displays lat/long of Seatac on stdout
    """
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
    """ Display the country thatSeatac airport is in.

    Args:
        None

    Returns:
           Displays the state that Seatac is in on stdout
    """
    airport_obj = airports()
    country_obj = countries()
    airport_id = "KSEA"
    result =\
        airport_obj.nearby_airports_within_one_degree(
            airport_id, state_country=True)
    country = country_obj.country_code_to_country_conversion(result[0])
    print('*' * 80)
    print('State-Country of ', airport_id)
    print('{0:>30}'.format(country))
    print('*' * 80)


def elevation_runway():
    """ Display the length of all of Seatac airport's
    runways.

    Args:
        None

    Returns:
           Displays the length of each runway at Seatac on stdout
    """
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
    """ Display the wiki page of Seatac airport
    runways.

    Args:
        None

    Returns:
           Displays Seatac airport's wiki page on stdout
    """
    airport_obj = airports()
    result = airport_obj.airports_with_wiki_pages()
    url = result["Seattle Tacoma International Airport"]
    airport_obj.open_web_page(url)


def land_737():
    """ Find out if a 737 can land at Seatac airport.
    runways.

    Args:
        None

    Returns:
           Displays whether or not a 737 can land at Seatac on stdout.
    """
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
    """ Display the runway length(s) of Seatac airport.

    Args:
        None

    Returns:
           Displays the runway lenght(s) of Seatac airport on stdout.
    """
    runway_obj = runways()
    airport_id = 'KSEA'
    result = runway_obj.runway_data_from_csv_file(airport_id, length=True)
    print('*' * 80)
    print('Runway lengths', airport_id)
    print('Runway name', ' ' * 10, 'Runway length')
    # returned runway names are like 'runway_length_runway'
    for runway_length in result:
        length = runway_length.split('_')
        print('{0}{1:>30}'.format(length[2], result[runway_length]))
    print('*' * 80)


def runway_lighted():
    """ Find out and display if the runway(s) of Seatac airport
    are lighted at night.

    Args:
        None

    Returns:
           Displays if the runway(s) of Seatac airport are lighted
           at night. The display goes to stdout.
    """
    runway_obj = runways()
    airport_id = 'KSEA'
    runway_lit_dict = {}
    result = runway_obj.runway_data_from_csv_file(airport_id)
    for key in result:
        if '_lit_' in key:
            # returned runway names are like 'runway_lit_runway'
            name = key.split('_')
            runway_lit_dict[str(name[3])] = result[key]
    print('*' * 80)
    print('Runway lights', airport_id)
    print('Runway name', ' ' * 10, 'Runway lighted')
    for keys in runway_lit_dict:
        if runway_lit_dict[keys] == '1':
            flag = 'yes'
        else:
            flag = 'no'
        print('{0}{1:>30}'.format(keys, flag))
    print('*' * 80)


def runway_status():
    """ Find out and display if the runway(s) of Seatac airport
    are open or closed to landing.

    Args:
        None

    Returns:
           Displays if the runway(s) of Seatac airport are open
           or closed to landing. The display goes to stdout.
    """
    runway_obj = runways()
    airport_id = 'KSEA'
    result = runway_obj.runway_data_from_csv_file(airport_id, status=True)
    print('*' * 80)
    print('Runway status', airport_id)
    print('Runway name', ' ' * 10, 'Runway status')
    # returned runway names are like 'runway_closed_runway'
    for key in result:
        name = key.split('_')
        if result[key] == '1':
            flag = 'closed'
        else:
            flag = 'open'
        print('{0}{1:>30}'.format(name[2], flag))
    print('*' * 80)


def count_of_navaids():
    """ Find out and display how many navigational aids
    to aircraft are in the US.

    Args:
        None

    Returns:
           Displays how many navigational aids to
           aircraft there are in the US.  The display goes to stdout.
    """
    navaid_obj = navaids()
    country = 'US'
    result = navaid_obj.nav_aids_data_from_csv_file(country)
    print('*' * 80)
    print('{0:^80}{1:^80}'.format('Navaids', country))
    # print('Runway name', ' ' * 10, 'Runway status')
    # print(result)
    # print(len(result['US']))
    print('{0:^80}'.format(len(result['US'])))
    print('*' * 80)


def navaid_names():
    """ Find out and display the names of navigational aids
    to aircraft near Seatac airport.

    Args:
        None

    Returns:
           Displays the names of each of the navigational aids to aircraft near
           Seatac  The display goes to stdout.
    """
    navaid_obj = navaids()
    country = 'US'
    airport_id = 'KSEA'
    result = navaid_obj.nav_aids_data_from_csv_file(country, airport_id)
    print('*' * 80)
    print('{0:^80}'.format('Navaid names around Seatac'))
    for nav in result['KSEA']:
        print('{0:^80}'.format(nav))
    print('*' * 80)


def runway_width():
    """ Find out and display the width of the runways at Seatac airport.

    Args:
        None

    Returns:
           Displays the width of each of the runways at
           Seatac airport.  The display goes to stdout.
    """
    runway_obj = runways()
    airport_id = 'KSEA'
    result = runway_obj.runway_data_from_csv_file(airport_id)
    runway_width_dict = {}
    print('*' * 80)
    print('Runway widths', airport_id)
    print('Runway name', ' ' * 10, 'Runway width')
    # returned runway names are like 'runway_width_runway'
    for key in result:
        if '_width_' in key:
            # returned runway names are like 'runway_width_runway'
            name = key.split('_')
            runway_width_dict[str(name[2])] = result[key]
            width = runway_width_dict[str(name[2])]
            runway_name = str(name[2])
            print('{0}{1:>30}'.format(runway_name, width))
    print('*' * 80)


def navigate_to_our_airports_com(url):
    """ Display the web page of ourairports.com.

    Args:
        url of the website

    Returns:
           Displays web page of ourairports.com.
    """
    webbrowser.open(url, new=1)


def our_airports_web_site():
    """ Display the data page of ourairports.com.

    Args:
        url of the website's data page

    Returns:
           Displays data web page of ourairports.com.
    """
    url = "http://ourairports.com/data"
    navigate_to_our_airports_com(url)


def exit_program():
    """ Exit the program """
    sys.exit()


def get_csv_files_in_current_directory():
    """ Find  all .csv files in the current directory.

    Args:
        None

    Return:
          files (list):  a list of csv files in the current directory.
    """
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files


def get_data_files_in_current_directory():
    """ Define a wrapper function used in answering
    the question about what data files are used

    Args:
        None

    Returns:
           Displays a list of csv files in the current directory
    """
    files = get_csv_files_in_current_directory()
    print('*' * 80)
    for file in files:
        print(file)
    print('*' * 80)


if __name__ == "__main__":
    while True:
        print('\n\n{:^60}\n\n'.format('MENU'))
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
        print("13.  How many navigational aides are in the US")
        print("14.  What are the names of the navigational aids around Seatac")
        print("15.  How wide is, (are), the runway(s) at Seatac")
        print("16.  What files contain all this data")
        print("17.  Where did the files come from")
        print("18.  Exit the program")
        answer = input("Make a choice, 1 - 18,"
                       " e.g. enter 15, (without the period)")
        answer_dict =\
            {
                "1": country_with_the_most_scheduled_nonscheduled_service_true,
                "2":
                country_with_the_most_scheduled_nonscheduled_service_false,
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
                "13": count_of_navaids,
                "14": navaid_names,
                "15": runway_width,
                "16": get_data_files_in_current_directory,
                "17": our_airports_web_site,
                "18": exit_program,
            }
        try:
            answer_dict[answer]()
        except KeyError:
            print("You entered ", answer,
                  "Please input a number between 1 and 17.")
