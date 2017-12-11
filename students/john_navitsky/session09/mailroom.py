#!/usr/bin/env python3

import sys
import json
import datetime
import hashlib
from pprint import pprint
import uuid

""" Program to manage donations. """

class Donors:

    """
    Class that stores donor records

    """

    def __init__(self, donor=None):
        # TODO:
        #   donors should take a donor or LIST of donors
        self._donors = {}
        if donor:
            self.add_donor = donor

    def __repr__(self):
        repr_out=[]
        for key in self._donors:
            repr_out.append( repr(self._donors[key]) )
        return "Donors( " + ", ".join(repr_out) + " )"

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        return iter(self.full_name_index)

    @property
    def add_donor(self):
        """ you can't read a donor via add_donor """
        raise AttributeError("You can't READ a donor via ADD_donor. Use get_donor instead.")

    @add_donor.setter
    def add_donor(self, donor):
        """
        add a donor to the donors database

        The add_donor method leverages the donor id which allows
        you to update or add a record using the same method.
        """
        self._donors[donor.id] = donor

    @property
    def number_donors(self):
        """ return the number of donor records """
        return len(self._donors)

    def get_donor(self, id):
        """ given a donor id, return the donor object """
        return self._donors[id]

    @property
    def full_name_index(self):
        """ Provide an index of keys, full_name, last_name and first_name """
        index=[]
        for key in self._donors:
            index.append( (self._donors[key].full_name, key, 
                self._donors[key].last_name,
                self._donors[key].first_name ) )
        return sorted(index)

    def match_donor(self, query_full_name):
        """ 
        find all records that match the query string

        return tupple with full_name, id

        """
        matches=[]
        for name, id, _, _ in self.full_name_index:
            if query_full_name.strip().lower() == name.lower():
                matches.append( (name, id) )
        return matches


