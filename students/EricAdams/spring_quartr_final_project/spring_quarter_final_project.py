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


def navigate_to_our_airports_com(url):
    webbrowser.open(url, new=1)


# He goes to the website and finds that there are six csv files with
# airport data that are downloadable
# The files are named airport.csv, airport-frequencies.csv, runways.csv
# navaids.csv, countries.csv and regions.csv
# Intrigued, he downloads the files

# def download_airport_data_csv_files(urls_filenames):
#     """Download the file from `url` and save it locally
#        under ./filename.
#        :parameters urls_filenames = [(url1, filename1), (url2, filename2)...]
#     """
#     for url, filename in urls_filenames:

#         if not os.path.isfile(filename):
#             with urllib.request.urlopen(url):
#                 with open(filename, 'w'):
#                     urllib.request.urlretrieve(url, filename)


# Curious as to what data are in these files, he opens them:
# airport.csv - appears to be a file with, well.. airport data
# He decides to list the column names
# He does this with all six files

def get_csv_files_in_current_directory():
    """ Return all .csv files in the current directory."""
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return files


# def get_column_names_in_csv_file(filename):
#     """ Return the column names from a csv file.
#     :parameters - filename = name of the csv file.
#     """
#     with open(filename, "r") as file_obj:
#         line = file_obj.readline()
#         return line

# Now that he knows what kind of data are in the files, he comes
# up with a list of questions to ask of the data.
# #
# 1. What country has the most airports with scheduled service
# 2 What country has the most airports with unscheduled service


# def get_list_of_records_from_a_csv_file(filename):
#     """Return the records from airports.csv or countries.csv file in list form.
#     :params - filename - airport.csv or countries.csv.
#     :return - the list returned will be in the form list[row][column]
#     """
#     with open(filename, 'r') as file_obj:
#         csv_reader_obj = csv.reader(file_obj)
#         # skip the first line of the file, which lists the column names
#         list_of_records = [
#             record for record in csv_reader_obj if record[0] != 'id']
#     return list_of_records


# def number_of_scheduled_or_nonscheduled_service_airports_per_country(
#         scheduled_or_not_scheduled):
#     """Use the airports.csv, existing in current working directory.
#     Return a dict of
#     {country_code:number_of_schedule_or_not_scheduled_airports}
#     :params - scheduled_or_not_scheduled boolean True = get scheduled airports,
#     False = get unscheduled airports.
#     """
#     # list_of_records_for_airport_csv[row][8] = country code
#     # list_of_records_for_airport_csv[row][11] = scheduled service
#     # list_of_records_for_airport_csv[row][1] = airport ident

#     # {country_name:number_of_airports_with_scheduled_service}

#     list_of_records_for_airports = get_list_of_records_from_a_csv_file()
#     list_of_countries_and_service = []
#     number_of_airports_with_service_or_no_service_per_country = {}
#     for row in list_of_records_for_airports:
#         list_of_countries_and_service.append([row[8], row[11]])
#     for country in list_of_countries_and_service:
#         # Sample entry of country = country['JP', 'no'] or ['JP', 'yes']
#         if scheduled_or_not_scheduled is True:
#             scheduled_or_not_scheduled = "yes"
#         if scheduled_or_not_scheduled is False:
#             scheduled_or_not_scheduled = "no"
#         if country[1] == scheduled_or_not_scheduled:
#             if country[0] in number_of_airports_with_service_or_no_service_per_country:
#                 number_of_airports_with_service_or_no_service_per_country[country[0]] += 1
#             else:
#                 number_of_airports_with_service_or_no_service_per_country[country[0]] = 1
#     # the return will be a dict with entries like {'US':22398, ...}
#     return number_of_airports_with_service_or_no_service_per_country


