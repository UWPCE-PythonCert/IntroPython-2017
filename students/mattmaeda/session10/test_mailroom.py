import pytest
from mailroom import Mailroom, Donor

INITIAL_DONORS = {
    "George Washington": 1,
    "John Adams": 3,
    "Thomas Jefferson": 3,
    "John Quincy Adams": 2,
    "James Madison": 1
}

EXPECTED_REPORT = """

Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Monty Python                                       $       10.00           1         10.00
John Adams                                         $        3.00           1          3.00
Thomas Jefferson                                   $        3.00           1          3.00
John Quincy Adams                                  $        2.00           1          2.00
George Washington                                  $        1.00           1          1.00
James Madison                                      $        1.00           1          1.00

"""

CHALLENGE_REPORT_ORIGINAL = """

Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Matt                                               $      100.00           1        100.00
Joe                                                $       40.00           1         40.00

"""

CHALLENGE_REPORT_MATCHING = """

Donor Name                                        | Total Given | Num Gifts | Average Gift
------------------------------------------------------------------------------------------
Matt                                               $      250.00           1        250.00
Joe                                                $      160.00           1        160.00

"""

def test_donor_init():
    donor = Donor("Test User")
    assert donor.name == "Test User"


def test_add_donation():
    donor = Donor("Test User")
    donor.add_donation(100)
    assert 100 in donor.donations


def test_get_donations():
    donor = Donor("Test User")
    donor.add_donation(200)
    donor.add_donation(100)
    assert [200, 100] == donor.get_donations()


def test_get_donation_total_no_donations():
    donor = Donor("Test User")
    assert donor.get_donation_total() == 0


def test_get_donation_total_multiple_donations():
    donor = Donor("Test User")
    donor.add_donation(200)
    donor.add_donation(100)
    assert donor.get_donation_total() == 300


def test_get_total_donations_no_donations():
    donor = Donor("Test User")
    assert donor.get_total_donations() == 0


def test_get_total_donations_multiple_donations():
    donor = Donor("Test User")
    donor.add_donation(200)
    donor.add_donation(100)
    assert donor.get_total_donations() == 2


def test_get_average_donation_no_donation():
    donor = Donor("Test User")
    assert donor.get_average_donation() == 0


def test_get_average_donation_single_donation():
    donor = Donor("Test User")
    donor.add_donation(100)
    assert donor.get_average_donation() == 100.00


def test_get_average_donation_multiple_donation():
    donor = Donor("Test Uesr")
    donor.add_donation(200)
    donor.add_donation(100)
    assert donor.get_average_donation() == 150.00


def test_mailroom_get_menu():
    """ test menu """
    mailroom = Mailroom()
    assert {1: "Send a Thank You",
            2: "Create a Report",
            3: "Model Matching Contribution",
            4: "Quit"} == mailroom.get_menu()


def test_mailroom_add_donation():
    """ test add donation workflow """
    mailroom = Mailroom()
    letter = mailroom.add_donation("Monty Python", 10)

    assert "Monty Python" == mailroom.donors[0].name
    assert [10] == mailroom.donors[0].get_donations()
    assert "\n\nDear Monty Python,\nThank you for your donation of 10.\n\n" == letter


def test_get_or_initialize_donor_new_user():
    """ test adding of new donor """
    mailroom = Mailroom()
    donor = mailroom.get_or_initialize_donor("Test User")
    assert isinstance(donor, Donor)
    assert donor.name == "Test User"
    assert donor in mailroom.donors


def test_send_thanks_single_donation():
    """ test thank you letter """
    mailroom = Mailroom()
    donor = Donor("Monty Python")
    donor.add_donation(10)
    assert "\n\nDear Monty Python,\nThank you for your donation of 10.\n\n" == mailroom.send_thanks(donor)


def test_send_thanks_multiple_donation():
    """ test thank you letter with multiple donations"""
    mailroom = Mailroom()
    donor = Donor("Monty Python")
    donor.add_donation(30)
    donor.add_donation(20)
    donor.add_donation(100)
    donor.add_donation(150)
    donor.add_donation(10)
    assert "\n\nDear Monty Python,\nThank you for your donation of 10.\n\n" == mailroom.send_thanks(donor)


def test_report():
    """ test report generation """
    mailroom = Mailroom()
    for donor, amount in INITIAL_DONORS.items():
        mailroom.add_donation(donor, amount)

    mailroom.add_donation("Monty Python", 10)
    assert EXPECTED_REPORT == mailroom.report()


def test_get_sorted_donors():
    """ test sorting of donors """
    mailroom = Mailroom()
    for donor, amount in INITIAL_DONORS.items():
        mailroom.add_donation(donor, amount)

    mailroom.add_donation("Monty Python", 10)
    sorted_donors = [donor_obj.name for donor_obj in
                     mailroom.sort_donors_by_donation(mailroom.donors)]

    assert ["Monty Python", "John Adams", "Thomas Jefferson",
            "John Quincy Adams", "George Washington",
            "James Madison"] == sorted_donors


def test_get_sorted_donors_with_passed_in_list_of_donors():
    """ test sorting of donor with external donor list """
    mailroom = Mailroom()
    for donor, amount in INITIAL_DONORS.items():
        mailroom.add_donation(donor, amount)

    mailroom.add_donation("Monty Python", 10)

    d1 = Donor("Test One", [1])
    d2 = Donor("Test Two", [1,2,3])
    donor_list = [d1, d2]
    sorted_donors = [donor_obj.name for donor_obj in
                     mailroom.sort_donors_by_donation(donor_list)]

    assert ["Test Two", "Test One"] == sorted_donors


def test_get_donation_match_no_min():
    """ test donation match with no min """
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(10, 3, None, 100)
    assert amount == 30


def test_get_donation_match_with_min_amount_too_small():
    """ test donation match with amount less than minimum """
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(10, 3, 11, 100)
    assert amount == 10


def test_get_donation_match_with_min_amount_equals_amount():
    """ test donation match with amount equal to minimum """
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(10, 3, 10, 100)
    assert amount == 30


def test_get_donation_match_with_min_amount_lt_amount():
    """ test donation match with amount greater than  minimum """
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(11, 3, 10, 100)
    assert amount == 33


def test_get_donation_match_with_no_max_amount():
    """ test donation match with amount greater than minimum no max"""
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(11, 3, 10, None)
    assert amount == 33


def test_get_donation_match_with_amount_lt_max():
    """ test donation match with amount less than max"""
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(11, 3, None, 12)
    assert amount == 33


def test_get_donation_match_with_amount_gt_max():
    """ test donation match with amount greater than max"""
    mailroom = Mailroom()
    amount = mailroom.get_donation_match(10, 3, None, 5)
    assert amount == 20


def test_model_matching_contribution():
    """ test model matching contribution """
    mailroom = Mailroom()
    donor = Donor("Test User", [1,2,3,4])
    new_donor = mailroom.model_matching_contribution(donor, 2, None, None)

    assert len(donor.donations) == len(new_donor.donations)
    assert donor.name == new_donor.name
    assert donor.donations != new_donor.donations


def test_challenge():
    mailroom = Mailroom()
    letter = mailroom.add_donation("Matt", 100)
    letter = mailroom.add_donation("Joe", 40)
    reports = mailroom.challenge(4, max_donation=50)
    assert len(reports) == 2
    assert reports[0] == CHALLENGE_REPORT_ORIGINAL
    assert reports[1] == CHALLENGE_REPORT_MATCHING
