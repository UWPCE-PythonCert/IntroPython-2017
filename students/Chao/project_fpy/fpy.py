#!/usr/bin/env python

"""
Project Fpy
=================
Po-Sung (Sean) Chao

The purpose of this Python program is to build a maintenance tool with F5 Python SDK

Package required: F5 Python SDK
$ pip install f5-sdk
=================
"""

from f5.bigip import ManagementRoot
from f5.utils.responses.handlers import Stats
from icontrol.exceptions import iControlUnexpectedHTTPError
from requests.exceptions import ConnectionError
import getpass
import ipaddress

class LTM:
    """ Main Class for Local Traffic Manager Module """
    def __init__(self, mgmt):
        self.mgmt = mgmt

class Pool(LTM):
    """ Pool class for retrieving pool status """

    def get_pool_state(self, p_name, p_partition='Common'):
        """ Function to retrieve current pool availability status """
        pool_stat = self.mgmt.tm.ltm.pools.pool.load(name=p_name, partition=p_partition)
        stats = Stats(pool_stat.stats.load())
        return stats.stat.status_availabilityState['description']

    def get_pool(self):
        """ Pool full status function """
        pools = self.mgmt.tm.ltm.pools.get_collection()
        print("\n==================== Pool Status ========================")
        print("|       Pool Name      |    Partition    | Availability |")
        for pool in pools:
            pstat = self.get_pool_state(pool.name, pool.partition)
            print("| {:20} | {:15} | {:12} |".format(pool.name, pool.partition, pstat))
        print("=========================================================")

class Virtual(LTM):
    """ Virtual class for retrieving virtual server status or modifying config """

    def get_virtual_state(self, v_name, v_partition='Common'):
        """ Function to retrieve current virtual server availability status """
        virtual_stat = self.mgmt.tm.ltm.virtuals.virtual.load(name=v_name, partition=v_partition)
        stats = Stats(virtual_stat.stats.load())
        return stats.stat.status_availabilityState['description']

    def get_virtual(self):
        """ Virtual Server full status function """
        virtuals = self.mgmt.tm.ltm.virtuals.get_collection()
        print("\n=================== Virtual Status ======================")
        print("|  Virtual Server Name |    Partition    | Availability |")
        for virtual in virtuals:
            vstat = self.get_virtual_state(virtual.name, virtual.partition)
            print("| {:20} | {:15} | {:12} |".format(virtual.name, virtual.partition, vstat))
        print("=========================================================")

    def apply_rule(self, myrule='fpy_maintenace'):
        """ iRule apply function """
        virtuals = self.mgmt.tm.ltm.virtuals.get_collection()
        for virtual in virtuals:
            # set full iRule path
            rule_path = '/{}/{}'.format(virtual.partition, myrule)
            vrule = self.mgmt.tm.ltm.virtuals.virtual.load(name=virtual.name, partition=virtual.partition)
            try:
                if rule_path in vrule.rules:
                    print("Rule {} already exists in {}".format(myrule, virtual.name))
                else:
                    # Insert iRule at the front of the list
                    vrule.rules.insert(0, rule_path)
                    vrule.update()
                    print("Rule {} added to {}".format(myrule, virtual.name))
            except iControlUnexpectedHTTPError:
                print("Unable to apply rule {} to {}. HTTP profile required.".format(myrule, virtual.name))

    def remove_rule(self, myrule='fpy_maintenace'):
        """ iRule removal function """
        virtuals = self.mgmt.tm.ltm.virtuals.get_collection()
        for virtual in virtuals:
            rule_path = '/{}/{}'.format(virtual.partition, myrule)
            vrule = self.mgmt.tm.ltm.virtuals.virtual.load(name=virtual.name, partition=virtual.partition)
            if rule_path in vrule.rules:
                vrule.rules.remove(rule_path)
                vrule.update()
                print("Rule {} removed from {}".format(myrule, virtual.name))
            else:
                print("Rule {} does not exist in {}".format(myrule, virtual.name))

