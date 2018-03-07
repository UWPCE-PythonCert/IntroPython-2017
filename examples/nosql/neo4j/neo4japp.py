#!/usr/bin/env python

"""
Simple neo4j app

To illustrate relationships

This requires the neo4j-driver package::

  pip install neo4j-driver

This assumes that you have a configuration file in a dir relative to this one:

.config/config

With the follwoing configuration in it:

[configuration]

neo4juser = your_graphenedb_username
neo4jpw = your_graphenedb_password

"""
from pathlib import Path
import logging
from configparser import ConfigParser
from neo4j.v1 import GraphDatabase, basic_auth

# Turning on logging lets you see what neo4j is doing
# but it's pretty noisy!
# logging.basicConfig(level=logging.INFO)

print('Simple app to illustrate Neo4j and relationships')

# get the config file
CONFIG = Path(__file__).parent / ".config/config"


def setup_db():
    """
    sets up the connection to the neo4j DB

    configuration (username and password) is read from a config file in
    a .config dir in the dir specified in CONFIG
    """

    config = ConfigParser()
    config.read(CONFIG)

    graphenedb_user = config["configuration"]["neo4juser"]
    graphenedb_pass = config["configuration"]["neo4jpw"]
    # graphenedb_url = 'bolt://hobby-opmhmhgpkdehgbkejbochpal.dbs.graphenedb.com:24786'
    graphenedb_url = 'bolt://hobby-khhgnhgpkdehgbkeoldljpal.dbs.graphenedb.com:24786'

    driver = GraphDatabase.driver(graphenedb_url,
                                  auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver


def clear_all(driver):
    """
    This clears the entire database, so we can start over

    NOTE: The Docs say about this:

    "This query isn’t for deleting large amounts of data, but is nice
    when playing around with small example data sets."

    I suppose if you have a really big datbase, you should just throw
    it away and make a new one.
    """
    print("Running clear_all")

    with driver.session() as session:
        print("Before clearing: all the records")
        result = session.run("MATCH (n) RETURN n")
        msg = ("There are these records:" +
               "\n".join([str(rec) for rec in result]))
        session.run("MATCH (n) DETACH DELETE n")


def test1(driver):
    """
    Create some relations
    """
    with driver.session() as session:
        print('Here we add a Person who has the name Bob. Note: care with quotes!')

        # The stuff in quotes is the Cypher query language
        session.run("CREATE (n:Person {name:'Bob'})")

        print('Now lets see if we can find Bob')

        result = session.run("MATCH (n:Person) RETURN n.name AS name")

        print('And print what we find')

        for record in result:
            print(record["name"])

        print(dir(record))

        print('Note - this needs some exception handling!')


def test2(driver):
    """
    Add a few people, some with a little more info
    """
    with driver.session() as session:

        print('Adding a couple Person nodes')
        session.run("CREATE (n:Person {first_name:'Bob', last_name: 'Jones'})")
        session.run("CREATE (n:Person {first_name:'Nancy', last_name: 'Cooper'})")

        # find all the Person nodes:
        print('finding all Person node')
        result = session.run("MATCH (n:Person) RETURN n")

        # result is an iterable of records
        # you can look at a record without "consuming" it.
        rec = result.peek()

        # a record is one or more nodes,
        # in an ordered mapping, you can get it by name or index:
        print(rec[0])
        print(rec['n']) # the n from the query above
        node = rec[0]

        # each node as a unique id:
        print('each node as a unique id')
        print(node.id)

        # A node is dict-like with the properties stored:
        print('and you can access its properties')
        print("the first person is:")
        print(node['first_name'], node['last_name'])

        # iterating through all the Person nodes:
        print('Looping through all the Person nodes')
        for rec in result:
            # each record object
            node = rec[0]
            print(node['first_name'], node['last_name'])


def test3(driver):
    """
    Add a few people, some with a little more info
    """
    with driver.session() as session:

        print('Adding a few Person nodes')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes')
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (first, last)
            session.run(cyph)

        print('Create a relationship')
        # Bob Jones likes Alice Cooper

        result = session.run("MATCH (person1:Person {first_name:'Bob', last_name:'Jones'}) "
                             "CREATE (person1)-[like:LIKE]->(person2:Person {first_name:'Alice', last_name:'Cooper'}) "
                             "RETURN like"
                             )
        print('This returns a Relationship object')
        rel = result.peek()[0]
        print("relationship:", rel)
        print("relationship's type:", rel.type)
        print("it connects nodes:", rel.start, "and", rel.end)
            # for name, node in rec.items():
            #     print("got node:", name)
            #     print(type(node))
            #     print(node['first_name'], node['last_name'])

        print("can we find Bob's friend?")
        result = session.run("MATCH (bob {first_name:'Bob', last_name:'Jones'})"
                             "-[:LIKE]->(bobFriends)"
                             "RETURN bobFriends")
        print("Bob's friends are:")
        for rec in result:
            for f in rec.values():
                print(f['first_name'], f['last_name'])


def test4(driver):
    """
    Add a few people, some with a little more info
    """
    with driver.session() as session:

        print('Adding a few Person nodes')
        for first, last in [('Bob', 'Jones'),
                            ('Nancy', 'Cooper'),
                            ('Alice', 'Cooper'),
                            ('Fred', 'Barnes'),
                            ('Mary', 'Evans'),
                            ('Marie', 'Curie'),
                            ]:
            cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (first, last)
            session.run(cyph)

        print("\nHere are all of people in the DB now:")
        cyph = """MATCH (p:Person)
                  RETURN p.first_name as first_name, p.last_name as last_name
                """
        result = session.run(cyph)
        for record in result:
            print(record['first_name'], record['last_name'])

        print('\nCreate some relationships')
        # Bob Jones likes Alice Cooper, Fred Barnes and Marie Curie

        for first, last in [("Alice", "Cooper"),
                            ("Fred", "Barnes"),
                            ("Marie", "Curie")]:
            cypher = """
              MATCH (p1:Person {first_name:'Bob', last_name:'Jones'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            session.run(cypher)

        print("Can we find all of Bob's friends?")
        cyph = """
          MATCH (bob {first_name:'Bob', last_name:'Jones'})
                -[:FRIEND]->(bobFriends)
          RETURN bobFriends
          """
        result = session.run(cyph)
        print("Bob's friends are:")
        for rec in result:
            for f in rec.values():
                print(f['first_name'], f['last_name'])

        print("\nSetting up Marie's friends")

        for first, last in [("Mary", "Evans"),
                            ("Alice", "Cooper"),
                            ('Fred', 'Barnes'),
                            ]:
            cypher = """
              MATCH (p1:Person {first_name:'Marie', last_name:'Curie'})
              CREATE (p1)-[friend:FRIEND]->(p2:Person {first_name:'%s', last_name:'%s'})
              RETURN p1
            """ % (first, last)
            # print(cypher)
            session.run(cypher)

        print("Can we find all of Marie's friends?")
        cyph = """
          MATCH (marie {first_name:'Marie', last_name:'Curie'})
                -[:FRIEND]->(friends)
          RETURN friends
          """
        result = session.run(cyph)
        print("Marie's friends are:")
        for rec in result:
            for f in rec.values():
                print(f['first_name'], f['last_name'])


if __name__ == '__main__':
    driver = setup_db()
    clear_all(driver)
    # test1(driver)
    # test2(driver)
    # test3(driver)
    test4(driver)




