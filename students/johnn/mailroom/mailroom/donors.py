#!/usr/bin/env python3

""" Program to manage donations. """

import sys
import datetime
import uuid
import pickle
import os
from mailroom import security
from mailroom.audit import audit_log
import json_save.json_save_meta as js


class Donors(js.JsonSaveable):

    """
    Class that stores donor records

    Optionally provide a Donor() object or add Donor() object
    with add_donor().

    Iterable, and provides an index for searching as well as
    a match(search) utility function.

    get_donor can be used to return a Donor() object given the
    donor did.
    """

    _donors = js.Dict()
    audit = js.List()

    def __init__(self, donor=None):

        self.__name__ = "Donors"

        self._donors = {}
        # TODO:
        #   donors should take a donor object or multiple donor objects
        if donor:
            self.add_donor(donor)

    def __repr__(self):
        repr_out = []
        for key in self._donors:
            repr_out.append(repr(self._donors[key]))
        return "Donors( " + ", ".join(repr_out) + " )"

    def __str__(self):
        str_out = []
        for key in self._donors:
            str_out.append(str(self._donors[key]))
        return "str(Donors(\n  " + ",\n  ".join(str_out) + " ))"

    def __iter__(self):
        return iter(self.full_name_index)

    @audit_log
    def add_donor(self, donor):
        """
        add a donor to the donors database

        The add_donor method leverages the donor did which allows
        you to update or add a record using the same method.
        """
        self._donors[donor.did] = donor

    @property
    def number_donors(self):
        """ return the number of donor records """
        return len(self._donors)

    def get_donor(self, did):
        """ given a donor did, return the donor object """
        return self._donors[did]

    @property
    def full_name_index(self):
        """ Provide an index of keys, full_name, last_name and first_name """
        index = []
        for key in self._donors:
            index.append((self._donors[key].full_name, key,
                          self._donors[key].last_name,
                          self._donors[key].first_name))
        return sorted(index)

    def match_donor(self, query_full_name):
        """
        find all records that match the query string

        return tupple with full_name, did

        """
        matches = []
        for name, did, _, _ in self.full_name_index:
            if query_full_name.strip().lower() == name.lower():
                matches.append((name, did))
        return matches


