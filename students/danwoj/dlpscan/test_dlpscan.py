import pytest, sys, csv

from dlpscan import ip_oct_bin, sn_calculation, subnet_calculator, target_list_input

def test_subnet_calculator():
# This test verifies the subnet calculator function works
    ip_addr1 = '192.168.36.133'
    subnet_mask1 = '255.255.255.0'
    value1 = subnet_calculator(ip_addr1, subnet_mask1)

    ip_addr2 = '10.2.34.17'
    subnet_mask2 = '255.255.248.0'
    value2 = subnet_calculator(ip_addr2, subnet_mask2)

    ip_addr3 = '172.20.23.128'
    subnet_mask3 = '255.255.0.0'
    value3 = subnet_calculator(ip_addr3, subnet_mask3)

    assert value1 == '192.168.36.0/24'
    assert value2 == '10.2.32.0/21'
    assert value3 == '172.20.0.0/16'
#    assert FALSE

def test_target_list_input():
# This test verifies the programs ability to input a 
# target list from a csv file
    target_file = 'test_targets.csv'

    targets = target_list_input(target_file)
    print(targets)
    assert targets == ['192.168.36.1', '192.168.36.2', '192.168.36.3', '192.168.36.4', '192.168.36.5']