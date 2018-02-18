# test_spring_quarter_final_project
# test file for test_spring_quarter_final_project.py


import csv
from spring_quarter_final_project import download_airport_data_csv_files,\
    get_csv_files_in_current_directory, get_column_names_in_csv_file,\
    country_with_most_scheduled_service_airports
import os


def test_download_airport_data_csv_files():
    url = "http://ourairports.com/data/airports.csv"
    filename = 'airports.csv'
    download_airport_data_csv_files(url, filename)
    with open(filename, "r") as file_obj:
        result = file_obj.readline()
    assert '"longitude_deg"' in result


def test_print_out_csv_files_in_current_directory():
    result = get_csv_files_in_current_directory()
    assert 'airports.csv' in result


def test_get_column_names_in_csv_file():
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    for i in files:
        result = get_column_names_in_csv_file(i)
        assert "id" in result


def test_country_with_most_scheduled_service_airports():
    result = country_with_most_scheduled_service_airports()
    with open('airports.csv', 'r', newline='') as fopen:
        csv_reader_obj = csv.reader(fopen)
        list_of_records = [record for record in csv_reader_obj]
    list_of_countries = [list_of_records[i][8]
                         for i in range(len(list_of_records))]
    assert result in list_of_countries
