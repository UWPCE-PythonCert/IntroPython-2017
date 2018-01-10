import os
import mailroom2 as mailroom 



mailroom.donor_db = mailroom.read_donors()
# print(mailroom.donor_db)

def test_list_donors():
    listing = mailroom.donor_db

    assert "Jeff Bezos" in listing
    assert "Donor Name - Donations with comma dilimiter" not in listing
    assert len(listing) == 5

def test_donor_missing():
    listing = mailroom.donor_db

    assert "jeff bezos"  not in listing







if __name__ == "__main__":
    test_list_donors()
    test_donor_missing()
