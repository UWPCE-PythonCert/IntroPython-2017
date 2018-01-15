#!/usr/bin/env python3

from mailroom.donors import load_donor_file, Donors
from mailroom.ui import main

# call the main input loop
if __name__ == "__main__":
    donors = load_donor_file()
    if donors is None:
        donors=Donors()

    main(donors)
