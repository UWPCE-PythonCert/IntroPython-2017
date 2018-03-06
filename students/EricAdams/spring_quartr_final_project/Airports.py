import os
import urllib.request
import urllib.error
import operator
import csv
import webbrowser
import logging


class airports():
    """ Create some methods to help answer some questions
    on the airports data file.data.
    """

    def __init__(self, url="http://ourairports.com/data/airports.csv",
                 filename="airports.csv"):
        """ Download the file from `url` and save it locally
            under ./filename.
        Args:
            url (str): url of the csv file. Defaults to
                       "http://ourairports.com/data/airports.csv"
            filename (str): name of the file to save to in the current
                            working directory. Defaults to "airports.csv"

        Return:
              None
        """
        # in case this class is subclassed
        if 'airports' in str(type(self)):
            self.logger = logging.getLogger(
                'test_spring_quarter_final_project.Airports.airports')
            self.logger.info('Creating an instance of airports')
        self.url = url
        self.filename = filename
        if not os.path.isfile(self.filename):
            try:
                with urllib.request.urlopen(self.url):
                    with open(self.filename, 'w'):
                        urllib.request.urlretrieve(self.url, self.filename)
            except urllib.error.URLError as e:
                self.logger.error("Check internet connection ", e)

    def get_column_names_in_csv_file(self, filename="airports.csv"):
        """ Return the column names from the airport.csv file.
        Args:
            filename (str): name of the csv file. Defaults to "airports.csv"

        Return:
              columns (str):  column names in csv file
        """
        self.filename = filename
        with open(self.filename, "r") as file_obj:
            line = file_obj.readline()
        columns = line.split(',')
        self.logger.info('Finished get_column_names_in_csv_file'
                         ' returning columns')
        return columns

    def get_list_of_records_from_a_csv_file(self, filename='airports.csv'):
        """Return the records from a csv file.  airports.csv is the default csv file.
        files must be in the current directory

        Args:
            filename (str):  airport.csv or countries.csv.

        Return:
              Records (list):  the list returned will be in the form
                               Records[row][column]
        """
        try:
            # avoids unbound error
            list_of_records = []
            with open(filename, 'r') as file_obj:
                csv_reader_obj = csv.reader(file_obj)
                # skip the first line of the file, which lists the column names
                list_of_records = [
                    record for record in csv_reader_obj if record[0] != 'id']
        except FileNotFoundError as e:
            self.logger.error("No .csv files, error is: ", e)
            raise
        self.logger.info('Finished get_list_of_records_from_a_csv_file'
                         ' returning list_of_records')
        return list_of_records

    def number_of_scheduled_or_nonscheduled_service_airports_per_country(
            self, scheduled_or_not_scheduled):
        """ Create a dictionary {country:xxxx} where xxxx is the number of
        airports with scheduled service or without scheduled service.
        airports.csv must be in the current directory.

        Args:
            scheduled_or_not_scheduled (bool):
                                             True - return number of scheduled
                                                service airports per country
                                             False - return number of airports
                                                without scheduled service.

        Return:
              number_of_airports_with_service_or_no_service_per_country (dict):
              a dict in the form of
              {country:numer_of_airports_with_without_service} key = (str),
              value = (int)
        """
    # list_of_records_for_airport_csv[row][8] = country code
    # list_of_records_for_airport_csv[row][11] = scheduled service
    # list_of_records_for_airport_csv[row][1] = airport ident

    # {country_name:number_of_airports_with_scheduled_service}

        self.scheduled_or_not_scheduled = scheduled_or_not_scheduled

        list_of_records_for_airports =\
            self.get_list_of_records_from_a_csv_file()
        list_of_countries_and_service = []
        number_of_airports_with_service_or_no_service_per_country = {}
        for row in list_of_records_for_airports:
            list_of_countries_and_service.append([row[8], row[11]])
        for country in list_of_countries_and_service:
            # Sample entry of country = country['JP', 'no'] or ['JP', 'yes']
            if self.scheduled_or_not_scheduled is True:
                self.scheduled_or_not_scheduled = "yes"
            if self.scheduled_or_not_scheduled is False:
                self.scheduled_or_not_scheduled = "no"
            if country[1] == self.scheduled_or_not_scheduled:
                if country[0] in\
                        number_of_airports_with_service_or_no_service_per_country:
                    number_of_airports_with_service_or_no_service_per_country[country[0]] += 1
                else:
                    number_of_airports_with_service_or_no_service_per_country[country[0]] = 1
        # the return will be a dict with entries like {'US':22398, ...}
        self.logger.info(
            'Finished'
            ' number_of_scheduled_or_nonscheduled_service_airports_per_country'
            ' returning'
            ' number_of_airports_with_service_or_no_service_per_country')
        return number_of_airports_with_service_or_no_service_per_country

    def country_with_the_most_scheduled_nonscheduled_service(self, scheduled_or_nonscheduled=True):
        """ Find the country with the most scheduled or nonscheduled service
        airports.  Airport.csv must be in the current directory.

        Args:
            scheduled_or_non_scheduled (bool):
                                            True, return the country with the
                                            most airports with scheduled
                                            service.
                                            False return the country
                                            with the most airports without
                                            scheduled service.
        Return:
              country, sorted_by_value_descending[0][1] (tuple):
                                                               country (str)
                                                               sorted_by_value_descending[0][1] (int)
        """
        number_of_scheduled_nonscheduled_service_airports_in_each_country =\
            self.number_of_scheduled_or_nonscheduled_service_airports_per_country(
                scheduled_or_nonscheduled)
        sorted_by_value_descending =\
            sorted(number_of_scheduled_nonscheduled_service_airports_in_each_country.items(
            ), key=operator.itemgetter(1), reverse=True)
        # print(sorted_by_value_descending)
        country_code = sorted_by_value_descending[0][0]
        country_obj = countries()
        country = country_obj.country_code_to_country_conversion(country_code)
        self.logger.info(
            'Finished country_with_the_most_scheduled_nonscheduled_service'
            ' returning country, sorted_by_value_descending[0][1]')
        return country, sorted_by_value_descending[0][1]

    def nearby_airports_within_one_degree(
            self, airport_id, airport_lat_long=False, state_country=False):
        """ Find other airports within a 1 deg.lat/long of airport_id.
        Args:
            airport_id (str):       Id of the airport as shown in airports.csv
            airport_lat_long (bool):
            state_country (bool):

        Returns:
            airport_lat_long/state_country: False/False
                                            a list of towns with airports
                                            within +- 1 deg. lat/long
                                            of airport_id.
                                            False/True
                                            a list of strings of length 2
                                            country that airport_id is in
                                            and the region e.g ['US', 'US-WA']
                                            True/False
                                            ["airport_id latitude",
                                             "airport_id longitude"]
                                            True/True
                                            (['US', 'US-WA'],
                                             '47.44900131225586',
                                              '-122.30899810791016')
        """
        # list_of_records[row][column]
        list_of_records = self.get_list_of_records_from_a_csv_file(
            'airports.csv')
        # airport id in column 2, lat, long in column 5 and 6,
        # airport name is in
        # column 4, municipality in row[10]
        # initialize airport_id_lat to determine if param is correct
        # country = row[8]
        # region = row[9]

        nearby_airports = []
        country_state = []
        for row in list_of_records:
            # data for airport_id
            if row[1] == airport_id:
                airport_id_lat = row[4]
                airport_id_long = row[5]
                country_state.append(row[8])
                country_state.append(row[9])

                nearby_airport_max_lat = float(airport_id_lat) + 1.0
                nearby_airport_min_lat = float(airport_id_lat) - 1.0
                nearby_airport_max_long = float(airport_id_long) + 1.0
                nearby_airport_min_long = float(airport_id_long) - 1.0
        try:
            if airport_id_lat is None:
                pass
        except UnboundLocalError as err:
            self.logger.error("Airport Id can not be found.\n"
                              "Make sure that"
                              "nearby_airports_within_two_degrees(airport_id)"
                              " has the correct airport_id\n", err)
            raise
        for row in list_of_records:
            if row[10] not in nearby_airports:
                if float(row[4]) <= nearby_airport_max_lat\
                        and float(row[4]) >= nearby_airport_min_lat:
                    if float(row[5]) <= nearby_airport_max_long\
                            and float(row[5]) >= nearby_airport_min_long:
                        nearby_airports.append(row[10])
        if airport_lat_long is False and state_country is False:
            self.logger.info(
                'Finished nearby_airports_within_one_degree, returning '
                'airport_lat_long')
            return nearby_airports
        if airport_lat_long is True and state_country is False:
            self.logger.info(
                'Finished nearby_airports_within_one_degree returning '
                'airport_id_lat, airport_id_long')
            return airport_id_lat, airport_id_long
        if airport_lat_long is False and state_country is True:
            self.logger.info(
                'Finished nearby_airports_within_one_degree returning '
                'country_state')
            return country_state
        if airport_lat_long is True and state_country is True:
            self.logger.info(
                'Finished nearby_airports_within_one_degree returning '
                'country_state, airport_id_lat, airport_id_long')
            return country_state, airport_id_lat, airport_id_long

    def airports_with_home_links(self):
        """ Find all of the airports that have home web pages.

        Args:
            No args

        Return:
              airport_names_homepage (dict):
                                           airport_name(str):home_web_page(str)


        """
        list_of_records = self.get_list_of_records_from_a_csv_file(
            'airports.csv')
        # list_of_records_for_airport_csv[row][15] = home_link
        # list_of_records_for_airport_csv[row][16] = wiki page
        # list_of_records_for_airport_csv[row][3] = airport name

        # dict{name:homepage}
        airport_names_homepage = {}
        for row in list_of_records:
            if row[3] != "name":
                if "http" in row[15]:
                    airport_names_homepage[row[3]] = row[15]
        self.logger.info(
            'Finished airports_with_home_links')
        return airport_names_homepage

    def airports_with_wiki_pages(self):
        """ Find all of the airports that have home web pages.

        Args:
            No args

        Return:
              airport_names_wiki (dict):
                                           airport_name(str):wiki_page(str)


        """
        list_of_records = self.get_list_of_records_from_a_csv_file(
            'airports.csv')
        # list_of_records_for_airport_csv[row][15] = home_link
        # list_of_records_for_airport_csv[row][16] = wiki page
        # list_of_records_for_airport_csv[row][3] = airport name

        # dict{name:wiki}
        airport_names_wiki = {}
        for row in list_of_records:
            if row[3] != "name":
                if "http" in row[16]:
                    airport_names_wiki[row[3]] = row[16]
        self.logger.info(
            'Finished airports_with_wiki_pages')
        return airport_names_wiki

    def open_web_page(self, url_of_web_page):
        """Open a web page in a new window

           Args:
               url_of_web_page (str):  web page url

           Return:
                 None

        """
        self.url = url_of_web_page
        # new=1 opens in a new window
        webbrowser.open(self.url, new=1)
        self.logger.info(
            'Finished open_web_page')