# def country_with_the_most_scheduled_nonscheduled_service(scheduled_or_nonscheduled):
#     """ Using the airport.csv in the current directory, return
#     the country with the least or with the most scheduled service airports.
#     Also return the number of airports
#     :params = Boolean.  If True, return the country with the most airports
#     with scheduled service.  If False then return the country
#     with the most airports without scheduled service.
#     :return - a tuple (country, number of airports with or without scheduled service)
#     """
#     number_of_scheduled_nonscheduled_service_airports_in_each_country = number_of_scheduled_or_nonscheduled_service_airports_per_country(
#         scheduled_or_nonscheduled)
#     sorted_by_value_descending = sorted(number_of_scheduled_nonscheduled_service_airports_in_each_country.items(
#     ), key=operator.itemgetter(1), reverse=True)
#     # print(sorted_by_value_descending)
#     country_code = sorted_by_value_descending[0][0]
#     country = country_code_to_country_conversion(country_code)
#     return country, sorted_by_value_descending[0][1]


# def country_code_to_country_conversion(country_code):
#     '''
#     Retrieve the country from countries.csv, given the country code.
#     countries.csv must in the current directory
#     country codes to country mapped in countries.csv
#     :params - country_code as displayed in the airports.csv file
#     '''
#     # list_of_records_for_countries_csv[row][1] =  countrycode
#     # list_of_records_for_countries_csv[row][2] = country name
#     list_of_records = get_list_of_records_from_a_csv_file('countries.csv')
#     for record in list_of_records:
#         if country_code == record[1]:
#             return record[2]


# 3 How many airports are within 100 miles of Seattle
# 5 What is the lat/long of the airport?
# 6 What state/country is the airport in?

# def nearby_airports_within_one_degree(airport_id, airport_lat_long=False, state_country=False):
#     """ Find other airports within a 1 deg.lat/long of airport_id.
#     :params - airport_id.  Id of the airport as shown in airports.csv
#     :return - a list of towns with airports within +- 1 deg. lat/long of airport_id.
#     """
#     # list_of_records[row][column]
#     list_of_records = get_list_of_records_from_a_csv_file('airports.csv')
#     # airport id in column 2, lat, long in column 5 and 6, airport name is in
#     # column 4, municipality in row[10]
#     # initialize airport_id_lat to determine if param is correct
#     # country = row[8]
#     # region = fow[9]

#     nearby_airports = []
#     country_state = []
#     for row in list_of_records:
#         # data for airport_id
#         if row[1] == airport_id:
#             airport_id_lat = row[4]
#             airport_id_long = row[5]
#             country_state.append(row[8])
#             country_state.append(row[9])

#             nearby_airport_max_lat = float(airport_id_lat) + 1.0
#             nearby_airport_min_lat = float(airport_id_lat) - 1.0
#             nearby_airport_max_long = float(airport_id_long) + 1.0
#             nearby_airport_min_long = float(airport_id_long) - 1.0
#     try:
#         if airport_id_lat is None:
#             pass
#     except UnboundLocalError as err:
#         print("Airport Id can not be found.\n"
#               "Make sure that"
#               "nearby_airports_within_two_degrees(airport_id)"
#               " has the correct airport_id\n", err)
#         raise
#     for row in list_of_records:
#         if row[10] not in nearby_airports:
#             if float(row[4]) <= nearby_airport_max_lat\
#                     and float(row[4]) >= nearby_airport_min_lat:
#                 if float(row[5]) <= nearby_airport_max_long\
#                         and float(row[5]) >= nearby_airport_min_long:
#                     nearby_airports.append(row[10])
#     if airport_lat_long is False and state_country is False:
#         return nearby_airports
#     if airport_lat_long is True and state_country is False:
#         return airport_id_lat, airport_id_long
#     if airport_lat_long is False and state_country is True:
#         return country_state
#     if airport_lat_long is True and state_country is True:
#         return country_state, airport_id_lat, airport_id_long


# def airports_with_home_links():
#     """ Return a list of airports from the airports.csv file and their
#      home web page
#     airports.csv exists in working directory.
#     """
#     list_of_records = get_list_of_records_from_a_csv_file('airports.csv')
#     # list_of_records_for_airport_csv[row][15] = home_link
#     # list_of_records_for_airport_csv[row][16] = wiki page
#     # list_of_records_for_airport_csv[row][3] = airport name

