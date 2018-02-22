# test_spring_quarter_final_project
# test file for test_spring_quarter_final_project.py


import csv
from spring_quarter_final_project import download_airport_data_csv_files,\
    get_csv_files_in_current_directory, get_column_names_in_csv_file,\
    get_list_of_records_from_a_csv_file,\
    number_of_scheduled_or_nonscheduled_service_airports_per_country,\
    country_with_the_most_scheduled_nonscheduled_service
import os


# def test_download_airport_data_csv_files():
#     url = "http://ourairports.com/data/airports.csv"
#     filename = './airports.csv'
#     download_airport_data_csv_files([(url, filename)])
#     with open(filename, "r") as file_obj:
#         result = file_obj.readline()
#     assert '"longitude_deg"' in result


# def test_get_csv_files_in_current_directory():
#     result = get_csv_files_in_current_directory()
#     assert 'airports.csv' in result


# def test_get_column_names_in_csv_file():
#     files = [f for f in os.listdir('.') if f.endswith('.csv')]
#     for i in files:
#         result = get_column_names_in_csv_file(i)
#         assert "id" in result


# def test_get_list_of_records_from_a_csv_file():
#     results = get_list_of_records_from_a_csv_file('airports.csv')
#     assert results[3082][9] == 'US-GA'


def test_number_of_scheduled_service_airports_per_country_true():
    result = number_of_scheduled_or_nonscheduled_service_airports_per_country(True)
    print(result)
    assert False
    # assert 'CF'in result


# def test_number_of_scheduled_service_airports_per_country_false():
#     result = number_of_scheduled_or_nonscheduled_service_airports_per_country(False)
#     assert 'US' in result


# def test_country_with_the_most_scheduled_nonscheduled_service_most():
#     result = country_with_the_most_scheduled_nonscheduled_service(True)
#     print(result)
#     assert False
#     # assert result == 'CN'


# def test_country_with_the_most_scheduled_nonscheduled_service_least():
#     result = country_with_the_most_scheduled_nonscheduled_service(False)
#     print(result)
#     assert False
#     # assert result == 'JP'