class Rule(LTM):
    """ Rule class for iRule functions """

    def get_rule(self):
        """ Function for retireving iRule list  """
        rules = self.mgmt.tm.ltm.rules.get_collection()
        print("\n======================== iRule List ======================")
        print("|                iRule Name                |  Partition  |")
        for rule in rules:
            print("| {:40} | {:11} |".format(rule.name, rule.partition))
        print("==========================================================")

    def create_rule(self, myrule='fpy_maintenace'):
        """ Create a maintenance iRule """
        if self.mgmt.tm.ltm.rules.rule.exists(name=myrule, partition='Common'):
            result = input("\nExisting iRule {}. Do you want to overwrite? ('y' or 'yes'): ".format(myrule))
            if result == 'y' or result == 'yes':
                # Modify the iRule
                mrule = self.mgmt.tm.ltm.rules.rule.load(name=myrule, partition='Common')
                mrule.modify(apiAnonymous="when HTTP_REQUEST {\nHTTP::respond 200 content {\n<!DOCTYPE html>\n<title>Site under Maintenance</title>\n}\n}")
                print("\niRule {} modified.".format(myrule))
            else:
                print("\nNo iRule modification was made.")
        else:
            # Create new iRule
            mrule = self.mgmt.tm.ltm.rules.rule.create(name=myrule, partition='Common', apiAnonymous="when HTTP_REQUEST {\nHTTP::respond 200 content {\n<!DOCTYPE html>\n<title>Site under Maintenance</title>\n}\n}")
            print("\niRule {} created.".format(myrule))

    def check_rule(self, myrule, mypar='Common'):
        """ Simple function to check if certain iRule already exists """
        return self.mgmt.tm.ltm.rules.rule.exists(name=myrule, partition=mypar)


def display(mgmt):
    """ Submenu for display menu """
    while True:
        print("\n================ Display Menu =================")
        print("*            (1) Pool Status                  *")
        print("*            (2) Virtual Server Status        *")
        print("*            (3) iRule List                   *")
        print("*            (q) Retuen to Main Menu          *")
        print("===============================================")

        result = input("Please select a menu item: ")

        if result == '1':
            p = Pool(mgmt)
            p.get_pool()
        elif result == '2':
            v = Virtual(mgmt)
            v.get_virtual()
        elif result == '3':
            r = Rule(mgmt)
            r.get_rule()
        elif result == 'q':
            break
        else:
            print("\n*** Selected item not in the menu. Please try again. ***")

def maintenance(mgmt):
    """ Submenu for maintenance menu """
    while True:
        print("\n================= Maintenance Menu ===================")
        print("*     (1) Create Maintenance iRule                   *")
        print("*     (2) Apply Maintenance iRule to All VIPs        *")
        print("*     (3) Remove Maintenance iRule from All VIPs     *")
        print("*     (q) Retuen to Main Menu                        *")
        print("======================================================")

        result = input("Please select a menu item: ")

        if result == '1':
            r = Rule(mgmt)
            rule_name = input("Please enter iRule name (optioanl): ")
            if rule_name:
                r.create_rule(rule_name)
            else:
                r.create_rule()
        elif result == '2':
            v = Virtual(mgmt)
            r = Rule(mgmt)
            rule_name = input("Please enter iRule you want to apply (default=fpy_maintenace): ")
            if rule_name:
                if r.check_rule(rule_name):
                    # Call apply_rule function only when it exists
                    v.apply_rule(rule_name)
                else:
                    print("iRule {} does not exist.".format(rule_name))
            else:
                v.apply_rule()
        elif result == '3':
            v = Virtual(mgmt)
            r = Rule(mgmt)
            rule_name = input("Please enter iRule you want to remove (default=fpy_maintenace): ")
            if rule_name:
                if r.check_rule(rule_name):
                    v.remove_rule(rule_name)
                else:
                    print("iRule {} does not exist.".format(rule_name))
            else:
                v.remove_rule()
        elif result == 'q':
            break
        else:
            print("\n*** Selected item not in the menu. Please try again. ***")


def login():
    """ Login handling function """

    ip = input("Please enter the IP address of the Big-IP system: ")
    try:
        # Make sure the user uses current ip format
        ipaddress.ip_address(ip)
    except ValueError:
        print("\nWrong IP format. Please enter a valid IP address.")
        quit()

    user = input("Username: ")
    # Hide user password
    pw = getpass.getpass("Password: ")
    try:
        # Return the Managemen object
        return ManagementRoot(ip, user, pw)
    except iControlUnexpectedHTTPError:
        print("\nInvalid login, please verify your credential and try again.")
        quit()
    except ConnectionError:
        print("\nUnable to connect to " + ip)
        quit()

def main_loop():
    """ Main menu to call submenu """

    # Call login functions
    mgmt = login()
    print("\nLogged in successful, Big-IP version: " + mgmt.tmos_version)

    menu_dict = {'1': display, '2': maintenance, 'q': quit}

    while True:
        print("\n===================== Fpy Main Menu ======================")
        print("*            (1) Display Current Objects                 *")
        print("*            (2) Maintenance Menu                        *")
        print("*            (q) Quit                                    *")
        print("==========================================================")
        result = input("Please select a menu item: ")
        if result == 'q':
            menu_dict[result]()
        else:
            try:
                menu_dict[result](mgmt)
            except KeyError:
                print("\n*** Selected item not in the menu. Please try again. ***")

if __name__ == '__main__':
    """ Main function """
    main_loop()