class Donor(js.JsonSaveable):

    """
    Class to store a donor record

    Args:
        full_name(str)      format: <first name> [<middle_name>] <last_name>
                                    [,<suffix>]
            or
        first_name(str)
        middle_name(str)
        last_name(str)
        suffix(str)

        donation(float)     amount of today's donation
            or
        donations(list)     list of dicts containing donations

        Not typically specified
        -----------------------
        did(str)            string representation of a record UUID
        created(str)        string representation of an utcnow isoformat
                            timestamp with "Z" appended

    Usage:

        The class allows flexibility in how a record is set.  It is allowable
        to create an empty instance of the class and update it piecemeal.

        It is also allowable to pass in all information needed to create a
        record using different strategies such as a full_name vs the
        constituent parts.

        In general, record manipulation is simply the name and donation.
        However, it is also allowable to set information that is normally
        auto-created such as the did, time created and entire donation list.
        This allows a record to be created from its repr which may have
        practical uses in record backup/recreation as needed.

    Example Use Cases:

        # empty donor record
        In [599]: d=Donor()
        In [600]: repr(d)
        Out[600]: "Donor(did='97d744de-de23-11e7-bee5-0800274b0a84',
            created='2017-12-11T03:30:11.077937Z' )"
        In [601]:

        # automatic parsing of full_name
        In [601]: d=Donor(full_name="sally q smith, iv")
        In [602]: repr(d)
        Out[602]: "Donor(did='067f51c4-de24-11e7-bee5-0800274b0a84',
                         first_name='Sally', middle_name='Q',
                         last_name='Smith', suffix='IV',
                         created='2017-12-11T03:33:16.728654Z' )"
        In [603]:

        # name creation based name sub-components
        In [594]: d=Donor(first_name="joe", last_name="smith", donation=100)
        In [595]: repr(d)
        Out[595]: "Donor(did='7724e750-de23-11e7-bee5-0800274b0a84',
                         first_name='Joe',last_name='Smith',
                         donations=[{'amount': 100.0, 'date': '2017-12-11Z'}],
                         created='2017-12-11T03:29:16.221954Z' )"
        In [596]:

        In [636]: d=Donor(full_name="john adams")
        In [637]: d.add_donation=1000
        In [638]: repr(d)
        Out[638]: "Donor(did='7e93d724-de25-11e7-bee5-0800274b0a84',
                         first_name='John',last_name='Adams',
                         donations=[{'amount': 1000.0, 'date': '2017-12-11Z'},
                         {'amount': 1000.0, 'date': '2017-12-11Z'}],
                         created='2017-12-11T03:43:47.686457Z' )"
        In [639]:

    """

    created = js.String()
    audit = js.List()
    _did = js.String()
    _first_name = js.String()
    _last_name = js.String()
    _middle_name = js.String()
    _suffix = js.String()
    _donations = js.List()

    def __init__(self,
                 did="",
                 created="",
                 full_name="",
                 first_name="",
                 last_name="",
                 middle_name="",
                 suffix="",
                 donations=None,
                 donation=None
                ):

        self.__name__ = "Donor"

        # normally no did is passed in, so we create one
        if did == "":
            did = str(uuid.uuid1())
        # create a uuid for each record
        self.did = did

        # normally, no timestamp is passed in, so we create one
        if created == "":
            created = datetime.datetime.utcnow().isoformat() + "Z"
        # keep track of record creation
        self.created = created

        # test to see if any of the name components are set
        sub_name_set = any(sub_name != "" for sub_name in (
            first_name,
            middle_name,
            last_name,
            suffix))

        # we don't expect full_name and a subset to be set at the same time
        if full_name != "" and sub_name_set:
            raise ValueError("You cannot set 'full_name' and a subset of the "
                             "name at the same time.")

        # set the name via full_name or via the constituent parts
        if full_name != "":
            self.full_name = full_name
        else:
            self.first_name = first_name.title()
            self.last_name = last_name.title()
            self.middle_name = middle_name.title()
            self.suffix = suffix.upper()

        if (donations is not None) and (donation is not None):
            raise ValueError("You cannot set 'donations' and 'donation' at "
                             "the same time.")

        if donation is not None:
            # if a donation is passed in, initialize the donations,
            # then add the donation
            self._donations = list()
            self.add_donation(donation)
        else:
            if donations is not None:
                # TODO donations need more validation
                self._donations = donations
            else:
                self._donations = list()

    @property
    def did(self):
        """ return the donor did """
        return self._did

    @did.setter
    @audit_log
    def did(self, value):
        """ set the did """
        self._did = value

    @property
    def donations(self):
        """ print all donations """
        return self._donations

    @donations.setter
    @audit_log
    def donations(self, value):
        """ allow bulk setting of donation entries """
        self._donations = value

    @audit_log
    def add_donation(self, value):
        """ add a single donation """
        today = datetime.datetime.utcnow().date().isoformat() + "Z"
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Donations must be values.")
        self._donations.append({"amount": value, "date": today})

    @property
    def number_donations(self):
        """ return the number of donations """
        return len(self._donations)

    @property
    def total_donations(self):
        """ return a sum of the donations """
        total_donations = 0
        for donation in self.donations:
            total_donations += donation["amount"]
        return round(total_donations, 2)

    @property
    def average_donations(self):
        """ return the average donation amount """
        try:
            return round(self.total_donations / self.number_donations, 2)
        except ZeroDivisionError:
            return 0

    @property
    def first_name(self):
        """ return the first name """
        return self._first_name

    @first_name.setter
    @audit_log
    def first_name(self, value):
        """ set the first name """
        self._first_name = value.title()

    @property
    def middle_name(self):
        """ return the middle name """
        return self._middle_name

    @middle_name.setter
    @audit_log
    def middle_name(self, value):
        """ set the middle name """
        self._middle_name = value.title()

    @property
    def last_name(self):
        """ return the last name """
        return self._last_name

    @last_name.setter
    @audit_log
    def last_name(self, value):
        """ set the last name """
        self._last_name = value.title()

    @property
    def suffix(self):
        """ return the suffix """
        return self._suffix

    @suffix.setter
    @audit_log
    def suffix(self, value):
        """ set the suffix """
        # special case roman numbers to all caps
        if value.lower() in ["i", "ii", "iii", "iv", "v"]:
            self._suffix = value.upper()
        else:
            self._suffix = value.title()

    @property
    def informal_name(self):
        """ return full name minus the suffix """
        return " ".join(filter(None, [self.first_name, self.middle_name,
                                      self.last_name]))

    @property
    def full_name(self):
        """ return the formal, full name """
        # if suffix, add with a comma
        if self.suffix != "":
            suffix = ", " + self.suffix
        else:
            suffix = ""
        return " ".join(filter(None, [self.first_name, self.middle_name,
                                      self.last_name])) + suffix

    @full_name.setter
    def full_name(self, full_name):

        """ allow the donor information to be updated via full_name as well """

        # for simplicity's sake, we make the assumption a suffix will
        # follow a comma

        # capture suffix, if present
        suffix = ""
        if full_name.find(","):
            try:
                suffix = full_name.split(",")[1].strip()
            except Exception:
                pass

        # name with suffix removed
        informal_name = full_name.split(",")[0].strip()

        # we assume the last name is one word minus the suffix
        last_name = informal_name.split()[-1]

        # build a list with everything to the left of the last name
        everything_but_last = informal_name.split()[0:-1]

        # pull the first name off
        try:
            first_name = everything_but_last.pop(0)
        except IndexError:
            # if we get an error, they probably gave us a malformed name
            first_name = ""

        try:
            # pull the middle, if exists
            middle_name = everything_but_last.pop(0)
        except IndexError:
            middle_name = ""

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.suffix = suffix

    def _query_attributes(self, which_attributes=(), return_empty=True):
        """ return list of formatted attribute/value entries """
        attributes = []
        for attr in which_attributes:
            # for our purposes, never print internal attributes
            if not attr.startswith("_"):
                try:
                    str_val = repr(getattr(self, attr))
                    # don't return empty values if they don't want them
                    if eval(str_val) or return_empty:
                        attributes.append(attr + "=" + str_val)
                except (AttributeError, SyntaxError):
                    # we know certain attributes are not readable, so skip them
                    pass
        return attributes

    def __repr__(self):
        """
        Return only the (settable) attributes

        Return only settable attributes so
        eval(repr(Donor(<foo>))) == Donor(<foo>)
        """
        which_attributes = ["did", "first_name", "middle_name", "last_name",
                            "suffix",
                            "donations", "created"]
        attributes = self._query_attributes(which_attributes,
                                            return_empty=False)
        return "Donor( " + ", ".join(attributes) + " )"

    def __str__(self):
        """ return all the non-internal attributes """
        which_attributes = []
        for attr in dir(self):
            if not attr.startswith("_"):
                which_attributes.append(attr)
        return "str(Donor(\n    " + ",\n    ".join(
            self._query_attributes(which_attributes)) + " ))"


