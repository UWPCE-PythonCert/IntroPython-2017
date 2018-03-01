import os
import urllib.request
import csv


class airports():
    """ This is the base class """

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
        self.url = url
        self.filename = filename
        if not os.path.isfile(self.filename):
            with urllib.request.urlopen(self.url):
                with open(self.filename, 'w'):
                    urllib.request.urlretrieve(self.url, self.filename)

    def get_column_names_in_csv_file(self, filename="airports.csv"):
        """ Return the column names from the airport.csv file.
        Args:
            filename (str): name of the csv file. Defaults to "airports.csv"

        Return:
              line (str):  column names in csv file
        """
        self.filename = filename
        with open(self.filename, "r") as file_obj:
            line = file_obj.readline()
        columns = line.split(',')
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
        with open(filename, 'r') as file_obj:
            csv_reader_obj = csv.reader(file_obj)
            # skip the first line of the file, which lists the column names
            list_of_records = [
                record for record in csv_reader_obj if record[0] != 'id']
        return list_of_records

    def number_of_scheduled_or_nonscheduled_service_airports_per_country(
            self, scheduled_or_not_scheduled):
        """ Create a dictionary {country:xxxx} where xxxx is the number of
        airports with scheduled service or without scheduled service
        airports.csv must be in the current directory.

        Args:
            scheduled_or_not_scheduled (bool):  True return number of scheduled
                                                service airports per country
                                                False return number of airports
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
        return number_of_airports_with_service_or_no_service_per_country