class countries(airports):
    """Create methods to help answer questions on
    the countries.csv file.
    """

    def __init__(self,
                 url="http://ourairports.com/data/countries.csv",
                 filename="countries.csv"):
        """ Download the file from `url` and save it locally
            under ./filename.
        Args:
            url (str): url of the csv file. Defaults to
                       "http://ourairports.com/data/countries.csv"
            filename (str): name of the file to save to in the current
                            working directory. Defaults to "countries.csv"

        Return:
              None
        """
        if 'countries' in str(type(self)):
            self.logger = logging.getLogger(
                'test_spring_quarter_final_project.Airports.countries')
            self.logger.info('Creating an instance of countries')
        self.url = url
        self.filename = filename
        super(countries, self).__init__(
            self.url,
            self.filename)

    def country_code_to_country_conversion(self, country_code):
        '''
        Retrieve the country from countries.csv, given the country code.
        countries.csv must in the current directory
        country codes to country mapped in countries.csv
        :params - country_code as displayed in the airports.csv file
        '''
        # list_of_records_for_countries_csv[row][1] =  countrycode
        # list_of_records_for_countries_csv[row][2] = country name
        list_of_records =\
            self.get_list_of_records_from_a_csv_file('countries.csv')
        for record in list_of_records:
            if country_code == record[1]:
                self.logger.info('Finished country_code_to_country_conversion')
                return record[2]