class Donor:

    """
    Class to store a donor record 

    Args:
        full_name(str)      format: <first name> [<middle_name>] <last_name> [,<suffix>]
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
        id(str)             string representation of a record UUID
        created(str)        string representation of an utcnow isoformat timestamp
                            with "Z" appended

    Usage:

        The class allows flexibility in how a record is set.  It is allowable
        to create an empty instance of the class and update it piecemeal.  

        It is also allowable to pass in all information needed to create a record
        using different strategies such as a full_name vs the constituent parts.

        In general, record manipulation is simply the name and donation.  However,
        it is also allowable to set information that is normally auto-created
        such as the id, time created and entire donation list.  This allows
        a record to be created from its repr which may have practical uses in
        record backup/recreation as needed.

    Example Use Cases:

        # empty donor record
        In [599]: d=Donor()
        In [600]: repr(d)
        Out[600]: "Donor( id='97d744de-de23-11e7-bee5-0800274b0a84', 
            created='2017-12-11T03:30:11.077937Z' )"
        In [601]:

        # automatic parsing of full_name
        In [601]: d=Donor(full_name="sally q smith, iv")
        In [602]: repr(d)
        Out[602]: "Donor( id='067f51c4-de24-11e7-bee5-0800274b0a84', first_name='Sally', 
            middle_name='Q', last_name='Smith', suffix='IV', 
            created='2017-12-11T03:33:16.728654Z' )"
        In [603]:

        # name creation based name sub-components
        In [594]: d=Donor(first_name="joe", last_name="smith", donation=100)
        In [595]: repr(d)
        Out[595]: "Donor( id='7724e750-de23-11e7-bee5-0800274b0a84', first_name='Joe', 
            last_name='Smith', donations=[{'amount': 100.0, 'date': '2017-12-11Z'}], 
            created='2017-12-11T03:29:16.221954Z' )"
        In [596]:    

        In [636]: d=Donor(full_name="john adams")
        In [637]: d.add_donation=1000
        In [638]: repr(d)
        Out[638]: "Donor( id='7e93d724-de25-11e7-bee5-0800274b0a84', first_name='John', 
            last_name='Adams', donations=[{'amount': 1000.0, 'date': '2017-12-11Z'}, 
            {'amount': 1000.0, 'date': '2017-12-11Z'}], created='2017-12-11T03:43:47.686457Z' )"
        In [639]:

    """

    def __init__(self, 
            id="", created="",
            full_name="",
            first_name="", last_name="", middle_name="", suffix="",
            donations=[], donation=None):

        # normally no id is passed in, so we create one
        if id == "":
            id = str(uuid.uuid1())
        # create a uuid for each record
        self._id = id

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
            raise ValueError("You cannot set 'full_name' and a subset of the name at the same time.")

        # set the name via full_name or via the constituent parts
        if full_name != "":
            self.full_name = full_name
        else:
            self._first_name = first_name.title()
            self._last_name = last_name.title()
            self._middle_name = middle_name.title()
            self._suffix = suffix.upper()

        if (len(donations) != 0) and (donation != None):
            raise ValueError("You cannot set 'donations' and 'donation' at the same time.")

        if donation != None:
            # if a donation is passed in, initialize the donations, then add the donation
            self._donations = list()
            self.add_donation(donation)
        else:
            # if they've passed in a pre-formatted donation list, accept it
            self._donations = donations

    @property
    def id(self):
        """ return the donor id """
        return self._id

    @id.setter
    def id(self, value):
        """ donor id cannot be changed once established """
        raise AttributeError("You cannot change the 'id' after the record has been created.")

    @property
    def donations(self):
        """ print all donations """
        return self._donations

    @donations.setter
    def donations(self, value):
        """ allow bulk setting of donation entries """
        self._donations = value

    # @property
    # def add_donation(self):
    #     """ reading not allowed via add_donation """
    #     raise AttributeError("Read donations with the 'donations' attribute, instead.")

    #@add_donation.setter
    def add_donation(self, value):
        """ add a single donation """
        today = datetime.datetime.utcnow().date().isoformat() + "Z"
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Donations must be values.")
        self._donations.append( { "amount": value, "date": today } )

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
    def first_name(self, value):
        """ set the first name """
        self._first_name = value.title()

    @property
    def middle_name(self):
        """ return the middle name """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        """ set the middle name """
        self._middle_name = value.title()

    @property
    def last_name(self):
        """ return the last name """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ set the last name """
        self._last_name = value.title()

    @property
    def suffix(self):
        """ return the suffix """
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        """ set the suffix """
        # special case roman numbers to all caps
        if value in ["i" "ii", "iii", "iv", "v"]:
            self._suffix=value.upper()
        else:
            self._suffix=value.title()

    @property
    def informal_name(self):
        """ return full name minus the suffix """
        return " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

    @property
    def full_name(self):
        """ return the formal, full name """
        return " ".join(filter(None, [self.first_name, self.middle_name, self.last_name, self.suffix]))

    @full_name.setter
    def full_name(self, full_name):

        """ allow the donor information to be updated via full_name as well """

        # for simplicity's sake, we make the assumption a suffix will follow a comma

        # capture suffix, if present
        suffix=""
        if full_name.find(","):
            try:
                suffix=full_name.split(",")[1].strip()
            except:
                pass

        # name with suffix removed
        informal_name=full_name.split(",")[0].strip()

        # we assume the last name is one word minus the suffix
        last_name=informal_name.split()[-1]
       
        # build a list with everything to the left of the last name
        everything_but_last=informal_name.split()[0:-1]

        # pull the first name off
        first_name=everything_but_last.pop(0)

        try:
            # pull the middle, if exists
            middle_name=everything_but_last.pop(0)
        except IndexError:
            middle_name=""

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.suffix = suffix

    def _query_attributes(self, which_attributes=[], return_empty=True):
        """ return list of formatted attribute/value entries """
        attributes = []
        for attr in which_attributes:
            # for our purposes, never print internal attributes
            if not attr.startswith("_"):
                try:
                    str_val=repr(getattr(self,attr))
                    # don't return empty values if they don't want them
                    if eval(str_val) or return_empty:
                        attributes.append( attr + "=" + str_val)
                except AttributeError:
                    # we know certain attributes are not readable, so skip them
                    pass
        return attributes

    def __repr__(self):
        """ return only the (settable) attributes needed to create the record """
        which_attributes=["id", "first_name","middle_name","last_name","suffix",
            "donations", "created"]
        attributes = self._query_attributes(which_attributes, return_empty=False)
        return "Donor( " + ", ".join(attributes) + " )"

    def __str__(self):
        """ return all the non-internal attributes """
        which_attributes=[]
        for attr in dir(self):
            if not attr.startswith("_"):
                which_attributes.append(attr)
        return "DONOR: " + ", ".join(self._query_attributes(which_attributes))
        

def load_donor_file(donor_file="donors.json"):
    """ load donors from file into dict, donors """
    try:
        with open(donor_file,'r') as donor_data:
            try:
                donors = json.load(donor_data)
            except (json.decoder.JSONDecodeError) as e:
                # catch malformed json
                print("The donors file is corrupt!")
                print(e)
                print("Please correct or delete the file.")
                sys.exit(1)
            return donors
    except (FileNotFoundError):
            # if the file isn't found, that's ok, give them
            # an empty donor dict and we'll save anything
            # they enter upon exit.
            return {}
    except (PermissionError):
        # if the file is there, but you can't read it, don't continue
        # because you won't be able to save the file on exit, risking
        # loss of data.  Fail early, fail often.
        print("Insufficent permission to access the donor file!")
        print("Please correct the permissions.")
        sys.exit(1)


def save_donor_file(donors,donor_file="donors.json"):
    """ save donors to json file """
    try:
        with open(donor_file,'w') as donor_data:
            donor_data.write(json.dumps(donors))
        return True
    except (PermissionError,OSError) as e:
        print("Sorry, couldn't write the donor file!")
        print(e)
        return False


def safe_input(prompt=">",mock=False,mock_in=""):
    """ Generic input routine. """
    # return null if anything goes wrong
    if not mock:
        # normal input mode
        try:
            selection=input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            # don't exit the program on ctrl-c, ctrl-d
            selection=""
        return selection
    else:
        # return what the test program told you to
        return mock_in


def print_lines(lines=2,dest=sys.stdout):
    """ Print variable number of linefeeds for clarity. """

    for i in range(lines):
        print("",file=dest)

def list_donors(donors,dest=sys.stdout):

    # print report header
    #      index    name   total gvn #gifts  avg gift
    print("{0:20} | {1:14} | {2:9} | {3:12}".format(
        "Donor Name","Total Given","Num Gifts","Average Gift"),file=dest)
    print("-"*72,file=dest)

    # for name, id, _, _ in donors:
    
    #     donor=donors.get_donor(id)

    #     #                 name     total gvn    #gifts    avg gift
    #     print("{0:20}  ${1:14,.2f}   {2:9.0f}  ${3:12,.2f}".format(
    #         donor.full_name,
    #         donor.total_donations,
    #         donor.number_donations,
    #         donor.average_donations), file=dest)
    #     print("{}".format(donor))
    #     print(donor.total_donations)

    print_lines(2,dest)
    print(repr(donors))
    print_lines(2,dest)

def print_report(donors,dest=sys.stdout):
    """ Print formatted list of all donors. """

    print_lines(2,dest)
  
    # print report header
    #      index    name   total gvn #gifts  avg gift
    print("{0:20} | {1:14} | {2:9} | {3:12}".format(
        "Donor Name","Total Given","Num Gifts","Average Gift"),file=dest)
    print("-"*72,file=dest)

    for donor_id in donors:

        donor=donors[donor_id]

        num_donations=len(donor["donations"])

        total_donations = 0
        for donation in donor["donations"]:
            total_donations += donation["amount"]

        average_donation = total_donations / num_donations

        #                 name     total gvn    #gifts    avg gift
        print("{0:20}  ${1:14,.2f}   {2:9.0f}  ${3:12,.2f}".format(
            donor["full_name"],
            total_donations,
            num_donations,
            average_donation), file=dest)


def parse_name(entered_name):
        """ Convert string name into constituent parts, return dict of parts. """

        # capture suffix, if present.  we assume it will follow a comma
        try:
            suffix=entered_name.split(",")[1].strip().upper()
        except:
            suffix=""

        # name with suffix removed
        informal_name=entered_name.split(",")[0].strip().title()

        # we assume the last name is one word minus the suffix
        last_name=informal_name.split()[-1].strip().title()
       
        # we assume the first name(s) is everything to the left of the last name
        first_name=" ".join(informal_name.split()[0:-1]).title()

        # ensure standard capitalization in suffix
        if suffix:
            new_full_name=", ".join([informal_name, suffix])
        else:
            new_full_name=informal_name

        return { "full_name": new_full_name, "informal_name": informal_name,
            "suffix": suffix, "last_name": last_name, "first_name": first_name }


def get_donation_amount(current_donor):
    """ Get a donation. """

    menu =  "\n"
    menu += "GIFT ENTRY (ammount)\n"
    menu += "-----------------------\n"
    menu += "\n"
    menu += "Enter the numeric amount {informal_name} has donated or\n"
    menu += "(q)uit to return to cancel the donation and\n"
    menu += "return to the previous menu.\n"
    menu += "\n"

    amount=0
    while amount==0:

        print_lines()

        #print(menu.format(**current_donor))
        selection=safe_input("Donation amount or (q)uit: ")

        # let them bail if they want
        if selection.lower() in ["q", "quit"]:
            return None

        # protect against non numeric input
        try:
            amount=float(selection)
            return amount
        except ValueError:
            print_lines()
            print("The value must be numeric.  Please try again or (q)uit.")

def print_thank_you(current_donor,hint="wonderful",dest=sys.stdout):
    """ Print a thank you letter. """

    letter =  "\n"
    letter += "Dearest {full_name},\n"
    letter += "\n"
    letter += "We are are grateful for the generious donation on the behalf of\n"
    letter += "the {last_name} family.\n"
    letter += "\n"
    letter += "It is through the donations of {} patrions like yourself that\n"
    letter += "allows us to continue to support the community.\n"
    letter += "\n"
    letter += "Sincerely,\n"
    letter += "\n"
    letter += "Tux Humboldt\n"
    letter += "Shark Loss Prevention Institue\n"

    print_lines(2,dest)
    print("-"*80,file=dest)

    print(letter.format(hint,**current_donor),file=dest)

    print("-"*80,file=dest)
    print_lines(2,dest)


def match_donor(current_donor, donors):
        """ See if record matches existing record, if so, return full record. """
        for donor_id in donors:
            existing_donor=donors[donor_id]
            if existing_donor["full_name"].lower() == current_donor["full_name"].lower():
                # if the owner exists, pull in the complete donor record
                current_donor=existing_donor
        return current_donor


def update_donor(current_donor, donors, new_donation):
        """ Update the donor database with new donation or donor record as needed. """

        # match to existing record, if exists
        current_donor = match_donor(current_donor, donors)

        # datetime.datetime.strptime(<iso date>,'%Y-%m-%dZ')
        today = datetime.datetime.utcnow().date().isoformat() + "Z"

        # add donation to an existing donor
        if "donor_id" in current_donor.keys():
            donor_id=current_donor["donor_id"]
            donors[donor_id]["donations"].append({ "amount": new_donation, "date": today })
            hint="returning"
        else:
            # datetime.datetime.strptime(<iso time>,'%Y-%m-%dT%H:%M:%S.%fZ')
            now = datetime.datetime.utcnow().isoformat() + "Z"
            # id is a hash of the full donor name plus high resolution time
            id_seed = current_donor["full_name"] + now
            donor_id = hashlib.md5( id_seed.encode() ).hexdigest()
            # add the donor
            donors[donor_id] = { 
                "created": now,
                "donor_id": donor_id,
                "donations": [ { "amount": new_donation, "date": today } ],
                **current_donor } 
            hint="new"


def thank_you_entry(donors):
    """ Enter new donation and send thank you. """

    menu =  "\n"
    menu += "DONATION ENTRY (Donor Name)\n"
    menu += "---------------------------\n"
    menu += "\n"
    menu += "Enter the full name (first last) of the donor\n"
    menu += "for whom you would like to enter a donation,\n"
    menu += "(l)ist to see a list of the existing donors, or\n"
    menu += "(q)uit to return to the previous menu.\n"
    menu += "\n"

    while True:

        print_lines()

        print(menu)
        selection=safe_input("Donor Name, (l)ist or (q)uit: ")

        # check for a quit directive
        if selection.lower() in ["q", "quit"]:
            return

        # check for a list directive
        if selection.lower() in ["l", "list"]:
            print_report(donors)
            continue

        # protect against no entry
        if not selection:
            continue

        # parse the string into name components
        current_donor=parse_name(selection)

        # reject blatantly bad input
        if current_donor["first_name"] == "" or current_donor["last_name"] == "":
            print("You must enter both a first and last name.")
            continue

        # prompt for new donation, cancel if None returned
        new_donation=get_donation_amount(current_donor)
        if new_donation is None:
            print_lines()
            print("Donation cancelled!")
            return

        # update the donor list with the new donation
        hint = update_donor(current_donor, donors, new_donation)

        # thank the donor for the new donation
        print_thank_you(current_donor,hint)



def data_entry():
    """ Enter new donation and send thank you. """

    menu =  "\n"
    menu += "DONATION ENTRY (Donor Name)\n"
    menu += "---------------------------\n"
    menu += "\n"
    menu += "Enter the full name (first last) of the donor\n"
    menu += "for whom you would like to enter a donation,\n"
    menu += "(l)ist to see a list of the existing donors, or\n"
    menu += "(q)uit to return to the previous menu.\n"
    menu += "\n"

    #stub it out
    donorsx=Donors()

    while True:

        print_lines()

        print(menu)
        selection=safe_input("Donor Name, (l)ist or (q)uit: ")

        # check for a quit directive
        if selection.lower() in ["q", "quit"]:
            return

        # check for a list directive
        if selection.lower() in ["l", "list"]:
            list_donors(donorsx)
            continue

        # protect against no entry
        if not selection:
            continue

        # reject blatantly bad input
        # if current_donor["first_name"] == "" or current_donor["last_name"] == "":
        #     print("You must enter both a first and last name.")
        #     continue

        # parse the string into name components
        matches=donorsx.match_donor(selection)
 
        if len(matches) == 0:
            # if there are no matches, go ahead and create a donor record
            current_donor=Donor(full_name=selection)
            donorsx.add_donor=current_donor 

        if len(matches) == 1:
            # if there is an exact match, let's use that one
            current_donor=donorsx.get_donor(matches[0][1])
 
        # prompt for new donation, cancel if None returned
        new_donation=get_donation_amount(current_donor)
        if new_donation is None:
            print_lines()
            print("Donation cancelled!")
            return

        #print(repr(current_donor))

        # update the donor list with the new donation
        #hint = update_donor(current_donor, donors, new_donation)
        current_donor.add_donation(new_donation)
 

        # thank the donor for the new donation
        # print_thank_you(current_donor,hint)


def thank_all_donors(donors,dest_override=None):
    """ loop through donors, open file, print a thank you letter. """
    for donor_id in donors:
        donor=donors[donor_id]
        file_name="_".join(filter( None, [ "thank_you", donor["last_name"], donor["suffix"], donor["first_name"] ])).lower()
        file_name=file_name.replace(" ", "_")
        if not dest_override:
            dest = open(file_name, "w")
        else:
            dest = dest_override
        print_thank_you(donor,"wonderful",dest)
        if not dest_override:
            dest.close()


def main(donors):
    """ Main menu / input loop. """
    
    menu =  "\n"
    menu += "DONATION WIZARD MAIN MENU\n"
    menu += "-------------------------\n"
    menu += "\n"
    menu += "Select from the following:\n"
    menu += "\n"
    menu += "(L)ist Donors\n"
    menu += "(E)nter/(A)dd Donation\n"
    menu += "(P)rint Donor Letters\n"
    menu += "(Q)uit\n"
    menu += "\n"

    selection=None
    while selection not in ["0", "quit", "q"]:

        print_lines()

        print(menu)
        selection=safe_input("(l)ist, (e)nter, (q)uit: ").lower()

        if selection in ["x"]:
            data_entry()

        if selection in ["l", "list"]:
            print_report(donors)

        if selection in ["p", "print"]:
            thank_all_donors(donors)

        # accept either send or enter
        if selection in ["s", "send", "e", "enter", "a", "add"]:
            thank_you_entry(donors)

        if selection in ["d", "debug"]:
            print_lines()
            pprint(donors)
            print_lines()

        if selection in ["q", "quit"]:
            saved = save_donor_file(donors)
            if saved:
                print("{} donor records saved.".format(len(donors)))
            else:
                print("Please resolve the issues with the donor file before exiting.")
                # if you are testing, don't get stuck in the loop
                if mock:
                    mock_in="exit"
                shall_abort = safe_input("Enter 'exit' to quit anyways and abandon changes:",mock)
                if not 'exit' in shall_abort:
                    # if they don't want to exit, clear the selection so we don't exit
                    selection = None

    print_lines()
    print("Thank you for using Donation Wizard!")
    print_lines()


# call the main input loop
if __name__ == "__main__":
    donors = load_donor_file()
    main(donors)