#     # dict{name:homepage}
#     airport_names_homepage = {}
#     for row in list_of_records:
#         if row[3] != "name":
#             if "http" in row[15]:
#                 airport_names_homepage[row[3]] = row[15]
#     return airport_names_homepage


#  Some random questions
# 1 Does the airport have a wiki page?
# 2 Does the airport have a home link?

# def airports_with_wiki_pages():
#     """ Return a list of airports from the airports.csv file and their
#     wiki web page.
#     airports.csv exists in working directory.
#     """
#     list_of_records = get_list_of_records_from_a_csv_file('airports.csv')
#     # list_of_records_for_airport_csv[row][15] = home_link
#     # list_of_records_for_airport_csv[row][16] = wiki page
#     # list_of_records_for_airport_csv[row][3] = airport name

#     # dict{name:wiki}
#     airport_names_wiki = {}
#     for row in list_of_records:
#         if row[3] != "name":
#             if "http" in row[16]:
#                 airport_names_wiki[row[3]] = row[16]
#     return airport_names_wiki

# 3 What does the wiki page say?
# 4 What does the home link say?


# def open_web_page(url_of_web_page):
#     """Open a web page in a new window"""
#     url = url_of_web_page
#     # new=1 opens in a new window
#     webbrowser.open(url, new=1)


# 7 What is the field elevation?
# 8 Can the airport land big planes?
# 9 How long is the airport?
# 10 How wide?
# 11 Can a plane land at night?
# 12 Is the runway paved?
# 13 Is the airport even open to use?


def runway_data_from_csv_file(airport_id, length=False,
                              status=False, elevation=False):
    """ Create a list of runway data, derived from runway.csv.
    Args:
         airport_id (str):  From column 2 of runway.csv. This is the
                            unique airport identifier
         length (bool):     See Returns section for usage

         status (bool):     See Returns section for usage

         elevation (bool):  See Returns section for usage

    Returns:
         dict:  The default returned dict has 6 key value pairs for each
                of the airport_id's runways. The keys will be:
                'runway_elevation_xx'
                'runway_length_xx'
                'runway_width_xx'
                'runway_is_lit_xx'
                'runway_paved_xx'
                'runway_closed_xx'
                where xx is the runway name.  The values are all strings

                Usage of the boolean args:
                length=False, status=False, elevation=True: returns
                the field elevations
                length=False, status=True, elevation=False: returns
                the field status
                length=False, status=True, elevation=True:  returns
                field elevations and field status
                length=True, status=False, elevation=False: returns
                the field lengths
                length=True, status=False, elevation=True:  returns
                the field lengths and elevations
                length=True, status=True, elevation=False:  returns
                the field lengths and status
                length=True, status=True, elevation=True:   returns
                the field lengths, status, and elevations
    """
    #  Column names in runways.csv
    # row[0] = "id",
    # row[1] = "airport_ref",
    # row[2] = "airport_ident",
    # row[3] = "length_ft",
    # row[4] = "width_ft",
    # row[5] = "surface",
    # row[6] = "lighted",
    # row[7] = "closed",
    # row[8] = "le_ident",
    # row[9] = "le_latitude_deg",
    # row[10] = "le_longitude_deg",
    # row[11] = "le_elevation_ft",
    # row[12] = "le_heading_degT",
    # row[13] = "le_displaced_threshold_ft",
    # row[14] = "he_ident",
    # row[15] = "he_latitude_deg",
    # row[16] = "he_longitude_deg",
    # row[17] = "he_elevation_ft",
    # row[18] = "he_heading_degT",
    # row[19] = "he_displaced_threshold_ft",

    list_of_records = get_list_of_records_from_a_csv_file('runways.csv')
    runway_info = {}
    for row in list_of_records:
        # data for airport_id
        if row[2] == airport_id:
            # ensure an entry for multiple runways
            runway = row[8]
            runway_info['runway_elevation_' + runway] = row[11]
            runway_info['runway_length_' + runway] = row[3]
            runway_info['runway_width_' + runway] = row[4]
            runway_info['runway_is_lit_' + runway] = row[6]
            runway_info['runway_paved_' + runway] = row[5]
            runway_info['runway_closed_' + runway] = row[7]
    if length is False and status is False and elevation is False:
        return runway_info
    if length is False and status is False and elevation is True:
        runway_elevation_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_elevation_'):
                runway_elevation_dict[key] = runway_info[key]
        return runway_elevation_dict
    if length is False and status is True and elevation is False:
        runway_closed_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_closed_'):
                runway_closed_dict[key] = runway_info[key]
        return runway_closed_dict
    if length is False and status is True and elevation is True:
        runway_status_elevation_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_closed_')\
                    or key.startswith('runway_elevation_'):
                runway_status_elevation_dict[key] = runway_info[key]
        return runway_status_elevation_dict
    if length is True and status is False and elevation is False:
        runway_length_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_length_'):
                runway_length_dict[key] = runway_info[key]
        return runway_length_dict
    if length is True and status is False and elevation is True:
        runway_length_elevation_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_length_')\
                    or key.startswith('runway_elevation_'):
                runway_length_elevation_dict[key] = runway_info[key]
        return runway_length_elevation_dict
    if length is True and status is True and elevation is False:
        runway_length_status_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_length_')\
                    or key.startswith('runway_closed_'):
                runway_length_status_dict[key] = runway_info[key]
        return runway_length_status_dict
    if length is True and status is True and elevation is True:
        runway_length_status_elevation_dict = {}
        for key in list(runway_info.keys()):
            if key.startswith('runway_length_')\
                    or key.startswith('runway_closed_')\
                    or key.startswith('runway_elevation'):
                runway_length_status_elevation_dict[key] = runway_info[key]
        return runway_length_status_elevation_dict