class runways(airports):
    def __init__(self, url="http://ourairports.com/data/runways.csv",
                 filename="runways.csv"):
        """ Download the file from `url` and save it locally
            under ./filename.
        Args:
            url (str): url of the csv file. Defaults to
                       "http://ourairports.com/data/runways.csv"
            filename (str): name of the file to save to in the current
                            working directory. Defaults to "runways.csv"

        Return:
              None
        """
        if 'runways' in str(type(self)):
            self.logger = logging.getLogger(
                'test_spring_quarter_final_project.Airports.runways')
            self.logger.info('Creating an instance of runways')
        self.url = url
        self.filename = filename
        super(runways, self).__init__(
            self.url,
            self.filename)

    def runway_data_from_csv_file(self, airport_id, length=False,
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

        list_of_records = self.get_list_of_records_from_a_csv_file(
            'runways.csv')
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
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_info')
            return runway_info
        if length is False and status is False and elevation is True:
            runway_elevation_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_elevation_'):
                    runway_elevation_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_elevation_dict')
            return runway_elevation_dict
        if length is False and status is True and elevation is False:
            runway_closed_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_closed_'):
                    runway_closed_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_closed_dict')
            return runway_closed_dict
        if length is False and status is True and elevation is True:
            runway_status_elevation_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_closed_')\
                        or key.startswith('runway_elevation_'):
                    runway_status_elevation_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_status_elevation_dict')
            return runway_status_elevation_dict
        if length is True and status is False and elevation is False:
            runway_length_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_length_'):
                    runway_length_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_length_dict')
            return runway_length_dict
        if length is True and status is False and elevation is True:
            runway_length_elevation_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_length_')\
                        or key.startswith('runway_elevation_'):
                    runway_length_elevation_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_length_elevation_dict')
            return runway_length_elevation_dict
        if length is True and status is True and elevation is False:
            runway_length_status_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_length_')\
                        or key.startswith('runway_closed_'):
                    runway_length_status_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_length_status_dict')
            return runway_length_status_dict
        if length is True and status is True and elevation is True:
            runway_length_status_elevation_dict = {}
            for key in list(runway_info.keys()):
                if key.startswith('runway_length_')\
                        or key.startswith('runway_closed_')\
                        or key.startswith('runway_elevation'):
                    runway_length_status_elevation_dict[key] = runway_info[key]
            self.logger.info('Finished runway_data_from_csv_file returning '
                             'runway_length_status_elevation_dict')
            return runway_length_status_elevation_dict


class navaids(airports):
    def __init__(self,
                 url="http://ourairports.com/data/navaids.csv",
                 filename="navaids.csv"):
        if 'navaids' in str(type(self)):
            self.logger = logging.getLogger(
                'test_spring_quarter_final_project.Airports.navaids')
            self.logger.info('Creating an instance of navaids')
        self.url = url
        self.filename = filename
        super(navaids, self).__init__(
            self.url,
            self.filename)

    def nav_aids_data_from_csv_file(self, country, airport_id=''):
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
        list_of_records = self.get_list_of_records_from_a_csv_file(
            'navaids.csv')
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
            self.logger.info('Finished nav_aids_data_from_csv_file returning '
                             'navaids_per_country')
            return navaids_per_country
