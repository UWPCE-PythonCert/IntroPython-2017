# test_spring_quarter_final_project
# test file for test_spring_quarter_final_project.py


from spring_quarter_final_project import download_airport_data_csv_files,\
    get_csv_files_in_current_directory, get_column_names_in_csv_file,\
    get_list_of_records_from_a_csv_file,\
    number_of_scheduled_or_nonscheduled_service_airports_per_country,\
    country_with_the_most_scheduled_nonscheduled_service,\
    country_code_to_country_conversion,\
    nearby_airports_within_one_degree,\
    airports_with_home_links,\
    airports_with_wiki_pages,\
    runway_data_from_csv_file,\
    nav_aids_data_from_csv_file
import os
import pytest


def test_download_airport_data_csv_files():
    url = "http://ourairports.com/data/airports.csv"
    filename = './airports.csv'
    download_airport_data_csv_files([(url, filename)])
    with open(filename, "r") as file_obj:
        result = file_obj.readline()
    assert '"longitude_deg"' in result


def test_get_csv_files_in_current_directory():
    result = get_csv_files_in_current_directory()
    assert 'airports.csv' in result


def test_get_column_names_in_csv_file():
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    for i in files:
        result = get_column_names_in_csv_file(i)
        assert "id" in result


def test_get_list_of_records_from_a_csv_file():
    results = get_list_of_records_from_a_csv_file('airports.csv')
    assert results[3082][9] == 'US-GA'


def test_number_of_scheduled_service_airports_per_country_true():
    result = number_of_scheduled_or_nonscheduled_service_airports_per_country(True)
    assert result['PH'] == 50


def test_number_of_scheduled_service_airports_per_country_false():
    result = number_of_scheduled_or_nonscheduled_service_airports_per_country(False)
    assert result['PH'] == 229


def test_country_with_the_most_scheduled_nonscheduled_service_most():
    result = country_with_the_most_scheduled_nonscheduled_service(True)
    assert result == ('United States', 479)
    # assert False


def test_country_with_the_most_scheduled_nonscheduled_service_least():
    result = country_with_the_most_scheduled_nonscheduled_service(False)
    assert result == ('United States', 21910)


def test_country_code_to_country_conversion():
    result = country_code_to_country_conversion('US')
    assert result == 'United States'


def test_nearby_airports_within_one_degree_with_invalid_param():
    with pytest.raises(UnboundLocalError):
        nearby_airports_within_one_degree("")


def test_nearby_airports_within_one_degree():
    result = nearby_airports_within_one_degree("KSEA")
    assert 'Olympia' in result


def test_nearby_airports_within_one_degree_state_country():
    result = nearby_airports_within_one_degree("KSEA", airport_lat_long=False, state_country=True)
    # print(result)
    assert len(result) == 2


def test_nearby_airports_within_one_degree_lat_long():
    result = nearby_airports_within_one_degree("KSEA", airport_lat_long=True, state_country=False)
    print(result)
    # assert False
    lat_long = float(result[0]) + float(result[1])
    assert type(lat_long) == float


def test_nearby_airports_within_one_degree_state_country_lat_long():
    result = nearby_airports_within_one_degree("KSEA", airport_lat_long=True, state_country=True)
    # print(result)
    # assert False
    assert type(result[0]) == list
    assert type(result[1]) == str
    assert type(result[2]) == str


def test_airports_with_home_links():
    result = airports_with_home_links()
    home_link_list = list(result.values())
    http_in_item = False
    for item in home_link_list:
        if 'http' in item:
            http_in_item = True
    assert http_in_item is True


def test_airports_with_wiki_pages():
    result = airports_with_wiki_pages()
    wiki_list = list(result.values())
    # account for some of the data being in the incorrect column
    wiki_in_list = False
    for item in wiki_list:
        if 'wiki' in item:
            wiki_in_list = True
    assert wiki_in_list is True


def test_runway_data_from_csv_file_default_params():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA")
    assert len(result) == 24
    assert type(result) == dict


def test_runway_data_from_csv_file_elevation_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", elevation=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_status_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", status=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_status_elevation_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", status=True, elevation=True)
    print(result)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", length=True)
    assert len(result) == 4
    assert type(result) == dict


def test_runway_data_from_csv_file_length_elevation_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", length=True, elevation=True)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_status_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", length=True, status=True)
    assert len(result) == 8
    assert type(result) == dict


def test_runway_data_from_csv_file_length_status_elevation_true():
    url = "http://ourairports.com/data/runways.csv"
    filename = './runways.csv'
    download_airport_data_csv_files([(url, filename)])
    result = runway_data_from_csv_file("KSEA", length=True,
                                       status=True, elevation=True)
    assert len(result) == 12
    assert type(result) == dict


def test_nav_aids_data_from_csv_file_by_country():
    url = "http://ourairports.com/data/navaids.csv"
    filename = 'navaids.csv'
    download_airport_data_csv_files([(url, filename)])
    result = nav_aids_data_from_csv_file("US")
    assert type(result) == dict
    assert "US" in result.keys()


def test_nav_aids_data_from_csv_file_by_airport_id():
    url = "http://ourairports.com/data/navaids.csv"
    filename = 'navaids.csv'
    download_airport_data_csv_files([(url, filename)])
    result = nav_aids_data_from_csv_file("US", airport_id="KSEA")
    print(result)
    assert False