def load_donor_file(donor_file=None):
    """ load donors from file into Donors object """
    donors = None
    if not donor_file:
        donor_file = os.path.join(os.path.expanduser('~'), '.donors.p')
    try:
        donors = pickle.load(open(donor_file, "rb"))
        return donors
    except FileNotFoundError:
        # if the file isn't found, that's ok, give them
        # an empty donor dict and we'll save anything
        # they enter upon exit.
        return donors
    except PermissionError:
        # if the file is there, but you can't read it, don't continue
        # because you won't be able to save the file on exit, risking
        # loss of data.  Fail early, fail often.
        print("Insufficent permission to access the donor file!")
        print("Please correct the permissions.")
        sys.exit(1)
    except Exception as err:
        # when pickle files are corrupt they can present in lots of ways
        # so if catch something other than what we expect, assume it's
        # a corrupt pickle file
        print("The donors file is invalid!")
        print(err)
        print("If you have run a previous version of Mailroom 2000, it may\n"
              "not be compatible with the current version.\n"
              "Please remove ~/.donors.p and try again.")
        sys.exit(1)


def save_donor_file(donors, donor_file=None):
    """ save donors object to pickle file """
    if not donor_file:
        donor_file = os.path.join(os.path.expanduser('~'), '.donors.p')
    try:
        pickle.dump(donors, open(donor_file, "wb"))
        return True
    except (PermissionError, OSError) as err:
        print("Sorry, couldn't write the donor file!")
        print(err)
        return False
