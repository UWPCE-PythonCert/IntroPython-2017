# test_spring_quarter_final_project
# test file for test_spring_quarter_final_project.py


import os
import logging
import pytest
from spring_quarter_final_project import \
    get_csv_files_in_current_directory
from Airports import airports, countries, runways,\
    navaids

logger = logging.getLogger('test_spring_quarter_final_project')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('test_spring_quarter_final_project.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


@pytest.fixture
def remove_csv_files():
    """Remove all csv data files that the script uses at the start
       of the test
    """
    filenames = ["airports.csv", "runways.csv", "navaids.csv",
                 "countries.csv", "regions.csv"]
    for file in filenames:
        if os.path.isfile(file):
            os.remove(file)


def test_download_airport_data_csv_files(remove_csv_files):
    """ Test that the object will download the correct file."""
    airports()
    with open("airports.csv", 'r') as fopen:
        line = fopen.readline()
        assert 'municipality' in line


def test_get_csv_files_in_current_directory():
    result = get_csv_files_in_current_directory()
    assert 'airports.csv' in result


def test_get_column_names_in_csv_file():
    column_names_obj = airports()
    result = column_names_obj.get_column_names_in_csv_file()
    assert len(result) == 18


def test_get_list_of_records_from_a_csv_file():
    airport_obj = airports()
    results = airport_obj.get_list_of_records_from_a_csv_file('airports.csv')
    assert results[3082][9] == 'US-GA'


def test_get_list_of_records_from_a_csv_file_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        airport_obj = airports()
        remove_csv_files()
        airport_obj.get_list_of_records_from_a_csv_file('airports.csv')


def test_number_of_scheduled_service_airports_per_country_true():
    airport_obj = airports()
    result =\
        airport_obj\
        .number_of_scheduled_or_nonscheduled_service_airports_per_country(
            True)
    assert result['PH'] == 50


def test_number_of_scheduled_service_airports_per_country_false():
    airport_obj = airports()
    result =\
        airport_obj\
        .number_of_scheduled_or_nonscheduled_service_airports_per_country(
            False)
    assert result['PH'] == 229


def test_country_with_the_most_scheduled_nonscheduled_service_most():
    airport_obj = airports()
    result = airport_obj.country_with_the_most_scheduled_nonscheduled_service()
    assert result == ('United States', 479)
    # assert False


def test_country_with_the_most_scheduled_nonscheduled_service_least():
    airport_obj = airports()
    result = airport_obj.country_with_the_most_scheduled_nonscheduled_service(
        False)
    assert result == ('United States', 21919)


def test_country_code_to_country_conversion():
    airport_obj = countries()
    result = airport_obj.country_code_to_country_conversion('US')
    assert result == 'United States'


def test_nearby_airports_within_one_degree_with_invalid_param():
    with pytest.raises(UnboundLocalError):
        airport_obj = airports()
        airport_obj.nearby_airports_within_one_degree("")


def test_nearby_airports_within_one_degree():
    airport_obj = airports()
    result = airport_obj.nearby_airports_within_one_degree("KSEA")
    assert 'Olympia' in result


def test_nearby_airports_within_one_degree_state_country():
    airport_obj = airports()
    result = airport_obj.nearby_airports_within_one_degree(
        "KSEA", airport_lat_long=False, state_country=True)
    assert len(result) == 2


def test_nearby_airports_within_one_degree_lat_long():
    airport_obj = airports()
    result = airport_obj.nearby_airports_within_one_degree(
        "KSEA", airport_lat_long=True, state_country=False)
    lat_long = float(result[0]) + float(result[1])
    assert type(lat_long) == float


def test_nearby_airports_within_one_degree_state_country_lat_long():
    airport_obj = airports()
    result = airport_obj.nearby_airports_within_one_degree("KSEA",
                                                           airport_lat_long=True,
                                                           state_country=True)
    assert type(result[0]) == list
    assert type(result[1]) == str
    assert type(result[2]) == str


def test_airports_with_home_links():
    airport_obj = airports()
    result = airport_obj.airports_with_home_links()
    assert type(result) == dict
    home_link_list = list(result.values())
    http_in_item = False
    for item in home_link_list:
        if 'http' in item:
            http_in_item = True
    assert http_in_item is True


def test_airports_with_wiki_pages():
    airport_obj = airports()
    result = airport_obj.airports_with_wiki_pages()
    assert type(result) == dict
    wiki_list = list(result.values())
    # account for some of the data being in the incorrect column
    wiki_in_list = False
    for item in wiki_list:
        if 'wiki' in item:
            wiki_in_list = True
    assert wiki_in_list is True


def test_runway_data_from_csv_file_default_params():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA")
    assert len(result) == 24
    assert type(result) == dict


def test_runway_data_from_csv_file_elevation_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA", elevation=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_length_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA", length=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_status_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA", status=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_status_elevation_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA",
                                                  status=True, elevation=True)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_elevation_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA",
                                                  length=True, elevation=True)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_status_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA",
                                                  length=True, status=True)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_status_elevation_true():
    runway_obj = runways()
    result = runway_obj.runway_data_from_csv_file("KSEA",
                                                  length=True, status=True,
                                                  elevation=True)
    assert len(result) == 12
    assert type(result) == dict


def test_nav_aids_data_from_csv_file_by_country():
    navaid_obj = navaids()
    result = navaid_obj.nav_aids_data_from_csv_file("US")
    assert type(result) == dict
    assert len(result) == 1
    assert "US" in result.keys()


def test_nav_aids_data_from_csv_file_by_airport_id():
    navaid_obj = navaids()
    result = navaid_obj.nav_aids_data_from_csv_file("US", airport_id="KSEA")
    assert type(result) == dict
    assert "KSEA" in result.keys()
    assert len(result) == 1


# def test_logging_config():
#     airport_obj = airports()
#     logger.info('Created')
