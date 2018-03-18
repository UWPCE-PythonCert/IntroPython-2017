
import sqlite3
from sqlite3 import Error


class Node:

    def __init__(self, node_id, site_id='', management_ip='', console_id='', vendor_id='', platform_id='', os_id=''):
        self.node_id = node_id
        self.site_id = site_id
        self.management_ip = management_ip
        self.console_id = console_id
        self.vendor_id = vendor_id
        self.platform_id = platform_id
        self.os_id = os_id


    @property
    def description(self):
        return ("""Node: {}
Site: {}
Management IP: {}
Console: {}
Vendor: {}
Platform: {}
SW Version: {}""".format(self.node_id, self.site_id, self.management_ip,
                      self.console_id, self.vendor_id, self.platform_id,
                      self.os_id))


class NodeStorage:
    """
    To test in database in memory use ':memory:'
    To use database use 'test.db'

    """

    def __init__(self, database='test.db'): 
        self.db = database
        self.conn = sqlite3.connect(self.db)
        self.create_table()


    def create_connection(self):
        try:
            conn = sqlite3.connect(self.db)
            return conn
        except Error as e:
            print(e)

        return None


    def create_table(self):
        with self.conn:
            # import pdb;pdb.set_trace()
            c = self.conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS node_db (
                            node_id text, 
                            site_id text, 
                            management_ip text, 
                            console_id text, 
                            vendor_id text, 
                            platform_id text, 
                            os_id text
                            );""")


    def add_node(self, node_info):
        """
        node_info is an object of Node() class

        """
        # node_info = Node(node_id, site_id, management_ip, console_id, vendor_id, platform_id, os_id)
        # print(node_info.description())
        with self.conn:
            c = self.conn.cursor()
            c.execute("INSERT INTO node_db VALUES (:node_id, :site_id, :management_ip, :console_id,"
                      " :vendor_id, :platform_id, :os_id)",
                      {'node_id': node_info.node_id, 'site_id': node_info.site_id, 'management_ip': node_info.management_ip,
                       'console_id': node_info.console_id, 'vendor_id': node_info.vendor_id, 'platform_id': node_info.platform_id,
                       'os_id': node_info.os_id})


    def remove_node(self, node_id):
        with self.conn:
            c = self.conn.cursor()
            c.execute("DELETE FROM node_db WHERE node_id = :node_id", {'node_id': node_id})
            return node_id


    def find_node(self, node_id):
        with self.conn:
            c = self.conn.cursor()
            c.execute("SELECT * FROM node_db WHERE node_id = :node_id", {'node_id': node_id})
            node = c.fetchone()

        if node:
            return Node(*node)
        else:
            return None


    def generate_report(self):
        with self.conn:
            c = self.conn.cursor()
            c.execute("SELECT * FROM node_db")
            all_devices = c.fetchall()

            print("\n\n"
                  "--------------------------------------------------------------------\n"
                  "Node name | Site | Management Ip | Vendor  | Platform | OS version \n"
                  "--------------------------------------------------------------------")
            for node in all_devices:
                # print(donor)
                node_id = node[0]
                site_id = node[1]
                management_ip = node[2]
                vendor_id = node[3]
                platform_id = node[4]
                os_id = node[5]

                print("{:12}{:7}{:16}{:10}{:11}{:11}".format(node_id, site_id, management_ip, vendor_id, platform_id, os_id))
            
            print("--------------------------------------------------------------------\n")
            print("Total Devices: {}".format(len(all_devices)))
            print("\n\n\n\n")