def nav_aids_data_from_csv_file(country, airport_id=''):
    """ Find the navigational aids to aviation, name and type,
    by country or airport

    Args:
         country (str):     ISO_Country as listed in countries.csv
         airport_id (str):  airport id as listed in airports.csv,
                            or as listed under associated airport
                            in navaids.csv

    Return:
          dict:  default return is a dict of navigational aids per country,
                 e.g. {"country":["name_of_navaid","type_of_navaid"]}
                 If airport_id is not empty then a dict of navaids for that
                 airport is returned.
                 e.g {"airport_id":["Country","name_of_navaid",
                 "type_of_navaid"]}
    """
    # column names in navaids.csv
    # row[0] = "id",
    # row[1] = "filename",
    # row[2] = "ident",
    # row[3] = "name",
    # row[4] = "type",
    # row[5] = "frequency_khz",
    # row[6] = "latitude_deg",
    # row[7] = "longitude_deg",
    # row[8] = "elevation_ft",
    # row[9] = "iso_country",
    # row[10] = "dme_frequency_khz",
    # row[11] = "dme_channel",
    # row[12] = "dme_latitude_deg",
    # row[13] = "dme_longitude_deg",
    # row[14] = "dme_elevation_ft",
    # row[15] = "slaved_variation_deg",
    # row[16] = "magnetic_variation_deg",
    # row[17] = "usageType",
    # row[18] = "power",
    # row[19] = "associated_airport",

    navaids_per_country = {}
    navaid_name_country = []
    list_of_records = get_list_of_records_from_a_csv_file('navaids.csv')
    if airport_id == '':
        for row in list_of_records:
            if row[9] == country:
                navaid_name_country.extend([row[3], row[4]])
                navaids_per_country[row[9]] = navaid_name_country[:]
        # navaid_name_country.clear()
        return navaids_per_country
    else:
        for row in list_of_records:
            if row[19] == airport_id:
                navaid_name_country.extend([row[3], row[4]])
                navaids_per_country[row[19]] = navaid_name_country[:]
                # keys are now airport names instead of countries
        return navaids_per_country


# 14 What radio frequencies are used?
# 15 How many navigational aids for airplanes in the country?
# 16 Navigational aid title?


# if __name__ == "__main__":
# country_with_most_scheduled_service_airports()
